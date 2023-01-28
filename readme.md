# Documentation
Small documentation about this project (drf-jwt-svelte).

## Routes
| | | | |
|-|-|-|-|
|Route|Method|Function|Token|
|/api/registration|POST|Sign up a new user|No|
|/api/login|POST|Sign in a user and get tokens|No|
|/api/user|GET|Fetching user detail|Yes|
|/api/logout|POST|Log out the user|Yes|

## How to run this project on your local machine
Install all python dependencies using pipenv.
```
pipenv install
```

Migrate Django models
```
python manage.py migrate
```

Run the server
```
python manage.py runserver
```
