import urllib.request

import pyrebase
from dotenv import load_dotenv
import os
from Person import *

load_dotenv()

API_KEY = os.getenv("API_KEY")

firebase_config = {
    "apiKey": API_KEY,
    "authDomain": "contact-me-dcec6.firebaseapp.com",
    "projectId": "contact-me-dcec6",
    "storageBucket": "contact-me-dcec6.appspot.com",
    "messagingSenderId": "161600233857",
    "appId": "1:161600233857:web:154f9535a9fc5ae2774880",
    "measurementId": "G-24YLTCJ9EZ",
    "databaseURL": "https://contact-me-dcec6-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(firebase_config)

auth = firebase.auth()
db = firebase.database()


# storage=firebase.storage()

# Authentication
# Login
# email = input("Enter your email: ")
# password = input("Enter your password: ")
# try:
#     auth.sign_in_with_email_and_password(email, password)
#     print("Successfully signed in")
# except:
#     print("Invalid email, or password. Please try again")
def login(email, password):
    try:
        auth.sign_in_with_email_and_password(email, password)
        print("Successfully signed in")
    except:
        print("Invalid email, or password. Please try again")

# # Signup
# email = input("Enter your email: ")
# password = input("Enter your password: ")
# confirm_password = input("Please confirm your password: ")
# if password == confirm_password:
#     try:
#         auth.create_user_with_email_and_password(email, password)
#         print("Success!")
#     except:
#         print('Email already exists, please login with your password')

# # Storage
# # Upload
# filename = input("Enter the name of the file you want to upload: ")
# # You can save the file to a path you specify e.g: \books\poem\cloud_filename. If the path doesn't exsist it will be created.
# cloud_filename = input("Enter the name you want the file in the cloud: ")
# storage.child(cloud_filename).put(filename)
# # Prints the url of the uploaded file
# print(storage.child(cloud_filename).get_url(None))

# # Download
# cloud_filename = input("Enter the name of the file you want to download")
# storage.child(cloud_filename).download("", "downloaded.txt")
#
# # Reading file to command line
# cloud_filename = input("Enter the name of the file you want to download")
# url = storage.child(cloud_filename).get_url(None)
# file = urllib.request.urlopen(url).read()
# print(file)

# Database
# Create
# db = root, db.child = child under root
# data = {"first_name": "Karlos", "last_name": "Tempes", "age": 21}
# db.child("contacts").push(data)
# Use custom id vs firebase generated one
# db.child("contacts").child("user_id").set(data)
def create_contact(data):
    db.child("contacts").push(data)


# # Update
# # Use this is you already know the key
# #db.child("contacts").child("user_id").update({"last_name":"James"})
#
# # Get all contacts
# contacts = db.child("contacts").get()
# # Iterate to get values from contacts including userid
# for contact in contacts.each():
#     #print(contact.val())
#     #print(contact.key())
#     if contact.val()['name'] == 'Mark':
#         db.child("contacts").child(contact.key)

# # Delete
# # If you know the id
# db.child("contacts").child("contact").remove()
# # Specific field
# db.child("contacts").child("contact").child("first_name").remove()
# # If you don't know the id
# contacts = db.child("contacts").get()
# for contact in contacts.each():
#     if contact.val()['first_name'] == 'Ben':
#         db.child("contacts").child(contact.key()).child("age").remove()

# #Read
# # Get everything
# #contacts = db.child("contacts").get()
# #Get single
# contacts = db.child("contacts").order_by_child("first_name").equal_to("Anna").get()
# for contact in contacts.each():
#     print(contact.val()["age"])
#
# contacts = db.child("contacts").order_by_child("age").start_at(20).get()
# for contact in contacts.each():
#     print(contact.val())

users_input = ""

print("Welcome to the address book program")

while users_input != "q":
    print("Available options")
    print("1 - Login")
    print("2 - Enter a contact")
    print("3 - Display contacts")
    print("4 - Find contact")
    print("q - quit program")
    users_input = input("Select option: ")

    if users_input == "1":
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        login(email, password)

    elif users_input == "2":
        print("Enter your contact's information")

        first_name = input("First name = ")
        last_name = input("Last name = ")
        age = input("Age = ")
        phone_number = input("Phone number = ")
        address = input("Address = ")

        contact = Person(first_name, last_name, age, phone_number, address)
        data = {"first_name": contact.first_name, "last_name": contact.last_name, "age": contact.age, "phone_number": contact.phone_number, "address": contact.address}
        create_contact(data)
        print("Thank you we have received your contacts information\n")
