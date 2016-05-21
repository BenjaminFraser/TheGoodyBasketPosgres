from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CategoryItem, User
from flask import session as login_session

# Initialise the flask application
app = Flask(__name__)

# Connect to Database and create database session
engine = create_engine('sqlite:///thegoodybasket.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# JSON APIs to view Category and associated items information
@app.route('/category/<int:category_id>/items/JSON')
def categoryItemsJSON(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(CategoryItem).filter_by(
        category_id=category_id).all()
    return jsonify(CategoryItems=[i.serialize for i in items])


# Return specific category item data in JSON.
@app.route('/category/<int:category_id>/items/<int:item_id>/JSON')
def categoryItemJSON(category_id, item_id):
    """ return JSON formatted category item data. """
    category_item = session.query(CategoryItem).filter_by(id=category_id).one()
    return jsonify(Category_Item=category_item.serialize)

# Return all category data in JSON format.
@app.route('/category/JSON')
def categoriesJSON():
    categories = session.query(Category).all()
    return jsonify(categories=[r.serialize for r in categories])

# Return basic user info in JSON format.
@app.route('/user/JSON')
def usersJSON():
    users = session.query(User).all()
    return jsonify(categories=[r.serialize for r in users])

# Return all the categories data in XML format.
@app.route('/category/XML')
def categoriesXML():
    categories = session.query(Category).all()
    return render_template('categories.xml', categories=categories)

# Return category item data in XLM format. 
@app.route('/category/<int:category_id>/items/XML')
def categoryItemsXML(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(CategoryItem).filter_by(
        category_id=category_id).all()
    return render_template('categoryItems.xml', category=category, items=items)
