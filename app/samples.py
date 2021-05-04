
# #  (THIS IS TO GET ALL BOOKS BEFORE QUERYING PARAMS FOR GETTING A SPECIFIC TITLE::: !!!)

# @books_bp.route("", methods=["GET", "POST"], strict_slashes=False)
# def handle_books():
#     if request.method == "GET":
#         # This SQLAlchemy syntax tells Book to query for all() books. This method returns a list of instances of Book.
#         books = Book.query.all()
#         # We store the list of Book instances in the variable books
#
# ...

#         return jsonify(books_response)

# books_response contains a list of book dictionaries. To turn it into a Response object, we pass it into jsonify(). This will be our common practice when returning a list of something because the make_response function does not handle lists.
# JSONIFY EVERYTHING YOU'RE RETURNING (!!!)


# #  (THIS IS TO GET A SINGLE BOOK BEFORE REFACTORING !!!)
# @books_bp.route("/<book_id>", methods=["GET")
#     def handle_book(book_id):
#         book= Book.query.get(book_id)
#         return {
#                 "id": book.id,
#                 "title": book.title,
#                 "description": book.description
#                 }


# @hello_world_bp.route("/hello-world", methods=["GET"])
# def say_hello_world():
#     my_beautiful_response_body = "Hello, World!"
#     return my_beautiful_response_body


# @hello_world_bp.route("/hello/JSON", methods=["GET"])
# def say_hello_json():
#     return {=
#         "name": "Lin Zhang",
#         "message": "Hurro!",
#         "hobbies": ["Sleeping", "Eating", "Pugging"]
#     }

# @hello_world_bp.route("/broken-endpoint-with-broken-server-code")
# def broken_endpoint():
#     response_body = {
#         "name": "Ada Lovelace",
#         "message": "Hello!",
#         "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
#     }
#     new_hobby = "Surfing"
#     # response_body["hobbies"] + new_hobby
#     response_body["hobbies"] = new_hobby
#     return response_body
