from app import create_app
from app.extensions import db
from app.models import Product
import random

products = [
    {
        'name': 'Wireless Mouse',
        'description': 'High-quality and durable',
        'image': 'wireless-mouse.png'
    },
    {
        'name': 'Bluetooth Speaker',
        'description': 'Best seller product',
        'image': 'bluetooth-speaker.jpeg'
    },
    {
        'name': 'USB-C Charger',
        'description': 'Limited edition',
        'image': 'usb-c-charger.jpg'
    },
    {
        'name': 'Laptop Stand',
        'description': 'Compact and portable',
        'image': 'laptop-stand.jpg'
    },
    {
        'name': 'Noise Cancelling Headphones',
        'description': 'User-friendly design',
        'image': 'noise-cancelling-headphones.jpg'
    },
    {
        'name': 'Smartphone Case',
        'description': 'Top-rated by customers',
        'image': 'smartphone-case.png'
    },
    {
        'name': 'Gaming Keyboard',
        'description': 'Affordable and reliable',
        'image': 'gaming-keyboard.jpeg'
    },
    {
        'name': 'HDMI Cable',
        'description': 'Premium build quality',
        'image': 'hdmi-cable.jpg'
    },
    {
        'name': 'Portable SSD',
        'description': 'Perfect for daily use',
        'image': 'portable-ssd.jpeg'
    },
    {
        'name': 'Smartwatch',
        'description': 'Sleek and modern design',
        'image': 'smartwatch.jpg'
    },
]

app = create_app()

with app.app_context():
    for data in products:
        product = Product(
            name=data['name'],
            description=data['description'],
            price=round(random.uniform(10, 200), 2),
            image=data['image']
        )
        db.session.add(product)

    db.session.commit()
    print("10 sample products added to the database.")
