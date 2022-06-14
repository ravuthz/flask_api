from flask import Flask,request
from flask_restful import Api, Resource, reqparse

from models import db, BookModel
from views import BooksView, BookView
 
app = Flask(__name__)

app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

api = Api(app)

api.add_resource(BooksView, '/books')
api.add_resource(BookView,'/book/<string:name>')
 
@app.before_first_request
def create_table():
    book1 = BookModel('python flask app', '100$', 'ravuthz')
    book2 = BookModel('python flask api', '100$', 'ravuthz')
    book3 = BookModel('python flast app, api auth', '500$', 'ravuthz')

    db.session.add(book1);
    db.session.add(book2);
    db.session.add(book3);
    db.session.commit();

    db.create_all()

if __name__ == '__main__':
    app.run(host='localhost', port=5000)