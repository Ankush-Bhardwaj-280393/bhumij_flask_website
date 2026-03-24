# bhumij_flask_website
Website made for bhumij plants with Flask framework


The folder structure is :
plant_shop/
├── app/
│   ├── __init__.py          # App factory & extension initialization
│   ├── models.py            # Database schemas (Plant, User, Order)
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── main.py          # Home, catalog, and search
│   │   ├── auth.py          # Login, Register, Logout
│   │   └── cart.py          # Add/remove items, checkout
│   ├── static/              # CSS, JS, and Plant Images
│   │   ├── css/
│   │   └── img/
│   └── templates/           # Jinja2 HTML files
│       ├── base.html
│       ├── index.html
│       ├── product_detail.html
│       └── checkout.html
|       └── login.html
|       └── register.html
├── config.py                # Secret keys and Database URI
├── requirements.txt         # Dependencies (Flask, Flask-SQLAlchemy, etc.)
└── run.py                   # Entry point to start the server