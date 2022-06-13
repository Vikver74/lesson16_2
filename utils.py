from models import *
from flask import jsonify
import datetime


def get_all_users():
    query = User.query.all()
    users = []
    for item in query:
        users.append(item.to_dict())
    return jsonify(users)


def get_one_user(user_id):
    try:
        return User.query.get(user_id).to_dict()
    except AttributeError:
        return "Пользователь с указанным ID не найден"


def set_one_user(user):
    with db.session.begin():
        try:
            db.session.add(User(
                first_name=user['first_name'],
                last_name=user['last_name'],
                age=user['age'],
                email=user['email'],
                role=user['role'],
                phone=user['phone']
            ))
            db.session.commit()
            return "Запись о пользователе успешно добавлена"
        except Exception:
            db.session.rollback()
            return "Запись о пользователе добавить не удалось"


def put_one_user(user_id, user_modified):
    with db.session.begin():
        try:
            user = User.query.get(user_id)
            user.first_name = user_modified['first_name']
            user.last_name = user_modified['last_name']
            user.age = user_modified['age']
            user.email = user_modified['email']
            user.role = user_modified['role']
            user.phone = user_modified['phone']

            db.session.add(user)
            db.session.commit()
            return 'Запись о пользователе успешно обновлена'
        except Exception:
            db.session.rollback()
            return "Запись о пользователе добавить не удалось"


def delete_one_user(user_id):
    with db.session.begin():
        try:
            user = User.query.get(user_id)

            db.session.delete(user)
            db.session.commit()
            return "Запись о пользователе успешно удалена"
        except Exception:
            db.session.rollback()
            return "Запись о пользователе удалить не удалось"


def get_all_orders():
    query = Order.query.all()
    orders = []
    for item in query:
        orders.append(item.to_dict())
    return jsonify(orders)


def get_one_order(order_id):
    try:
        return Order.query.get(order_id).to_dict()
    except AttributeError:
        return "Заказ с указанным ID не найден"


def set_one_order(order):
    with db.session.begin():
        try:
            year_start, month_start, day_start = order['start_date'].split('/')
            year_end, month_end, day_end = order['end_date'].split('/')

            db.session.add(Order(
                name=order['name'],
                description=order['description'],
                start_date=datetime.date(int(year_start), int(month_start), int(day_start)),
                end_date=datetime.date(int(year_end), int(month_end), int(day_end)),
                address=order['address'],
                price=order['price'],
                customer_id=order['customer_id'],
                executor_id=order['executor_id']
            ))
            db.session.commit()
            return "Запись о заказе успешно добавлена"
        except Exception:
            db.session.rollback()
            return "Запись о заказе добавить не удалось"


def put_one_order(order_id, order_modified):
    with db.session.begin():
        try:
            year_start, month_start, day_start = order_modified['start_date'].split('/')
            year_end, month_end, day_end = order_modified['end_date'].split('/')

            order = Order.query.get(order_id)

            order.name = order_modified['name']
            order.description = order_modified['description']
            order.start_date = datetime.date(int(year_start), int(month_start), int(day_start))
            order.end_date = datetime.date(int(year_end), int(month_end), int(day_end))
            order.address = order_modified['address']
            order.price = order_modified['price']
            order.customer_id = order_modified['customer_id']
            order.executor_id = order_modified['executor_id']

            db.session.add(order)
            db.session.commit()
            return 'Запись о заказе успешно обновлена'
        except Exception:
            db.session.rollback()
            return "Запись о заказе добавить не удалось"


def delete_one_order(order_id):
    with db.session.begin():
        try:
            order = Order.query.get(order_id)

            db.session.delete(order)
            db.session.commit()
            return "Запись о заказе успешно удалена"
        except Exception:
            db.session.rollback()
            return "Запись о заказе удалить не удалось"


def get_all_offers():
    query = Offer.query.all()
    offers = []
    for item in query:
        offers.append(item.to_dict())
    return jsonify(offers)


def get_one_offer(offer_id):
    try:
        return Offer.query.get(offer_id).to_dict()
    except AttributeError:
        return "Предложение с указанным ID не найдено"


def set_one_offer(offer):
    with db.session.begin():
        try:
            db.session.add(Offer(
                order_id=offer['order_id'],
                executor_id=offer['executor_id']
            ))
            db.session.commit()
            return "Запись о предложении успешно добавлена"
        except Exception:
            db.session.rollback()
            return "Запись о предложении добавить не удалось"


def put_one_offer(offer_id, offer_modified):
    with db.session.begin():
        try:
            offer = Offer.query.get(offer_id)

            offer.order_id = offer_modified['order_id']
            offer.executor_id = offer_modified['executor_id']

            db.session.add(offer)
            db.session.commit()
            return 'Запись о предложении успешно обновлена'
        except Exception:
            db.session.rollback()
            return "Запись о предложении добавить не удалось"


def delete_one_offer(offer_id):
    with db.session.begin():
        try:
            offer = Offer.query.get(offer_id)

            db.session.delete(offer)
            db.session.commit()
            return "Запись о предложении успешно удалена"
        except Exception:
            db.session.rollback()
            return "Запись о предложении удалить не удалось"
