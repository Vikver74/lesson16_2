from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy

from utils import *


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mybase.db'
app.config['JSON_AS_ASCII'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/users', methods=['GET', 'POST'])
def view_all_users():
    if request.method == 'GET':
        users = get_all_users()
        return users

    elif request.method == 'POST':
        user = request.json
        result = set_one_user(user)
        return result


@app.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def view_one_users(user_id):
    if request.method == 'GET':
        result = get_one_user(user_id)
        return result

    elif request.method == 'PUT':
        user = request.json
        result = put_one_user(user_id, user)
        return result

    elif request.method == 'DELETE':
        result = delete_one_user(user_id)
        return result


@app.route('/orders', methods=['GET', 'POST'])
def view_all_orders():
    if request.method == 'GET':
        return get_all_orders()

    elif request.method == 'POST':
        order = request.json
        result = set_one_order(order)
        return result


@app.route('/orders/<int:order_id>', methods=['GET', 'PUT', 'DELETE'])
def view_order(order_id):
    if request.method == 'GET':
        result = get_one_order(order_id)
        return result

    elif request.method == 'PUT':
        order = request.json
        result = put_one_order(order_id, order)
        return result

    elif request.method == 'DELETE':
        result = delete_one_order(order_id)
        return result


@app.route('/offers', methods=['GET', 'POST'])
def view_all_offers():
    if request.method == 'GET':
        return get_all_offers()

    elif request.method == 'POST':
        offer = request.json
        result = set_one_offer(offer)
        return result


@app.route('/offers/<int:offer_id>', methods=['GET', 'PUT', 'DELETE'])
def view_offer(offer_id):
    if request.method == 'GET':
        return get_one_offer(offer_id)

    elif request.method == 'PUT':
        offer = request.json
        result = put_one_offer(offer_id, offer)
        return result

    elif request.method == 'DELETE':
        result = delete_one_offer(offer_id)
        return result


if __name__ == "__main__":
    app.run()
