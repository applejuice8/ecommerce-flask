from app import create_app
from app.extensions import db
from app.models import Product
import random

product_names = [
    'Wireless Mouse', 'Bluetooth Speaker', 'USB-C Charger', 'Laptop Stand',
    'Noise Cancelling Headphones', 'Smartphone Case', 'Gaming Keyboard',
    'HDMI Cable', 'Portable SSD', 'Smartwatch'
]

product_descriptions = [
    'High-quality and durable', 'Best seller product', 'Limited edition',
    'Compact and portable', 'User-friendly design', 'Top-rated by customers',
    'Affordable and reliable', 'Premium build quality', 'Perfect for daily use',
    'Sleek and modern design'
]

app = create_app()

with app.app_context():
    # Generate 10 products
    for i in range(10):
        name = product_names[i]
        description = product_descriptions[i]
        price = round(random.uniform(10, 200), 2)

        product = Product(name=name, description=description, price=price)
        db.session.add(product)

    db.session.commit()
    print("10 sample products added to the database.")
