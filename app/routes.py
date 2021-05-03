from app import db
from app.models.book import Book
from flask import request, Blueprint, make_response, jsonify

# hello_world_bp = Blueprint("hello_world", __name__)

# We'll use it to group routes that start with /books. "books" is the debugging name for this Blueprint.
# __name__ provides information the blueprint uses for certain aspects of routing.
# A keyword argument. This url_prefix indicates that every endpoint using this Blueprint should be treated like it starts with /books. We should use this blueprint for all of our RESTful routes that start with /books!
books_bp = Blueprint(
    "books", __name__, url_prefix="/books")

# @books_bp.route("", methods=["POST"], strict_slashes=False)
# def handle_books():


@books_bp.route("", methods=["GET", "POST"], strict_slashes=False)
def handle_books():
    if request.method == "GET":
        # This SQLAlchemy syntax tells Book to query for all() books. This method returns a list of instances of Book.
        books = Book.query.all()
        # We store the list of Book instances in the variable books
        books_response = []
        for book in books:
            books_response.append({
                "id": book.id,
                "title": book.title,
                "description": book.description
            })
        return jsonify(books_response)
# books_response contains a list of book dictionaries. To turn it into a Response object, we pass it into jsonify(). This will be our common practice when returning a list of something because the make_response function does not handle lists.
# JSONIFY EVERYTHING YOU'RE RETURNING (!!!)

    elif request.method == "POST":
        # This method "Pythonifies" the JSON HTTP request body by converting it to a Python DICT !!!
        request_body = request.get_json()
        # We create an instance of Book using data in request_body. We assign this new instance to new_book variable.
        new_book = Book(title=request_body["title"],
                        description=request_body["description"])
        # We use keyword arguments matching our model attributes...

        # db.session is the database's way of collecting changes that need to be made. Here, we are saying we want the database to add new_book.
        db.session.add(new_book)
        # Here, we are saying we want the database to save and commit the collected changes.
        db.session.commit()
        # This function instantiates a Response object. A Response object is generally what we want to return from Flask endpoint functions.
        return make_response(f"Book {new_book.title} successfully created", 201)


@books_bp.route("/<book_id>", methods=["GET"])
def handle_book(book_id):
    # This is the SQLAlchemy syntax to query for one Book resource. This method returns an instance of Book.
    book = Book.query.get(book_id)

    # We can create a dictionary literal for our HTTP response.
    return {
        "id": book.id,
        "title": book.title,
        "description": book.description
    }
    # As always, we must return a response. Flask will default to returning status 200 OK.
    # ???
