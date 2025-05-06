from flask import Flask, render_template, request, redirect, url_for, send_file
import sqlite3
import os
from datetime import date, datetime
from openpyxl import Workbook
from io import BytesIO
import json

app = Flask(__name__)
DATABASE = 'database.db'


def init_db():
    """Initializes the SQLite database and creates necessary tables if they do not exist."""
    if not os.path.exists(DATABASE):
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    code TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    expiration_date TEXT NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE movements (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id INTEGER,
                    type TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    date TEXT NOT NULL,
                    FOREIGN KEY (product_id) REFERENCES products(id)
                )
            ''')
            conn.commit()


@app.route('/')
def index():
    """
    Renders the main inventory page.
    Supports optional filtering using a search query.
    Displays products and recent stock movements.
    Also passes the current date to the form as default and minimum expiration date.
    """
    query = request.args.get('q', '').strip()
    today = date.today().isoformat()

    with sqlite3.connect(DATABASE) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        if query:
            cursor.execute("SELECT * FROM products WHERE name LIKE ? OR code LIKE ?",
                           (f'%{query}%', f'%{query}%'))
        else:
            cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()

        products = []
        for row in rows:
            exp_date = datetime.strptime(row['expiration_date'], '%Y-%m-%d').date()
            days_left = (exp_date - date.today()).days
            products.append({
                'id': row['id'],
                'name': row['name'],
                'code': row['code'],
                'quantity': row['quantity'],
                'expiration_date': row['expiration_date'],
                'low_stock': row['quantity'] < 5,
                'expiring_soon': days_left <= 7
            })

        cursor.execute('''
            SELECT m.date, p.name, m.type, m.quantity 
            FROM movements m
            JOIN products p ON m.product_id = p.id
            ORDER BY m.date DESC
            LIMIT 20
        ''')
        movements = cursor.fetchall()

    product_names = [p['name'] for p in products]
    product_quantities = [p['quantity'] for p in products]

    return render_template('index.html',
                           products=products,
                           movements=movements,
                           names_json=json.dumps(product_names),
                           quantities_json=json.dumps(product_quantities),
                           query=query,
                           today=today)


@app.route('/add', methods=['POST'])
def add_product():
    """
    Adds a new product to the inventory.
    Also logs an 'Add' movement entry.
    Validates that the expiration date is not earlier than today.
    """
    name = request.form['name']
    code = request.form['code']
    quantity = int(request.form['quantity'])
    expiration_date = request.form['expiration_date']
    today = date.today()

    try:
        exp_date_obj = datetime.strptime(expiration_date, '%Y-%m-%d').date()
    except ValueError:
        return "Invalid expiration date format", 400

    if exp_date_obj < today:
        return "Expiration date cannot be earlier than today.", 400

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO products (name, code, quantity, expiration_date)
            VALUES (?, ?, ?, ?)
        ''', (name, code, quantity, expiration_date))
        product_id = cursor.lastrowid

        cursor.execute('''
            INSERT INTO movements (product_id, type, quantity, date)
            VALUES (?, ?, ?, ?)
        ''', (product_id, 'Add', quantity, expiration_date))

        conn.commit()
    return redirect(url_for('index'))


@app.route('/delete/<int:product_id>')
def delete_product(product_id):
    """
    Deletes a product from the inventory by ID.
    """
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
        conn.commit()
    return redirect(url_for('index'))


@app.route('/update/<int:product_id>', methods=['POST'])
def update_product(product_id):
    """
    Updates the quantity of a product.
    Logs a movement with the difference (entry or exit).
    """
    new_quantity = int(request.form['quantity'])

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT quantity FROM products WHERE id=?", (product_id,))
        current = cursor.fetchone()

        if current:
            old_quantity = current[0]
            difference = new_quantity - old_quantity

            if difference != 0:
                movement_type = 'Entry' if difference > 0 else 'Exit'
                cursor.execute("UPDATE products SET quantity=? WHERE id=?", (new_quantity, product_id))
                cursor.execute('''
                    INSERT INTO movements (product_id, type, quantity, date)
                    VALUES (?, ?, ?, ?)
                ''', (product_id, movement_type, abs(difference), datetime.now().strftime('%Y-%m-%d')))
                conn.commit()

    return redirect(url_for('index'))


@app.route('/history')
def history():
    """
    Displays the full movement history.
    """
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT m.date, p.name, m.type, m.quantity
            FROM movements m
            JOIN products p ON m.product_id = p.id
            ORDER BY m.date DESC
        ''')
        movements = cursor.fetchall()
    return render_template('history.html', movements=movements)


@app.route('/export')
def export_excel():
    """
    Exports current inventory data to an Excel file.
    """
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name, code, quantity, expiration_date FROM products")
        products = cursor.fetchall()

    wb = Workbook()
    ws = wb.active
    ws.title = "Inventory"
    ws.append(["Name", "Code", "Quantity", "Expiration Date"])

    for product in products:
        ws.append(product)

    output = BytesIO()
    wb.save(output)
    output.seek(0)

    return send_file(
        output,
        as_attachment=True,
        download_name="inventory.xlsx",
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


if __name__ == '__main__':
    init_db()
    app.run(debug=True)