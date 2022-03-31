## The project
### Technologies used
We used the following technologies:
- [Google App Engine](https://cloud.google.com/appengine/docs/overview)
- [Python](https://www.python.org/)
- [Firebase Authentication and Realtime Datababvse](https://firebase.google.com/)

## The app
The app is a simple address book that our team built for our Hackathon. It is a command line application that uses Google Firebase for authentication and the real time database. The app is deployed on Google App Engine. 

I've extracted all the business logic to `Helper.py` to make it easier to maintain the app. 
The program logic is in `main.py`. 

## Folder structure
- App engine configuration is located in `app.yaml` 
- The Python code is located in `main.py`
- Business logic is located in `Helper.py`
- Person model is in `Person.py`

##Team Members 
- Kareem James Lead Developer
- Kandace Francois Technical Writer
- Shavonne Tate Technical Writer / Project Manager
- Harold Garner Developer

##Goals
Design, develop and deploy a serverless address book application with a Google Firebase database service that will accept inputs, updates, and deletions.  
Track project progress via a [project plan](https://docs.google.com/spreadsheets/d/1x0Ypg61Q5odscDEIvArWdwBKpq5_x_k1cGQ3kvADorw/edit?usp=sharing) and [Trello board](https://trello.com/b/BEfpav45/contact-app).

##Future Development
A future iteration of the application will  include a Google Maps API integration that gives users the option to add the locations they use Google Maps to travel to the Contact Me application with the click of a button.
A future iteration of the application may include in app Video calling.
Screen lock or timeout when screen is idling will be added in a future version to enhance privacy and security concerns.

##Design
View full size diagram [here](https://drive.google.com/file/d/1Ut_b5qHCrG0kWtm3OCtpbC-tq-W6iJy4/view?usp=sharing).