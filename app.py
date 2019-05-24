from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        for item in items:
            if name == item.name:
                return item
            else:
                return 'Item does not exist'

    def post(self, name):
        item = {'name': name, 'price': 12.00}
        items.append(item)

api.add_resource(Item, '/item/<string:name>')

app.run(port=5000)