# main.py

from services import *


def menu():
    print("\n===== REST API CLIENT =====")
    print("1. Fetch all posts")
    print("2. Fetch post by ID")
    print("3. Create new post")
    print("4. Update post")
    print("5. Delete post")
    print("6. Exit")


def main():
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            posts = fetch_all_posts()
            print(posts[:5])  # show first 5

        elif choice == "2":
            post_id = int(input("Enter post ID: "))
            print(fetch_post(post_id))

        elif choice == "3":
            title = input("Enter title: ")
            body = input("Enter body: ")
            user_id = int(input("Enter user ID: "))
            print(create_new_post(title, body, user_id))

        elif choice == "4":
            post_id = int(input("Enter post ID: "))
            title = input("Enter new title: ")
            body = input("Enter new body: ")
            user_id = int(input("Enter user ID: "))
            print(update_existing_post(post_id, title, body, user_id))

        elif choice == "5":
            post_id = int(input("Enter post ID: "))
            result = delete_existing_post(post_id)
            print("Deleted successfully" if result else "Delete failed")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice, try again")


if __name__ == "__main__":
    main()