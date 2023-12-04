
# Weather Information

This is a partial implementation of a web app that should display weather information from a weather api. The backend of the app is powered by Django while the frontend is powered by Vue Js.

This implementation comes from a template. You, the Software Engineer, have been requested to refactor this project.

You have the freedom to choose how to display the data points and also which data points to display from the weather api.

You may make any technical decisions you would like, but must not change the overall structure of the package.

Please treat this code as an element of a larger production system. The code is being refactored to ensure reliability and testability.

Tasks requested:

- Finish implementing the code for the app.
- Display the weather information in the frontend. The design and "feel" is entirely up to you.
- Implement the `convert_date` function in `utils.py` to convert any dates from api data to the format `DD-MM-YYYY` before displaying in the frontend.
- Write suitable unit tests for the `convert_date` function. Please use the python's unittest framework.
- Document the necessary steps/setup to run the application under the "Setup Instructions" header at the end of this file.

If you do not have enough information, make any assumptions you would like and note them down with comments in the section below. Feel free to make comments that highlight completion of the tasks listed above.

Please budget 3 hours to complete, and your code should be production ready, clean and tested! Please ensure the code is version controlled also, and make sure to make several commits with sensile commit messages while working on this. When submitting please either:
- Provide a Github/GitLab/etc. link that we can view and clone your work

## My Assumptions

## My Tasks & Explanations
1. Initialized a git repo in the root folder
2. Made the project setup:
    - I created a virtual environment called venv, activated it, and then installed django with python -m pip install Django
    - Stored the requirements in requirements.txt with pip freeze > requirements.txt
    - I got the django app running with django-admin startproject
    - I created a .gitignore file and added the venv/ folder

### Todos
- Create basic view of the data with django
	- Create Views: fetch data from the external API
	- Create templates to display data
	- Configure URLs

- Django Rest Framework
	- Install & include in project setup
	- refactor views, use Django Rest Framework's APIView
	- Create Serializers to transform the data before sending to frontend

- convert_date function
	- Implement the `convert_date` function in `utils.py` to convert any dates from api data to the format `DD-MM-YYYY` before displaying in the frontend.
	- Write suitable unit tests for the `convert_date` function. Please use the python's unittest framework.

- Vue Frontend
	- install vue & include in project setup
	- create better look and feel

## Setup Instructions 
1. Create and activate a virtual environment
After cloning the project into your root folder for the project, open a terminal in this root folder create a virtual environment and activate it.
```
python -m venv .\venv
venv/scripts/activate
```

2. Install the required packages from requirements.txt:
```
pip install -r requirements.txt
```

3. Start the project on the development server:
```
python manage.py runserver
```
  
### Still lacking in Setup
- Django Rest Framework
- Vue