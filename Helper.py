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


# Authentication
# Login
def login(email, password):
    try:
        auth.sign_in_with_email_and_password(email, password)
        print("Successfully signed in")
    except:
        print("Invalid email, or password. Please try again")


# Signup
def sign_up():
    email = input("Enter your email: ").lower()
    password = input("Enter your password: ")
    confirm_password = input("Please confirm your password: ")
    if password == confirm_password:
        try:
            auth.create_user_with_email_and_password(email, password)
            print("Success!")
        except:
            print('Email already exists, please login with your password')

# CRUD operations
# Create
def create_contact(data):
    db.child("contacts").push(data)


# Update
def update_contact(name):
    is_contact_updated = False
    contacts = db.child("contacts").get()
    for contact in contacts.each():
        if contact.val()['first_name'].lower() == name:
            print(contact.val())
            field_to_update = input("We have found the contact, which field would you like to update?\n")
            update = input("What do you want to update this value to\n")
            db.child("contacts").child(contact.key()).update({field_to_update: update})
            print(f"You can successfully updated {name}\n")
            is_contact_updated = True


# Delete
def delete_contact(name):
    is_contact_deleted = False
    contacts = db.child("contacts").get()
    for contact in contacts.each():
        if contact.val()['first_name'].lower() == name.lower():
            db.child("contacts").child(contact.key()).remove()
            is_contact_deleted = True
            print(f"{name} has been removed from contacts")
    if not is_contact_deleted:
        print("No contact with this name found")


# Get all contacts
def get_all_contacts():
    contacts = db.child("contacts").get()
    for contact in contacts.each():
        print(contact.val())


# Get single contact
def find_contact(name):
    contacts = db.child("contacts").order_by_child("first_name").equal_to(name).get()
    for contact in contacts.each():
        print(contact.val())
