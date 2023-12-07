
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
- I assume that the snippets provided in the sample repo are best practice enough for the project so I don't have to dive deeper into the possibilities of django and django rest framework (like mixins, generic class-based Views, hyperlinking...).
- I assume that we only want to display weather data from the external API Endpoint, so we only deal with get requests here and don't want to provide options for post, put, or delete calls
- I assume that we only want to display the weather of one place, so we don't need to alter the longitude and latitude values in the request.
- I assume that there is no Authentication Functionality and no superuser needed, and we only want to display data to any unauthenticated user who accesses the site.
- I want to display daily data instead of hourly data, and get weather codes from the endpoint. I assume it is ok to alter the OpenMeteo-Endpoint for that purpose.
- After adding django rest framework and refactoring the project to use it, I noticed that the folder structure differs slightly from the sample repo. I assume this is ok unless I stumble into issues.

## My Tasks & Explanations
1. Initialized a git repo in the root folder
2. Made the project setup:
    - I created a virtual environment called venv, activated it, and then installed django with python -m pip install Django
    - Stored the requirements in requirements.txt with pip freeze > requirements.txt
    - I got the django app running with django-admin startproject
    - I created a .gitignore file and added the venv/ folder
3. Created the api in django without rest framework
	- in weather_practice/weather_app, I created the api app:
	```
	python manage.py startapp api
	```
	- I registered the api app in settings.py INSTALLED_APPS array and included the path to api app in weather_app/urls.py
	- in the api app, I created 2 URLS for current and hourly weather, views to make the requests and modify the data, and created corresponding templates and an error template
4. refactored the api with django rest framework
	- installed djangorestframework and updated requirements.txt to reflect the current environment
	- created a model, a serializer and an APIView for WeatherData
5. Created vue frontend
	- installed cors headers and included it in the list of installed apps
	- altered the OpenMeteo Endpoint and the corresponding data model


### Todos
[x] Create basic view of the data with django
	[x] Create Views: fetch data from the external API
	[x] Create templates to display data
	[x] Configure URLs

[x] Django Rest Framework
	[x] Install & include in project setup
	[x] look up what should be refactored
	[x] Create Serializers to transform the data before sending to frontend
	[x] refactor views, use Django Rest Framework's APIView

[x] Documentation

[] Frontend
	[x] learn enough vue to implement a basic frontend
	
	[x] Install cors headers
	[x] Find out how to allow cors for specific resources only
	[x] Add cors settings, cors installed app and middleware

	[x] install vue & include in project setup
	[x] create vue app
	[] Decide what data should be displayed and how they should be modified before passing them to the frontend
	[] Modify the api endpoint: weather codes, daily weather
	display the necessary data of current weather

	[] Documentation
	

[] convert_date function
	[] check if django datetime or timezone modules should be used
	[] Implement the `convert_date` function in `utils.py` to convert any dates from api data to the format `DD-MM-YYYY` before displaying in the frontend.
	[] Dive into unit testing a bit
	[] Write suitable unit tests for the `convert_date` function. Please use the python's unittest framework.

[] Evaluate: do we want to have the option to submit our own lon and lat data and make the requests based on that? Then look at the tutorial again, fix the conditional rendering of the templates (always reset to false if anything changes), alter the api-endpoint addresses

## Setup Instructions 
1. Prerequisites
	You should have the following installed:
	- Python (we are using Python 3.12)
	- pip (package manager for python)

2. Clone the repository
```
git clone <repository path>
cd <your clone repository>

3. Create and activate a virtual environment
	Create a virtual environment and activate it.
```
python -m venv venv
venv/scripts/activate
```

4. Install the required packages from requirements.txt
```
pip install -r requirements.txt
```
5. Set up the database
	Apply the migrations. Make sure you are in the folder where the manage.py file is located, normally the first level weather_app folder:
```
cd weather_app
python manage.py migrate
```

6. Start the backend on the development server
```
python manage.py runserver
```
	The Api View will can be accessed on http://127.0.0.1:8000/api/weather

7. Go to the client folder and install the packages for the frontend
```
cd ../client/weather_client
npm install
```
8. Start the frontend client
```
npm run serve
```
	The Frontend client will can be accessed on http://127.0.0.1:8080/


### Still lacking in Setup
- Vue
- Do I need a superuser?
