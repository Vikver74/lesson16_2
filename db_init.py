import json
import datetime
from models import *

db.drop_all()
db.create_all()

with open('data/users.json', 'r') as file:
    users = json.load(file)
    with db.session.begin():

        for user in users:
            db.session.add(User(
            id = user['id'],
            first_name = user['first_name'],
            last_name = user['last_name'],
            age = user['age'],
            email = user['email'],
            role = user['role'],
            phone = user['phone']
            ))
        db.session.commit()


with open('data/orders.json', 'r') as file:
    orders = json.load(file)

    with db.session.begin():
        for order in orders:
            month_start, day_start, year_start = order['start_date'].split('/')
            month_end, day_end, year_end = order['end_date'].split('/')
            db.session.add(Order(
            id = order['id'],
            name = order['name'],
            description = order['description'],
            start_date = datetime.date(int(year_start), int(month_start), int(day_start)),
            end_date = datetime.date(int(year_end), int(month_end), int(day_end)),
            address = order['address'],
            price = order['price'],
            customer_id = order['customer_id'],
            executor_id = order['executor_id']
             ))
        db.session.commit()




with open('data/offers.json', 'r') as file:
    offers = json.load(file)

    with db.session.begin():
        for offer in offers:
            db.session.add(Offer(
            id = offer['id'],
            order_id = offer['order_id'],
            executor_id = offer['executor_id']
            ))
        db.session.commit()