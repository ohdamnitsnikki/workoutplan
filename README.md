# Workoutplan

Workoutplan is a platform for people in all ages that needs help to get into training. The exercises are few, which gives anyone time to take on this challenge. 

## How does it work?

* The user get asked about their age and gets to fill it in.
* Depending on the users age a training program if shown with exercises and how many times the user should do them.
* The user then gets asked if the workout was easy.
* Incase the workout was easy it will be increased by 10% for the next day and if it wasn't it will stay the same

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!