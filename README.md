Overview
This Flask application provides user registration, login, and profile management functionalities. It allows users to register with unique usernames, emails, and phone numbers, login securely, and manage their profiles by editing information or deleting their accounts.

Features
#    User registration with validation for unique usernames, emails, and phone numbers.
#    Profile management functionalities:
#    Edit profile information (username, email, phone).
#    Delete user account.

Setup
Local Setup
1.Clone Repository: Clone the repository to your local machine.
  git clone https://github.com/toshiladitya/User_Profile.git

2.Install Dependencies: Navigate to the project directory and install dependencies using pip.
  pip install -r requirements.txt

3.To perform database migrations using Flask-Migrate, follow these steps:
   1.Create an initial migration:
     " flask db init "
   2.Generate a migration script based on model changes:
     'flask db migrate -m "Initial migration"'
   3.Apply the migration to the database
     " flask db upgrade "
     
4.Run the Flask application
 " python app.py "


Usage

User Registration

1. Navigate to the registration page (/register).
2. Fill out the registration form with a unique username, email, phone number, and password.
3. Click on the "Register" button to submit the form.


User Login

1. Navigate to the login page (/login).
2. Enter your username and password.
3. Click on the "Login" button to authenticate.


Profile Management

1. Once logged in, navigate to the profile page (/profile) to view your profile information.
2. Click on the "Edit Profile" button to update your username, email, or phone number.
3. Click on the "Delete Account" button to delete your account permanently.
