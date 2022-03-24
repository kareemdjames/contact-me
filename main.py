import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyAxRQPXM4KwXTaXvG55NZD1ZiAv3kSejrw",
    "authDomain": "contact-me-dcec6.firebaseapp.com",
    "projectId": "contact-me-dcec6",
    "storageBucket": "contact-me-dcec6.appspot.com",
    "messagingSenderId": "161600233857",
    "appId": "1:161600233857:web:154f9535a9fc5ae2774880",
    "measurementId": "G-24YLTCJ9EZ",
    "databaseURL": "https://contact-me-dcec6-default-rtdb.firebaseio.com/"

}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()
# db=firebase.database()
# storage=firebase.storage()

# Authentication
# Login
email = input("Enter your email")
password = input("Enter your password")
try:
    auth.sign_in_with_email_and_password(email, password)
    print("Successfully signed in")
except:
    print("Invalid email, or password. Please try again")
