Password Vault

Technologies: Python, Django, SQL

Project Overview

Password Vault is a secure credential management system that allows users to safely store, retrieve, and manage their passwords. The project emphasizes security, efficiency, and usability.

Features

Secure Storage: All passwords are stored encrypted to protect sensitive information.

User Authentication: Login system ensures only authorized users can access their vault.

Efficient Retrieval: Users can quickly search and retrieve stored credentials.

Responsive UI: Clean, intuitive interface with real-time input validation.

CRUD Operations: Users can add, update, view, and delete credentials.

Installation

Clone the repository

git clone <your-repo-link>
cd password-vault


Create a virtual environment

python -m venv venv
source venv/bit/activate  # Linux/Mac
venv\Scripts\activate     # Windows


Install dependencies

pip install -r requirements.txt


Apply migrations

python manage.py makemigrations
python manage.py migrate


Run the server

python manage.py runserver


Open your browser and visit http://127.0.0.1:8000

Usage

Sign up as a new user.

Log in to access your password vault.

Add, update, or delete credentials securely.

Use search to quickly find stored credentials.

Security Features

Passwords are encrypted before storage in the database.

Strong password validation for user accounts.

Session management to protect user data.

Future Enhancements

Two-factor authentication (2FA)

Password generator tool

Export/import credentials securely
