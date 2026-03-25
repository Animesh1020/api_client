from services import *

print(fetch_all_posts()[:2])
print(fetch_post(1))

print(create_new_post("Test", "Hello", 1))

print(update_existing_post(1, "Updated", "Body", 1))

print(delete_existing_post(1))