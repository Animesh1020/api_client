import requests
from config import BASE_URL, HEADERS

# GET all posts
def get_all_posts():
    url = f"{BASE_URL}/posts"
    try:
        response = requests.get(url, headers=HEADERS)
        return response.json() if response.status_code == 200 else None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# GET post by ID
def get_post_by_id(post_id):
    url = f"{BASE_URL}/posts/{post_id}"
    try:
        response = requests.get(url, headers=HEADERS)
        return response.json() if response.status_code == 200 else None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# POST (create new post)
def create_post(data):
    url = f"{BASE_URL}/posts"
    try:
        response = requests.post(url, json=data, headers=HEADERS)
        return response.json() if response.status_code == 201 else None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# PUT (update post)
def update_post(post_id, data):
    url = f"{BASE_URL}/posts/{post_id}"
    try:
        response = requests.put(url, json=data, headers=HEADERS)
        return response.json() if response.status_code == 200 else None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# DELETE post
def delete_post(post_id):
    url = f"{BASE_URL}/posts/{post_id}"
    try:
        response = requests.delete(url, headers=HEADERS)
        return True if response.status_code == 200 else False
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return False