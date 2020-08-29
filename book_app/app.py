from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

# display all books
# create a book
# search a book using book id

def db_connection():
    conn = None
    try:
        conn =sqlite3.connect('books.sqlite')
    except sqlite3.Error as e:
        print(e)
    return conn

@app.route('/books/create', methods = ['POST'])
def create_book():
    conn = db_connection()
    cursor = conn.cursor()
    book_name = request.form['name']
    price = request.form['price']
    cursor.execute(""" INSERT INTO book(name, price) VALUES (?, ?)""", (book_name, price))
    conn.commit()
    return "Book added succesfullly", 201

@app.route('/books', methods = ['GET'])
def book_index():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute(""" SELECT * FROM book """)
    book_sql_result = cursor.fetchall()
    books = []
    for row in book_sql_result:
        books.append(dict({"book_id":row[0], "name":row[1], "price":row[2]}))
    return jsonify(books)

@app.route('/book',methods = ['GET'])
def get_book_by_id():
    book_id = request.args.get('book_id')
    conn = db_connection()
    cursor = conn.cursor()
    query = """ SELECT * FROM book where id = ?"""
    cursor.execute(query,(book_id,))
    row = cursor.fetchone()
    if row:
        data = {"book_id":row[0], "name":row[1], "price":row[2]}
        return jsonify(data)
    else:
        return 'Not Found',404




app.run(host="0.0.0.0",debug=True)