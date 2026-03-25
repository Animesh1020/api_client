
from client import (
    get_all_posts,
    get_post_by_id,
    create_post,
    update_post,
    delete_post
)


def fetch_all_posts():
    data = get_all_posts()
    if data:
        return data
    else:
        print("Failed to fetch posts")
        return []


def fetch_post(post_id):
    if not isinstance(post_id, int) or post_id <= 0:
        print("Invalid ID")
        return None

    data = get_post_by_id(post_id)
    if data:
        return data
    else:
        print("Post not found")
        return None


def create_new_post(title, body, user_id):
    if not title or not body:
        print("Title and body are required")
        return None

    data = {
        "title": title,
        "body": body,
        "userId": user_id
    }

    return create_post(data)


def update_existing_post(post_id, title, body, user_id):
    if post_id <= 0:
        print("Invalid ID")
        return None

    data = {
        "title": title,
        "body": body,
        "userId": user_id
    }

    return update_post(post_id, data)


def delete_existing_post(post_id):
    if post_id <= 0:
        print("Invalid ID")
        return False

    return delete_post(post_id)