# 📖 PyStock Developer Documentation

Welcome to the PyStock developer documentation! This guide provides all the information you need to understand, contribute to, and extend the PyStock project.

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Development Workflow](#development-workflow)
- [API Endpoints](#api-endpoints)
- [Database Schema](#database-schema)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)

---

## 📦 Project Overview

PyStock is an inventory management system built with Flask and SQLite. It provides features like product tracking, expiration alerts, stock visualizations, and movement history.

### Key Technologies
- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript (Chart.js)
- **Deployment**: Docker, Heroku, Render, Railway

---

## 🛠️ Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/inventory-system.git
   cd inventory-system
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Access the app at [http://localhost:5000](http://localhost:5000).

---

## 📂 Project Structure

```
/c:/Repos/PyStock/
├── app/
│   ├── templates/         # HTML templates
│   ├── static/            # Static files (CSS, JS)
│   ├── __init__.py        # App initialization
│   ├── routes.py          # Flask routes
│   ├── models.py          # Database models
│   └── utils.py           # Utility functions
├── tests/                 # Unit and integration tests
├── requirements.txt       # Python dependencies
├── README.md              # Project overview
├── CONTRIBUTING.md        # Contribution guidelines
├── CODE_OF_CONDUCT.md     # Code of conduct
└── RELEASE.md             # Release notes
```

---

## 🔄 Development Workflow

1. **Create a Branch**:  
   Always create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature/my-feature-name
   ```

2. **Make Changes**:  
   Implement your changes and ensure they follow the [Style Guide](#style-guide).

3. **Run Tests**:  
   Run the test suite to ensure your changes don't break anything:
   ```bash
   pytest
   ```

4. **Commit and Push**:  
   Commit your changes with a meaningful message:
   ```bash
   git add .
   git commit -m "✨ Add: short description of what you changed"
   git push origin feature/my-feature-name
   ```

5. **Open a Pull Request**:  
   Submit a pull request with a detailed description of your changes.

---

## 🌐 API Endpoints

### Product Management
- **GET /**: View all products.
- **POST /add**: Add a new product.
- **POST /update/<id>**: Update product quantity.
- **GET /delete/<id>**: Delete a product.

### Export
- **GET /export**: Export inventory data to Excel.

---

## 🗄️ Database Schema

### Products Table
| Column           | Type        | Description                     |
|-------------------|-------------|---------------------------------|
| `id`             | Integer     | Primary key                     |
| `name`           | Text        | Product name                    |
| `code`           | Text        | Unique product code             |
| `quantity`       | Integer     | Quantity in stock               |
| `expiration_date`| Date        | Expiration date of the product  |

### Movements Table
| Column           | Type        | Description                     |
|-------------------|-------------|---------------------------------|
| `id`             | Integer     | Primary key                     |
| `date`           | DateTime    | Date of the movement            |
| `product_id`     | Integer     | Foreign key to Products table   |
| `type`           | Text        | Movement type (add/update)      |
| `quantity`       | Integer     | Quantity involved in the movement |

---

## 🧪 Testing

### Running Tests
Run the test suite using `pytest`:
```bash
pytest
```

### Adding Tests
Add your tests in the `tests/` directory. Use descriptive names for test files and functions.

---

## ☁️ Deployment

### Docker
1. Build the Docker image:
   ```bash
   docker build -t inventory-app .
   ```

2. Run the container:
   ```bash
   docker run -p 5000:5000 inventory-app
   ```

### Heroku
1. Install Gunicorn:
   ```bash
   pip install gunicorn
   ```

2. Create a `Procfile`:
   ```bash
   echo "web: gunicorn app:app" > Procfile
   ```

3. Deploy to Heroku:
   ```bash
   heroku create
   git push heroku main
   ```

---

## 🤝 Contributing

Refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file for detailed contribution guidelines.

---

Thank you for contributing to PyStock! 💙
