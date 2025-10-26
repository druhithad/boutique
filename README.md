
# Django Boutique App

**Druhitha Duggirala’s Fashion Boutique App** is a Django-based e-commerce application designed to manage boutique operations efficiently. The project demonstrates core Django concepts, including models, views, templates, URL routing, and app separation (`shop` and `cart`).

---

## Repository Description
**Django Boutique App** | A fashion e-commerce platform with cart and shop management functionalities.

---

## Features

### Shop App
- Display and categorize products
- Product search functionality
- Product detail pages

### Cart App
- Add, update, and remove products from the cart
- Simulated checkout functionality

### Admin Panel
- Manage products, categories, and orders
- Full CRUD support for app data

---

## Project Structure

project_folder/
├── cart/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── templates/
│ └── static/
├── shop/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── templates/
│ └── static/
├── project_name/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── manage.py
├── requirements.txt
└── case studies druhitha.docx


> **Important:** The file `case studies druhitha.docx` contains **step-by-step instructions** for running the project, understanding each feature, and following the implementation process. Anyone can set up and explore the app easily by following this document.

---

## Installation & Setup

1. Clone the repository:
git clone <your-repo-link>
cd <project-folder>
Create and activate a virtual environment: python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
Install dependencies: pip install -r requirements.txt
Apply migrations: python manage.py migrate
Run the development server: python manage.py runserver
Open your browser at http://127.0.0.1:8000/ to access the app.

