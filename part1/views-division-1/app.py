from flask import Flask
from flask_restx import Api, Resource

from views.views.books import book_ns

app = Flask(__name__)
app.url_map.strict_slashes = False

api = Api(app)
api.add_namespace(book_ns)



# Вы можете протестировать свое приложение самостоятельно.
# Проверьте получаете ли вы соответсвующие коды
# в ответах на запрос по адресу
#  GET http://localhost:10001/books/  - returns [] code 200
#  POST http://localhost:10001/books/ - returns "" code 201
#  GET http://localhost:10001/books/1 - returns bid (Int), code 200

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
