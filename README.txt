Steps to Create a MySQL Database (data) and Connect It to Your Django Project
## **1. Install WampServer**
Download: Go to the official WampServer website: Download WampServer.
Install: Run the downloaded installer and follow the on-screen instructions.
Start WampServer: After installation, click the WampServer icon to start the services. You should see a green icon in your system tray, which means WampServer is running.
Verify: Open your web browser and go to http://localhost/ to ensure WampServer is running. If you see the WampServer homepage, you're good to go.
## **2. Create the data Database in MySQL**
WampServer includes phpMyAdmin, a web interface to manage MySQL databases. Here’s how you can create the data database.

a. Access phpMyAdmin:
Open your web browser and go to: http://localhost/phpmyadmin.
Login: The default login for phpMyAdmin is:
Username: root
Password: Leave it blank (unless you've set a password for MySQL).
b. Create the Database data:
In phpMyAdmin, go to the Databases tab.
In the Create database section:
Database Name: Enter data (this will be your database name).
Choose the Collation: You can leave it as utf8_general_ci (default).
Click Create to create the data database.
The database data is now ready to be used in your Django project.

## **##3. Configure Django to Use MySQ**
Now, let’s configure your Django project to use the data MySQL database.

a. Open settings.py:
Navigate to your Django project folder.
Open the settings.py file inside your project directory (usually located inside the project folder like myproject/settings.py).
b. Update DATABASES Settings:
Update the DATABASES setting to use MySQL instead of the default SQLite. Modify the DATABASES section in settings.py like this:

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Use MySQL as the database engine
        'NAME': 'data',                        # The name of the database you created
        'USER': 'root',                        # MySQL username (default for WampServer is 'root')
        'PASSWORD': '',                        # MySQL password (leave it blank by default in WampServer)
        'HOST': 'localhost',                   # MySQL host (WampServer runs MySQL locally)
        'PORT': '3306',                        # Default MySQL port
    }
}
c. Install MySQL Client:
To interact with MySQL, Django needs a database adapter. We recommend using mysqlclient, but if you encounter issues, you can use mysql-connector-python instead.

Install mysqlclient (Recommended):
bash
Copy code
pip install mysqlclient
If you face issues installing mysqlclient, you can use the mysql-connector-python alternative:

bash
Copy code
pip install mysql-connector-python
## **4. Run Django Migrations**
Now that Django is configured to use MySQL, you need to run the migrations to create the necessary tables in your data database.

a. Run Migrations:
Open a terminal or command prompt and navigate to your Django project directory. Then run the following command to apply the migrations:

bash
Copy code
python manage.py migrate
This will apply all the default migrations and create tables in the data database.

## **5. Start the Django Development Server**
You can now start the Django development server to test if everything is working.

a. Start the Server:
bash
Copy code
python manage.py runserver
b. Test the Project:
Open your web browser and go to http://127.0.0.1:8000. You should see your Django project running, and it's now connected to the data MySQL database.

## **6. Verify Database in phpMyAdmin (Optional)**
If you want to verify that Django is using the data database, follow these steps:

Go back to http://localhost/phpmyadmin in your browser.
In the left sidebar, you should now see the data database.
Click on the data database, and you will see all the tables that Django created (like auth_user, django_session, etc.).
## **7. (Optional) Create a Superuser for Admin Access**
If you want to access the Django admin panel, you’ll need to create a superuser account:

bash
Copy code
python manage.py createsuperuser
Follow the prompts to set up a superuser account (username, email, and password).

After the superuser is created, you can access the Django admin panel at http://127.0.0.1:8000/admin.
