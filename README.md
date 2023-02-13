# Web Classification to Imagenet classes
Simple classification app using Flask, Flask-Login, Login with Google, App setup as Google Client. 
The app allows logging using Google Account and classifies a picture uploaded by the user.
It uses Xception model, with preset imagenet-trained weights.

![obraz](https://user-images.githubusercontent.com/76066386/218544843-7c2c3765-55d3-4fa0-b815-69265e60b002.png)


```
clientId : "yourClientId"
clientSecret: "yourClientSecret"
``` 
 
Installation with:
 
```
pip install -r requirements.txt
```
 
Initalize the database by running app.py for the first time:
 
```
python app.py
```
 
Should see "Initialized the database."
 
Run the command again to start the Flask web server locally:
 
```
python app.py
```

## Views
The app has four views. 
### Login
The first one is used to let the user login -> from there the user will be redirected to google login page.
![obraz](https://user-images.githubusercontent.com/76066386/218545353-ff039dce-ccda-457c-9b8c-c361cf0e1952.png)

After successfully logging in the user will be sent to the index page. If the result of login is not successful the user will be redirected back to login page.

### Index/Main page
This is the page where most of the interactions take place. The user can enter a valid image (with png, jpg or jpeg extensions), when the user hits the submit button they will be redirected to verify subpage. Below the image uploading part of the page there is a button that sends the user to stats page. Lastly, the user can logout from the site.
![obraz](https://user-images.githubusercontent.com/76066386/218545740-f57ae521-ef64-4f20-becd-1666917bce0c.png)

### Verify
On this page the uploaded image along the classification obtained from Xception model will be displayed. 
![obraz](https://user-images.githubusercontent.com/76066386/218546348-78369152-e52a-4270-b10b-dd1eb5997222.png)

The user is prompted to give feedback whether the classification was or was not correct. If it was correct, the user should use the 'yes' button, otherwise, the 'no' button. After sending feedback it is saved alongside other information in the database. The entries made by user actions can be seen on stats page.

### Stats
The last page contains the effects of a query that pulls every row that has current user's id. With this the user can check their history in the app.
![obraz](https://user-images.githubusercontent.com/76066386/218547140-cdafa121-19f4-4f19-956f-937198c9f6ee.png)

From this page the user can only go back to index page.


