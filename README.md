# Coffee Social API

## Introduction 

The Corner Bistro is full stack website developed to allow the owner/admin of the site to recieve, view, edit and delete restraunt bookings. 

The site allows an Admin user to login using a pre-registered login(superuser) from there the Admin-user can create, read, update and delete(CRUD) bookings. 

This website also allows a users to create a login, make a booking at the restruant wbesite and view an edit the bookings. 

To create this website Agile principles where used. The frameworks used were bootstrap and django. 

 + This is a link to my live website [Live site](https://coffee-social-4aee33ad3a6e.herokuapp.com/)
 + This is a link to my Repo [Repo](https://github.com/Brionconroy/Coffee_social_api)

--- 

## Table of Contents 

 
 

 - ## [Introduction](#introduction) 

 
 

 - ## [Agile Methodologie](#agile-methodologie-1) 

 
 

 - ## [User Experience](#user-experience-1) 

 
 

 - ## [Features](#features-1) 

 
 

 - ## [Technologies](#technologies-1) 

     

- ## [Testing](#testing-1) 

    - ## [Bugs](#bugs-1) 

    - ## [Manual Testing](#manual-testing-1) 

    - ## [Code Validation](#code-validation-1) 

    - ## [Responsiveness Testing](#responsiveness-testing-1) 

     

 
 

- ## [Deployment](#deployment-1) 

 
 

- ## [Credits](#credits-1) 

--- 

 
 

## Agile Methodologie 

 
 

Agile principles were utilised throughout the planning and development of this project. The tecnoligy used in this project was github issues which were categorised into user storys, seperate out into tasks for various aspects of the project. The issues were then added into a project board through github issues as shown. 

 
 

<details> 

 
 

<summary>Agile</summary>  

 
 

![Agile](readme/userstorys.png) 

 
 

</details> 

 
 
 

I created a user storys template through github issues to layout each user stories containing acceptance criteria. These requirements were altered through the project as things dont always go to plan and new ideas can happen. I also used the MoSCoW method while developing this project this helped to prioritize certian feature ahead of others by using tags on the user storys into three differnt actagorys (Must Haves, Should Have, Could Have). By focusing on the Must Haves first you end up with a MVP (minimuim viable prject) qiucker. 

 
 

<details> 

 
 

<summary>User Storys</summary>  

 
 

![User Storys](readme/userstorys2.png) 

 
 

</details> 

 
 

## User Experience 

 
 

As a new visitor to the site, I would like to be able to make a booking and edit it acourdingly. i would also like to be able to login to the website so that i may find and edit my booking. As a returning customer, I want to be able to easily navigate the site and quickily find what I'm looking for. I would also like the ability to contact the Resteraunt directly through their website. 

 
 

### The User Experience Design was constructed using the five planes. 

 
 

+ Stratagy: Is this content relvent to the user and is it appropriate for the database? 

+ Scope: Are we accomplishing our goals of having a fully functioning database. 

+ Structure: How many pages should we have in our website and why? 

+ Skeleton: Does the structure of the database meet the users needs?

+ Surface: Does the site look good visully?


## Milestones

### Setup

+ This milestone covers all the inital setup with Django, Django REST Framework and cloadinary.

### Profile

+ This Milestone covers all CRUD functionality and API endpoint creation in the database for profiles.

### Posts

+ This Milestone covers all CRUD functionality and API endpoint creation in the database for user posts.

### Comments

+ This Milestone covers all CRUD functionality and API endpoint creation in the database for user Comments on posts.

### Barista

+ This Milestone covers all CRUD functionality and API endpoint creation in the database for user who register as a Barista.

### Reviews

+ This Milestone covers all CRUD functionality and API endpoint creation in the database for Reviewing a barista and leaving a star-rating.

### Contact Admin

+ This Milestone covers all functionality and API endpoint creation in the database for Contacting the administrater with any issues you may have.

### Followers

+ This Milestone covers all functionality to be able to follow other users.


## User Storys

+ This is a link to user storys and milestones [Repo](https://github.com/Brionconroy/Coffee_social_api/issues)



## DataBase Design

<details> 

 
 

<summary>Database Design</summary>  

 
 

![Database](readme/database.png) 

 
 

</details> 



 

 

## Technologies 

 
 

### Libraries, Frameworks, Tools 

 
 

* [Django 3.2.22](https://www.djangoproject.com/)

* [djangorestframework==3.14.0](https://www.django-rest-framework.org/) 

* [pillow==10.2.0](https://pillow.readthedocs.io/en/stable/) 

* [Heroku](https://www.heroku.com) 

* [ElephantSQL](https://www.elephantsql.com/) 

* [SQLite3](https://www.sqlite.org/index.html) 

* [Cloudinary 1.36.0](https://cloudinary.com/) 

* [Gunicorn 21.2.0](https://gunicorn.org/) 

* [Psycopg2 2.9.9](https://pypi.org/project/psycopg2/) 

* [GitPod](https://www.gitpod.io/) 

* [GitHub](https://github.com/) 

* [CI pep8 linter](https://pep8ci.herokuapp.com/) 



### Languages 

 

* [Python 3.9](https://www.python.org/downloads/release/python-390/) 

 
 
 

# Testing 

 
 

### Bugs 

 

### Manual Testing



### Features Testing



**Navbar**



|Test  | Expected Outcome  | Pass or Fail |
|--|--|--|
| The Corner Bistro Logo present | Yes  | Pass |
| Click Logo in navbar | Home page Redirect | Pass |
| Click Home in navbar | Home page Redirect | Pass |
| Click Menu in navbar| Bring user to menu page | Pass |
| Click Log-in | Redirect to Log-in page | Pass |
| Click Log-out | Redirect to Log-out page | Pass |
| Click Sign-up | Redirect to Sign-up page | Pass |
| If user Logged in booking appears in navbar | log-in disappears and booking appears | Pass |
| Click Booking in navbar | Redirect to Booking page | Pass |



**Booking Form**



|Test  | Expected Outcome  | Pass or Fail |
|--|--|--|
| Booking form only appear in navbar if logged in | Yes  | Pass |
| First name must be entered for the form to be submitted | Yes  | Pass |
| Last name must be entered for the form to be submitted | Yes | Pass |
| Email must be entered for the form to be submitted | Yes | Pass |
| Time field appear with start time of 12:00 | Yes | Pass |
| Date field appear with today’s date | Yes | Pass |
| Number of guest field only excepts number | Yes | Pass |
| Special Request/Requirements field must take information | Yes | Pass |
| Clicking Reserve button send booking to the database | Yes | Pass |



**Booking Details**



|Test  | Expected Outcome  | Pass or Fail |
|--|--|--|
| Booking details page will only appear after you've made a booking | Yes  | Pass |
| Booking details page will only show your booking | It shows you all the booking on the database  | Fail |
| Clicking Cancel will return you to the home page | Yes | Pass |
| Clicking Cancel will give you confirmation of your cancelation | No  | Fail |
| Clicking Update Booking will update booking | No | Fail |
| Clicking Update Booking will also return you to the home page | No | Fail |
| Clicking Update Booking will give you confirmation of updated booking | No | Fail |



**Sign-up**



|Test  | Expected Outcome  | Pass or Fail |
|--|--|--|
| Sign-up form creates an account on the database | Yes  | Pass |
| Form must have a username to create an account | Yes  | Pass |
| Form must have a password to create an account | Yes  | Pass |
| Account will only be created if password is entered twice correctly | Yes  | Pass |
| Form doesn’t have to have email but will except it if user wants | Yes  | Pass |
| The sign up button will redirect you to home page | Yes  | Pass |
| The sign up button will log you in | Yes  | Pass |



**Sign-in**



|Test  | Expected Outcome  | Pass or Fail |
|--|--|--|
| Sign-in form signs in a user if information is correct  | Yes  | Pass |
| Sign-in form dose not signs in a user if information is incorrect  | Yes  | Pass |
| Sign-in form will throw a (The username and/or password you specified are not correct.) if password is incorrect| Yes  | Pass |
| Sign-in form will throw a (The username and/or password you specified are not correct.) if username is incorrect| Yes  | Pass |
| The Remember Me if toggled remembers users information | Yes  | Pass |
| Clicking sign-in button will sign you in | Yes  | Pass |
| Clicking sign-in button will also return you to the home page if clicked | Yes  | Pass |
| Clicking Forgot Password will send you reset password email | it return a error 500 | Fail |



**Sign-out**



|Test  | Expected Outcome  | Pass or Fail |
|--|--|--|
| Sign-out will only appear in navbar if signed in | Yes  | Pass |
| Sign-out message appear on page asking you are you sure you want to sign out | Yes  | Pass |
| clicking Sign-out will redirect user to home page | Yes  | Pass |

**Footer**



|Test  | Expected Outcome  | Pass or Fail |
|--|--|--|
| Footers links all work | Yes  | Pass |
| Links bring you to each site in a diffent tab | Yes  | Pass |



### Code Validation 

 

### Python 

 
 

+ Before I deployed my App for the final time. I ran the code throught the PEP8 validator and it pass. 

 
 

<details> 

 
 

<summary>view.py</summary> 

 
 

![view.py](booking_service/static/images/readme/validation_testing/view.py_validation.png) 

 
 

</details> 

 
 

<details> 

 
 

<summary>setting.py</summary> 

 
 

![setting.py](booking_service/static/images/readme/validation_testing/setting.py_validator.png) 

 
 

</details> 

 
 

<details> 

 
 

<summary>models.py</summary> 

 
 

![models.py](booking_service/static/images/readme/validation_testing/models.py_validation.png) 

 
 

</details> 

 
 

<details> 

 
 

<summary>form.py</summary> 

 
 

![form.py](booking_service/static/images/readme/validation_testing/form.py-validation.png) 

 
 

</details> 

 
 

<details> 

 
 

<summary>corner bistro url.py</summary> 

 
 

![corner_bistro_url.py](booking_service/static/images/readme/validation_testing/corner_bistro_url.py_validation.png) 

 
 

</details> 

 
 

<details> 

 
 

<summary>booking service url.py</summary> 

 
 

![booking_service_url.py](booking_service/static/images/readme/validation_testing/booking_service_url.py_validator.png) 

 
 

</details> 

 
 

<details> 

 
 

<summary>app.py</summary> 

 
 

![app.py](booking_service/static/images/readme/validation_testing/app.py_validation.png) 

 
 

</details> 

 
 

<details> 

 
 

<summary>admin.py</summary> 

 
 

![admin.py](booking_service/static/images/readme/validation_testing/admin.py_valation.png) 

 
 

</details> 

 
 


 
 

## Deployment 

 
 

The first thing you should do when creating a new project is to deploy it as quick as you can to prevent any nasty errors that might be a pain to fix when your project is complete. For this project I used Heroku to deploy too. The framework I used in this project was Django, so the first thing you need to do is to create a Django project in you work space and install all the supporting libraries. Once evrthing is installed you should you should make a migration to the database with a small model to make sure everything works. 

 
 

Just to make a note of this the database used in the workspace (db.sqlite3) does not work when deployed to Heroku so we need a differnt database when deplying. I used ElephantSQL database as it was free and works with Heroku. 

 
 

### Installing Django and Libraries 

 
 

+ Step 1: Django and Gunicorn installation enter in the terminal: 

 
 

        pip3 install 'django<4' gunicorn 

+ Step 2: Install Supporting Libraries in the terminal: 

 
 

        pip3 install dj_database_url==0.5.0 psycopg2 

+ Step 3: Install Cloudinary Libraries in the terminal: 

 
 

        pip3 install dj3-cloudinary-storage 

        pip3 install urllib3==1.26.15 

+ Step 4: Create a requirements file in the terminal: 

 
 

        pip3 freeze --local > requirements.txt 

+ Step 5: Create a Project in the terminal: 

 
 

        django-admin startproject *Your Project name*. 

+ Step 6: Create a App in the terminal: 

 
 

        python3 manage.py startapp *App name* 

+ Step 7: Add App name to the  Installed Apps in setting.py file. 

 
 

+ Step 8: Migrate the changes enter in the terminal: 

 
 

        python3 manage.py migrate 

+ Step 9: Run the local server to make sure that everthing works, enter in the terminal: 

 
 

        python3 manage.py runserver 

+ Step 10: Add your local URL from the preview page to your setting.py file in the section thats called ALLOWED HOST. You must also Add your Heroku URL here too. 

 
 

+ Step 11: Create ElephantSQL Database, by creating/login to your account, creating a new instance, and copying the URL into Heroku (See step 13) 

 
 

+ Step 12: Create a new Heroku project by creating/login to your account and clicking (Create new app). Pick a name for your project and the region that your project is base in. Then click CREATE APP. 

 
 

+ Step 13: In the Heroku app setting click on Reveal Config Vars, add DATABASE_URL as a value with the URL from ElephantSQL as the Key. Repeat this step for SECRET_KEY, DEBUG, CLOUDINARY_URL, Port and DISABLE_COLLECTSTATIC as seen in the image below. 

 
 

    <details> 

 
 

    <summary>config var Image</summary>  

 
 

    ![config var](booking_service/static/images/readme/config-var.png) 

 
 

    </details> 

 
 

+ Step 14: IN your workspace create an env.py file to store all your sensative data, like in step 13 add your DATABASE_URL, SECRET_KEY and CLOUDINARY_URL to this file. at the top of this file add import os. 

 
 

    <details> 

 
 

    <summary>Env.py</summary>  

 
 

    ![Env.py](booking_service/static/images/readme/env.py.png) 

 
 

    </details> 

 
 

+ Step 15: Go back to setting.py file and at the top add these lines of code 

 
 

        from pathlib import Path 

        import os 

        import dj_database_url 

        if os.path.isfile('env.py'): 

            import env 

 
 

    <details> 

 
 

    <summary>Top of Setting.py</summary>  

 
 

    ![Top of Setting.py](booking_service/static/images/readme/top_of_setting.py.png) 

 
 

    </details> 

 
 

+ Step 16: In Setting.py find where it say SECRET_KEY and replace it with: 

 
 

        SECRET_KEY = os.environ.get('SECRET_KEY') 

 
 

+ Step 17: IN setting.py find the section DATABASES and comment out the section of code. 

 
 

    <details> 

 
 

    <summary>Database Comment Out</summary>  

 
 

    ![Database Comment Out](booking_service/static/images/readme/database_comment_out.png) 

 
 

    </details> 

 
 

+ Step 18: IN setting.py just below DATABASES the commented out section, add this code. 

 
 

        DATABASES = { 

            'default': dj_database_url.parse(os.environ.get("DATABASE_URL")) 

        } 

 
 

    <details> 

 
 

    <summary>Database Add</summary>  

 
 

    ![Database Add](booking_service/static/images/readme/database_add.png) 

 
 

    </details> 

 
 
 

+ Step 19: At this point it is a good idea to make a migration, so in the terminal: 

 
 

        python3 manage.py migrate 

 
 

+ Step 20: IN setting.py in the Installed Apps section add (location added is importent see image below): 

 
 

        'cloudinary_storage', 

        'cloudinary', 

 
 

    <details> 

 
 

    <summary>Cloudinary</summary>  

 
 

    ![Cloudinary](booking_service/static/images/readme/cloudinary_apps.png) 

 
 

    </details> 

 
 

+ Step 21: IN setting.py find the area called Static files and add this code.(makes Django use cloudinary for storing static files) 

 
 

        STATIC_URL = '/static/' STATICFILES_STORAGE = ('cloudinary_storage.storage.' 'StaticHashedCloudinaryStorage') STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ] STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 

 
 

        MEDIA_URL = '/media/' DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage' 

 
 

        DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' 

 
 

    <details> 

 
 

    <summary>Cloudinary Static</summary>  

 
 

    ![Cloudinary Static](booking_service/static/images/readme/cloudinary_static_media.png) 

 
 

    </details> 

 
 

+ Step 22: IN setting.py add this code just below BASE_DIR 

 
 

        TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates') 

 
 

+ Step 23: create 3 new in the base directory static templates and media 

 
 

+ Step 24: IN setting.py In the templates array add this: 

 
 

        'DIRS': [TEMPLATES_DIR], 

 
 

    <details> 

 
 

    <summary>TEMPLATES</summary>  

 
 

    ![TEMPLATES](booking_service/static/images/readme/templates_setting.png) 

 
 

    </details> 

 
 

+ Step 25: Add a Procfile to the root directory make sire the Procfile has a capital P. In the Procfile add this code: 

 
 

        web: gunicorn cornerbistro.wsgi 

 
 

+ Step 26: In your Heroku app navigate to the setting and add buildpack: heroku/python. 

 
 

+ Step 27: Link your GitHub Repo to your project. 

 
 

+ Step 28: Navigate to the deploy section and click on Automatic deployment (mian) 

 
 

+ Step 29: Well done!! 

 
## Conclusion

This project has thought me a lot about the differnt technologys used. It has also thought me a lot about time constrains and working to a deadline. The deadlines forced me to prioritize differnt parts of the project with User Storys and MoSCoW thinking. Moving on if you get stuck on something small and come back to it at a later time is a must when you have time constains. keeping everything well documented is a must, when not fully finishing feature (if you get stuck) so that when you come back to the feature you can pick up where you left off. 

## Credits 

+ Thanks to the tutors at Coding instatute and to my mentor Anthony for guiding me through my project. I would also like to thank Katie Duggan for proofreading the content.
 

+ This help me set up the time zone correctly  [Timezone](https://www.educative.io/answers/what-is-djangoutilstimezone) 

 
 

+ This helped me set up my crispyform [Crispy Forms](https://simpleisbetterthancomplex.com/tutorial/2018/08/13/how-to-use-bootstrap-4-forms-with-django.html) 

 
 

+ This helped me set up my menu format [Codesandbox](https://codesandbox.io/s/restaurant-menu-with-html-css-3bqzx?file=/index.html:527-5114) 

 
 

### Media 

 
 

Background image was taken from [pexels](https://www.pexels.com/search/bistro/) 

 
 

Favicon was generated by [favicon](https://favicon.io/favicon-generator/) 

 
 

 