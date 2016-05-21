# **THE GOODY BASKET: ITEM CATALOG WEB APP - README** 

----------


## INTRODUCTION 

The Goody Basket is a web application, which provides a range of individual items that are organised into various categories. The application features a full user registration and authentication system through which users can create a profile and log into the system using either a Google+ account or Facebook account. Once logged in, the user will gain the ability to create, edit and delete their own categories and associated items. Additionally, users may upload their own chosen image to each created item as they wish, along with being able to edit and delete these as required.

The application is built using the Flask framework in conjunction with SQLAlchemy and Python, along with various external libraries, including OAuth 2.0, Google+ API and Facebook Login. 

----------


## REQUIREMENTS 

This project provides you with the following required directory and files:

```
    The_Goody_Basket/
    ├── README.md
    ├── runserver.py
    ├── database_setup.py
    ├── client_secrets.json
    ├── fb_client_secrets.json
    ├── lotsofitemswithusers.py
    ├── The_Goody_Basket/
        ├── __init__.py
        ├── signin.py
        ├── views.py
        ├── endpoints.py
        ├── static/
            ├── css
            ├── images 
            ├── js 
            ├── font-awesome
            ├── item_images
            ├── user_images
        ├── templates/
            ├── PAGE TEMPLATES
```
- `Vagrantfile` contains the virtual machine configuration data to enable use of the database in PostgreSQL.
- `database_setup.py` is the setup file for the SQLAlchemy database schema.
- `runserver.py` is the startup Python file for running the application.
- `lotsofitemswithusers.py` contains a sample selection of database objects ready to pre-load into The Goody Basket application for quick setup.
- `__init__.py` creates the Flask application object, which allows other modules within the application to safely import it for use.   
- `signin.py` is the module required for setting up a full user registration and authentication system within our app, using OAuth 2.0.
- `views.py` is the module containing the applications routings, views and CRUD functionality.
- `endpoints.py` is the module that contains the applications API endpoint views, to provide functionality for JSON and XML data. 

You will need Git installed on your system to get the Virtual Machine running prior to using the database. You can download the required version of Git for your operating system using this [link](http://git-scm.com/downloads).

If you are on windows Git will provide you with a linux style terminal and shell called Git bash. If you are using a Mac system or Linux the regular terminal program will suffice. 

You will also need VirtualBox to run the Virtual Machine, where you must download the platform package relevant to your operating system. No extension pack or SDK is required with VirtualBox for the database, nor do you need to manually launch VirtualBox after installation. The link for download can be accessed [here](https://www.virtualbox.org). 

Finally, you shall need Vagrant installed to allow configuration of the virtual machine and allow file sharing between the host and VM. You can download Vagrant [here](https://www.vagrantup.com).

---------


## TABLE SCHEMA 

### Tables 

- **User** - Stores the users name, email and unique user_id for each registered user of the application.

- **Category** - Stores the category name, category_id and the creater user_id of each category inserted into the database.

- **CategoryItem** - Stores the unique item id, item name, description, price, picture, category id and original creators user id. The category and user references are foreign keys of the Category and User tables respectively. 

---------


## QUICK START 

In order to get the app up and running, follow the series of steps given below:

1 - Download The Goody Basket App directory to obtain the directory files listed above, and store these somewhere accessible so that you know the path to the application directory.

2 - You shall need Git, Vagrant and VirtualBox installed as instructed above in order to use the database.

3 - Using the terminal, navigate to the `/vagrant` directory in the downloaded fileset, and use the command `vagrant up`. If it is your first time running this it may take some time. Once it is up and running, type `vagrant ssh` in order to log in. You should now be operating within the Vagrant Virtual Machine. 

4 - Within the Vagrant VM, change directory to the tournament folder using `cd /vagrant/thegoodybasket`.

5 - You can now run the application in using Python within the VM. To setup the database initially, you must run the database_setup.py file, which uses SQLAlchemy to create the database schema. This is carried out using:
    `python database_setup.py`
in the Virtual machine command line.

6 - To run the application, you must use python to execute runserver.py, using:
    `python runserver.py`
The application can then be accessed using the url 'localhost:5000' within a web browser of your choice. 

7 - In order to create, edit or delete category data, you will be required to create an account through secure login in with either Google+ or Facebook. Upon login, your default Google+ or Facebook profile image will be used as your user image for The Goody Basket.

7 - If sample data for insertion into the application is required, it can be loaded into the database through running the lotsofitems.py file using `python lotsofitems.py` from the VM `/thegoodybasket` directory.

--------


## CREATOR 

Benjamin Fraser

Credit to Udacity for the Authentication and Authorisation process through using the Oauth API.
Built using the Twitter Bootstrap framework coupled with Flask, SQLAlchemy and SQLite. 

--------
