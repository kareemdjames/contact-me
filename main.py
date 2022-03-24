import urllib.request

import pyrebase

firebase_config = {
    "apiKey": "AIzaSyAxRQPXM4KwXTaXvG55NZD1ZiAv3kSejrw",
    "authDomain": "contact-me-dcec6.firebaseapp.com",
    "projectId": "contact-me-dcec6",
    "storageBucket": "contact-me-dcec6.appspot.com",
    "messagingSenderId": "161600233857",
    "appId": "1:161600233857:web:154f9535a9fc5ae2774880",
    "measurementId": "G-24YLTCJ9EZ",
    "databaseURL": "https://contact-me-dcec6-default-rtdb.firebaseio.com/"

}

firebase = pyrebase.initialize_app(firebase_config)

#auth = firebase.auth()
db=firebase.database()
#storage=firebase.storage()

# Authentication
# Login
# email = input("Enter your email: ")
# password = input("Enter your password: ")
# try:
#     auth.sign_in_with_email_and_password(email, password)
#     print("Successfully signed in")
# except:
#     print("Invalid email, or password. Please try again")

## Signup
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

# # Database
# # Create
# # db = root, db.child = child under root
# data = {"first_name": "Ben", "last_name": "Jackson", "age": 42}
# db.child("contacts").push(data)
# # Use custom id vs firebase generated one
# db.child("contacts").child("user_id").set(data)

# Update
# Use this is you already know the key
#db.child("contacts").child("user_id").update({"last_name":"James"})

# Get all contacts
contacts = db.child("contacts").get()
# Iterate to get values from contacts including userid
for contact in contacts.each():
    #print(contact.val())
    #print(contact.key())
    if contact.val()['name'] == 'Mark':
        db.child("contacts").child(contact.key)



