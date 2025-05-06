# 📦 PyStock

![PyStock](https://img.shields.io/badge/PyStock-Inventory%20Management-blue?style=flat-square)
![Flask](https://img.shields.io/badge/Flask-v2.0+-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

A simple, intuitive, and extensible inventory management system built with Flask and SQLite. Designed to help small businesses, labs, or personal projects track product stock levels, expiration dates, and historical movements with ease.

---

## 🚀 Motivation

Many existing inventory systems are either too complex or locked behind expensive paywalls. This project aims to provide:

- A lightweight, open-source alternative.
- An intuitive UI for tracking products, quantities, and expiration dates.
- A foundation that's easy to customize and extend for specific needs.

Whether you're managing medical supplies, hardware tools, or groceries, this system helps ensure you never run out of critical items or let them expire unnoticed.

---

## 📚 Features

- ✅ Add, update, and delete products with expiration tracking.
- ⚠️ Alerts for low stock or near-expiry items.
- 📊 Full movement history for all stock changes.
- 🔍 Search, filter, and export to Excel.
- 📈 Dashboard with real-time stock visualizations.

---

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Docker, Heroku, Render, Railway

---

## ☁️ Deployment Options

### 💡 Render / Railway
1. Fork this repo.
2. Connect your GitHub to the platform.
3. Set Python as the environment and add `requirements.txt` and `app.py` as the entry points.

### 🐳 Docker
```bash
docker build -t inventory-app .
docker run -p 5000:5000 inventory-app
```

### 🔁 Heroku (with Gunicorn)
```bash
pip install gunicorn
echo "web: gunicorn app:app" > Procfile
heroku create
git push heroku main
```

---

## 🖥️ Local Development

To run the project locally:

```bash
# Clone the repository
git clone https://github.com/yourusername/inventory-system.git

# Navigate to the project directory
cd inventory-system

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🌟 Acknowledgments

- [Flask](https://flask.palletsprojects.com/) for the web framework.
- [Chart.js](https://www.chartjs.org/) for the data visualizations.
- Open-source contributors for inspiration and guidance.
