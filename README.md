## The project
### Technologies used
I've used the following technologies:
- [Google App Engine](https://cloud.google.com/appengine/docs/overview)
- [Python](https://www.python.org/)
- [Firebase Authentication and Realtime Datababvse](https://firebase.google.com/)

## The app
The app is a simple address book that our team built for our Hackathon. It is a command line application that uses Google Firebase for authentication and the real time database. The app is deployed on Google App Engine. 

I've created a Person class in `Person.py` to make it easier to maintain the app. 
The logic is in `main.py`. 

## Folder structure
- App engine configuration is located in `app.yaml` 
- The Python code is located in `main.py`
- Person model is in `Person.py`
