from login import login
from database import test_connection


def start_app():
    test_connection()
    print(
        "Welcome to Password Manager CLI\n\n Menu:\n 1. Login\n 2. Register\n 3. Exit"
    )
    choice = input("Enter your choice: ")
    if choice == "1":
        login()
    elif choice == "2":
        register()
    elif choice == "3":
        exit()


if __name__ == "__main__":
    start_app()
