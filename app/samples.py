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
