# yetti-assesment
Implementing authentication and testing in the Django Framework
## About the app
Only logged-in users can access the home screen and every other user will be redirected to the login screen.
- Users can register with their email, username and password
- After registration, the User gets redirected to the homepage
- On the homepage, The  user can see the logout button
- After logging out, The user gets redirected to the login page

### Technologies used
- The app's backend is implemented in Python Django.
- Authentication is handled by Django authentication
- The database used is SQLite
- The app is styled with Bootstrap
- Registration forms and Login forms are made with crispy forms
- Testing is handled with Python's unit test
## Logged in screen
![homepage](https://github.com/kipkoech88/yetti-assesment/blob/main/127.0.0.1_8000_(Nest%20Hub%20Max).png)
## Login screen
![login screen](https://github.com/kipkoech88/yetti-assesment/blob/main/127.0.0.1_8000_login_(Nest%20Hub%20Max).png)
## Register screen
![register screen](https://github.com/kipkoech88/yetti-assesment/blob/main/127.0.0.1_8000_register(Nest%20Hub%20Max).png)

## Prerequisites
- Have Python3 installed on your PC
- Have pip installed
- Know how to work with command line

## How to get started
1. Fork this repository
2. Clone this repository
3. `cd yetti-assesment`
4. `cd yetti`
5. `pip install -r requirements.txt`
6. `python manage.py migrate`
7. `python manage.py makemigrations` to apply migrations
8. `python manage.py migrate`
9. `python manage.py runserver` to run a local server
10. Open your browser on [localhost:8000](http://127.0.0.1:8000/) to access the website
11. You'll get directed to the login page, but you don't have an account, so click, register
12. After creating an account, you'll be automatically redirected to homepage
13. You can logout, and you'll be redirected to the login page
14. Login again to verify everything works correctly
15. You can access the admin's site through [localhost:8000/admin](http://127.0.0.1:8000/admin)
16. To run the test, in the terminal, run `python manage.py test`
17. **Important** : if you are using python3 on Ubuntu or any Linux distro, you might have to use `python3 `  instead of `python` for example `python3 manage.py runserver`
