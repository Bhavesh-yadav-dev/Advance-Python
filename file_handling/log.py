
import json
import os

file_name = "user.json"


# Create database
def create_db():
    if not os.path.exists(file_name):
        with open(file_name, "w") as file:
            json.dump({}, file)


# Load users
def load_users():
    with open(file_name, "r") as file:
        users = json.load(file)
    return users


# Save users
def save_users(users):
    with open(file_name, "w") as file:
        json.dump(users, file, indent=4)


# Registration
def register():
    users = load_users()

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users:
        print("Username already exists")
    else:
        users[username] = password
        save_users(users)
        print("Registration successful")


# Login
def login():
    users = load_users()

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users:
        if users[username] == password:
            print(f"Login successful! Welcome, {username}")
        else:
            print("Incorrect password")
    else:
        print("Username not found")