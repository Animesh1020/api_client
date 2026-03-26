# client.py

import requests
from config import BASE_URL, HEADERS


def get_all_posts():
    url = f"{BASE_URL}/posts"
    
    try:
        response = requests.get(url, headers=HEADERS)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None