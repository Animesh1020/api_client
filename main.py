from client import *

print(get_post_by_id(1))

new_post = {
    "title": "New Post",
    "body": "Testing",
    "userId": 1
}

print(create_post(new_post))

print(update_post(1, new_post))

print(delete_post(1))