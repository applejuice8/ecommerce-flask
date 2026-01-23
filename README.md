# Ecommerce Flask

![Screenshot](screenshot.png)

An ecommerce website built in Python using Flask, SQLAlchemy, SQLite, WTForms and Bootstrap.

## Features
- Authentication (Login, Signup)
- CSRF-protected WTForms
- Add to cart
- Modify quantity of items
- Mock checkout system

## Project Structure
```bash
├── app/
│   ├── __init__.py     # Application factory, Blueprint registration
│   ├── api.py          # API endpoints used by JavaScript
│   ├── auth.py
│   ├── cart.py
│   ├── errors.py       # Error handlers
│   ├── extensions.py   # Initializes Flask extensions
│   ├── forms.py        # Flask WTForms
│   ├── home.py
│   ├── models/         # Database models
│   │   ├── __init__.py
│   │   ├── cart_item.py
│   │   ├── cart.py
│   │   ├── product.py
│   │   └── user.py
│   ├── static/         # Static assets
│   │   ├── css/
│   │   ├── images/
│   │   │   └── no-image.jpg
│   │   └── js/
│   │       ├── cart.js
│   │       └── index.js
│   └── templates/      # Jinja2 HTML templates
│       ├── base.html
│       ├── cart.html
│       ├── errors/
│       │   ├── 404.html
│       │   └── 500.html
│       ├── index.html
│       ├── login.html
│       └── signup.html
├── config.py           # Application configuration
├── generate_products.py    # Generate sample product data
├── instance
│   └── app.db
├── README.md
├── requirements.txt
└── wsgi.py             # WSGI entry point for running the app
```
