# **THE GOODY BASKET: CATALOG WEB APP - README** 

----------


## INTRODUCTION 

The Goody Basket is a web application, which provides a range of individual items that are organised into various categories. The application features a full user registration and authentication system through which users can create a profile and log into the system using either a Google+ account or Facebook account. Once logged in, the user will gain the ability to create, edit and delete their own categories and associated items. Additionally, users may upload their own chosen image to each created item as they wish, along with being able to edit and delete these as required.

The application is built using the Flask framework in conjunction with SQLAlchemy and Python, along with various external libraries, including OAuth 2.0, Google+ API and Facebook Login. 

A manually configured baseline installation of Ubuntu Linux is used to host the application. This installation has been made to be safe and secure against server attacks and malicious behaviour, along with being configured for automatic updates and hosting of a full Flask application using Apache2 and mod_wsgi.

----------

## ACCESSING THE APPLICATION

The application server has the IP address: `52.36.82.174`, and is available via SSH on port 2200.

The following URL's will provide access to the The Goody Basket:

[http://ec2-52-36-82-174.us-west-2.compute.amazonaws.com](http://ec2-52-36-82-174.us-west-2.compute.amazonaws.com)

or 

[http://52.36.82.174](http://52.36.82.174)

----------

## SERVER SOFTWARE, CONFIGURATIONS AND CHANGES MADE

A summary of the key actions, software and procedures I used during configuration of the Ubuntu Linux distribution was as follows:

1. Creation of a new user named 'grader', after initially connecting to the server via SSH as root.

2. Configured user 'grader' to have permission to sudo, through modification of the `/etc/passwd` file using `visudo`.

3. Set up sudo user password authentication only once every 30 minutes, through `sudo visudo` and appending `timestamp_timeout=30` to the Defaults parameters. 

4. Updated and upgraded all default Ubuntu packages using `sudo apt-get update` and `sudo apt-get upgrade` respectively. Also set up automatic updates through installation of the unattended-packages software.

5. Modified the timezone to UTC using `sudo dpkg-reconfigure tzdata`, followed by selecting UTC within the UI.

6. Changed the SSH port from 22 to 2200, through modification of the `/etc/ssh/sshd_config` file.

7. Generated an SSH key pair on my local machine using `ssh-keygen`, and copied the produced public key (.pub file)

8. Logged into the server as grader, using `ssh -v grader@52.36.82.174 -p 2200, and copied the key to a new file called authorized_keys within grader's .ssh/ directory on the remote server.

9. Modified the `/etc/ssh/sshd_config` to `PasswordAuthentication no`, so that only two factor authentication can be used to access the server. Also prevened root login through modification of `PermitRootLogin` to `no`. Source - [Udacity](https://www.udacity.com/course/configuring-linux-web-servers--ud299).

10. Configuration of Uncomplicated Firewall to only allow incoming connections for SSH (2200), HTTP (80) and NTP (123). Source - [Udacity](https://www.udacity.com/course/configuring-linux-web-servers--ud299).

11. Installation of Apache 2.0 using `sudo apt-get install apache2`, and mod_wsgi and python-setuptools using `sudo apt-get install python-setuptools libapache2-mod-wsgi`. Source - [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps)

12. Installation of PostgreSQL using `sudo apt-get install postgresql`, followed by creation of a PostgreSQL user called catalog with authority to create database tables. A database called thegoodybasket was then created within PostgreSQL, with access being restricted only to the catalog user, with `REVOKE ALL ON SCHEMA public FROM public;` and `GRANT ALL ON SCHEMA public TO catalog;`. Also Ensure no remote connections are authorised to PostgreSQL, at `/etc/postgresql/9.3/main/pg_hba.conf`. Source - [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-secure-postgresql-on-an-ubuntu-vps).

13. Creation of a new Linux user for PostgreSQL, called catalog.

14. Installation of Git, using `sudo apt-get install git`, and configured username and user-email using `git config --global` as required.

15. Installation of python-dev for the header files for Python extension modules, using `sudo apt-get python-dev`, followed by enabling of mod_wsgi using `sudo a2enmod wsgi`.

16. Cloned the Project 3 Github repo to the server and moved it to the `/var/www/` directory, using `git clone git@github.com:whatever folder-name`. Also edited the `.htaccess` to contain `RedirectMatch 404 /\.git`, thus making the GitHub repository inaccessible. Source - [Stack Overflow](http://stackoverflow.com/questions/651038/how-do-you-clone-a-git-repository-into-a-specific-folder)

17. Creation of a `thegoodybasket.wsgi` file to allow Apache to serve the web application, located within the /var/www/thegoodybasket directory. Source - [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps)

18. Installation of pip, using `sudo apt-get install python-pip`, followed by setting up my virtual environment, as follows (Source - [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps):
    1. `sudo pip install virtualenv` to install the virtual env package.
    2. Creation of a virtual environment, located at /var/www/thegoodybasket/venv, using `sudo virtualenv venv`
    3. Set venv permissions to chmod 777: `sudo chmod -R 777 venv`
    4. Activate the virtual environment (`source venv/bin/activate`) and install the required packages for the flask application using pip. The applications I required were: 
        * python-psycopg2
        * SQLAlchemy
        * sqlalchemy-utils
        * werkzeug==0.8.3
        * flask==0.9
        * oauth2client
        * httplib2
        * requests
    5. Enable the new virtual host through creating thegoodybasket.conf within /etc/apache2/sites-available/, and inserting a VirtualHost configuration set of code for the application, as taken from [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps)
    6. Enable the virtual host, using `sudo a2ensite thegoodybasket`. 

19. Update the existing Flask application to work with the catalog user within PostgreSQL by modification of the Python `create engine` functions to `create_engine('postgresql://catalog:catalog@localhost/thegoodybasket'). Followed by restarting Apache using `sudo service apache restart`.

20. Apply the correct file permission and ownerships to the required application directory folders, which includes all upload folders of the app (item_images and user_images), along with the site resources, including JS, Font-Awesome etc. libraries. For this I applied chmod 775 for the upload folders, with ownership given to www-data (the default linux user that apache uses). Source - [Stack Exchange(1)](http://serverfault.com/questions/125865/finding-out-what-user-apache-is-running-as) and [Stack Exchange(2)](http://superuser.com/questions/581194/setting-correct-permissions-for-uploading-files).

21. Configuration of apache application configuration file to allow connection through server host name, through addition of `ServerAlias HOSTNAME`, which worked out as `ServerAlias http://ec2-52-36-82-174.us-west-2.compute.amazonaws.com` for my application. I obtained the hostname through the use of [http://www.hcidata.info/host2ip.cgi](http://www.hcidata.info/host2ip.cgi) and the server IP. Enable the virtual host again, using `sudo a2ensite thegoodybasket` Source - [Apache](http://httpd.apache.org/docs/2.2/en/vhosts/name-based.html)

22. Correct configuration of Google Developers settings and Facebook App settings:
    1. Add the host name and IP address to the Authorised JavaScript origins on the developer console for the application.
    2. To the Google app authorised redirect URIs, add the host name + '/gconnect', '/login' and any other application required redirects for Google+.
    3. Redownload client_secrets.json if required.
    4. On the Facebook App settings, insert the hostname, including http:// prefix, into the site URL.
    5. Add the relevant Facebook redirect URI's to the authorised redirect URI field within the app. This can be accessed through the Facebook Login functionality menu within the application on the developers console. Source - [Udacity](https://discussions.udacity.com/t/oauth-provider-callback-uris/20460).

23. Implemented protection from malicious login attempts and server attacks, through installation and configuration of fail2ban to supplement UFW. This is carried out by:
    1. `sudo apt-get install fail2ban`
    2. Copy the jail.conf file to a duplicate named jail.local: `sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local`
    3. Edit the jail.local file, and update the selected parameters, in this case, ssh to port 2200 rather than ssh default.
    4. Install sendmail and setup email address within jail.local, as previously. `sudo apt-get install sendmail`.
    5. Stop fail2ban and start again, using `sudo service fail2ban stop` and `sudo service fail2ban start`. Source - [Stack Exchange](http://askubuntu.com/questions/54771/potential-ufw-and-fail2ban-conflicts).


----------

## APPLICATION STRUCTURE 

This project provides you with the following required directory and files:

```
    The_Goody_Basket/
    ├── README.md
    ├── runserver.py
    ├── venv/
    ├── thegoodybasket.wsgi
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
- `thegoodybasket.wsgi` is the .wsgi file that Apache uses to serve the web application.
- `venv/` is the virtual environment through which we run the application on the Ubuntu server.
- `database_setup.py` is the setup file for the SQLAlchemy PostgreSQL database schema.
- `runserver.py` is the startup Python file for running the application.
- `lotsofitemswithusers.py` contains a sample selection of database objects ready to pre-load into The Goody Basket application for quick setup.
- `__init__.py` creates the Flask application object, which allows other modules within the application to safely import it for use.   
- `signin.py` is the module required for setting up a full user registration and authentication system within our app, using OAuth 2.0.
- `views.py` is the module containing the applications routings, views and CRUD functionality.
- `endpoints.py` is the module that contains the applications API endpoint views, to provide functionality for JSON and XML data. 

---------


## TABLE SCHEMA 

### Tables 

- **User** - Stores the users name, email and unique user_id for each registered user of the application.

- **Category** - Stores the category name, category_id and the creater user_id of each category inserted into the database.

- **CategoryItem** - Stores the unique item id, item name, description, price, picture, category id and original creators user id. The category and user references are foreign keys of the Category and User tables respectively. 

---------

## USEFUL RESOURCES AND REFERENCES USED

1. Setting up a LAMP server (Linux, Apache, MySQL and PHP): [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu)

2. Starting web servers with Flask, virtualenv, pip: [Enigmeta](http://www.enigmeta.com/2012/08/16/starting-flask/)

3. Structuring large Flask apps: [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications)

4. Alternative LAMP server (Linux, Apache, MySQL and Python): [Udacity](http://blog.udacity.com/2015/03/step-by-step-guide-install-lamp-linux-apache-mysql-python-ubuntu.html)

5. Deploy a Flask application on a Ubuntu virtual private server: [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps)

6. Creating mod_wsgi functionality with .wsgi application files: [flask.pocoo.org](http://flask.pocoo.org/docs/0.10/deploying/mod_wsgi/)

7. Grant a new user sudo privileges: [http://askubuntu.com](http://askubuntu.com/questions/7477/how-can-i-add-a-new-user-as-sudoer-using-the-command-line)

8. Updating and upgrading packages on ubuntu: [https://help.ubuntu.com](https://help.ubuntu.com/community/AptGet/Howto#Maintenance_commands)

9. Changing/setting up timezones: [https://help.ubuntu.com](https://help.ubuntu.com/community/UbuntuTime#Using_the_Command_Line_.28terminal.29)

10. Using PostgreSQL with Flask or Django: [Kill the Yak](http://killtheyak.com/use-postgresql-with-django-flask/)

11. Setting up PostgreSQL users: [http://www.postgresql.org](http://www.postgresql.org/docs/9.1/static/app-createuser.html)

12. Securing PostgreSQL on a ubuntu vps: [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-secure-postgresql-on-an-ubuntu-vps)

13. Gracefully changing SSH port and setting up uncomplicated firewall (UFW): [Udacity](https://discussions.udacity.com/t/graceful-way-to-change-ssh-port-and-ufw/4830)

14. Apache default linux user during server operation, and how to scrutinise this: [http://serverfault.com](http://serverfault.com/questions/125865/finding-out-what-user-apache-is-running-as)

15. Installation of fail2ban on top of Uncomplicated Firewall: [Stack Exchange](http://askubuntu.com/questions/54771/potential-ufw-and-fail2ban-conflicts)

16. Oauth URI and JS origins settings for a server hosted flask app: [Udacity](https://discussions.udacity.com/t/oauth-provider-callback-uris/20460)

17. Virtual host configuration with apache: [Apache](http://httpd.apache.org/docs/2.2/en/vhosts/name-based.html)

18. Setting up the correct server permissions for an application file upload system: [Stack Exchange](http://superuser.com/questions/581194/setting-correct-permissions-for-uploading-files)

19. Online tool for obtaining host name through server IP, and vice versa: [http://www.hcidata.info/host2ip.cgi](http://www.hcidata.info/host2ip.cgi)

---------

## CREATOR 

Benjamin Fraser

Credit to Udacity for the Authentication and Authorisation process through using the Oauth API.
Built using the Twitter Bootstrap framework coupled with Flask, SQLAlchemy and SQLite. 

Hosted through the use of a configured Ubuntu Linux distribution and the HTTP server software Apache 2.0.

--------
