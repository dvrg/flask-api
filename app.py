from http import HTTPStatus
from flask import Flask, jsonify, request

api = Flask(__name__)

my_items = [
    {
        "id": 1,
        "name": "Basic T-Shirt",
        "price": 35000
    },
    {
        "id": 2,
        "name": "Long T-Shirt",
        "price": 45000
    },
]

my_tuple = {'a', 'b', 'c'}
my_list = ['a', 'b', 'c', 'd']
# my_list[1:2] == 'b'

prefix = "items"

@api.route('/login', methods=["GET", "POST"])
def index2():
    return 'a'

@api.get('/')
def index():
    return {"hello": "david!"}

@api.get(f'/{prefix}')
def get_items():
    return jsonify(my_items), HTTPStatus.OK
    
@api.get(f'/{prefix}/<int:item_id>')
def get_item(item_id):
    check_item = [item for item in my_items if item.get("id") == item_id]
    if check_item:
        return jsonify({"message": "data found", "item": (lambda x: x)(*check_item)}), HTTPStatus.OK
    else:
        return jsonify({"item_id": item_id, "message": "data not found!"}), HTTPStatus.NOT_FOUND

    # item = {}
    # for item in my_items:
    #     if item.get("id") == item_id:
    #         return item

@api.post(f'/{prefix}')
def post_item():
    data = request.get_json()
    my_list.append(data)
    return jsonify({"message": "data successful created", "item": data}), HTTPStatus.CREATED