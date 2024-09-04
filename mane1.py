import json
from datetime import datetime
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Product

# Данные для подключения к БД
DSN = 'postgresql://ЛОГИН:ПАРОЛЬ@localhost:5432/БД'
engine = sqlalchemy.create_engine(DSN)

# Создание таблиц
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Заполнение таблицы данными
product1 = Product(name="Laptop", created_at=datetime.now(), price=1000.50, quantity=10)
product2 = Product(name="Smartphone", created_at=datetime.now(), price=500.75, quantity=20)
product3 = Product(name="Tablet", created_at=datetime.now(), price=300.00, quantity=15)
product4 = Product(name="Headphones", created_at=datetime.now(), price=200.00, quantity=30)
product5 = Product(name="Bananas", created_at=datetime.now(), price=1.25, quantity=50)

session.add_all([product1, product2, product3, product4, product5])
session.commit()

# Чтение данных из таблицы
products = session.query(Product).all()

# Преобразование данных в словари для сохранения в JSON
data = []
for product in products:
    data.append({
        "id": product.id,
        "name": product.name,
        "created_at": product.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        "price": float(product.price),
        "quantity": product.quantity
    })

# Сохранение данных в JSON файл
with open('products_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print("Данные успешно сохранены в файл products_data.json")

session.close()

#Бонусное задание

import ftplib

# Данные для подключения к FTP серверу
ftp_config = {
    'host': 'ftp.ваш сервер.com',
    'user': 'ваш логин',
    'passwd': 'ваш пароль'
}

# Загрузка файла на FTP сервер
with ftplib.FTP(**ftp_config) as ftp, open('products_data.json', 'rb') as file:
    ftp.storbinary('STOR products_data.json', file)

print("Файл успешно загружен на FTP сервер")
