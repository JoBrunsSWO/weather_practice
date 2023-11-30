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

- Document the necessary steps/setup to run the application under the "Setup Instructions" header at the end of this file.
- Display the weather information in the frontend. The design and "feel" is entirely up to you.
- Finish implementing the code for the app.
- Implement the `convert_date` function in `utils.py` to convert any dates from api data to the format `DD-MM-YYYY` before displaying in the frontend.
- Write suitable unit tests for the `convert_date` function. Please use the python's unittest framework.



## My Tasks & Explanations
1. Initialized a git repo in the root folder
2. Made the project setup:
- I created a virtual environment called venv, activated it, and then installed the packages django, djangorestframework  With pip freeze > requirements.txt
- I got the django app running with django-admin startproject
@Todo: do we need gitignore for requirements.txt and venv?
@Todo How to install vue? Should be possible to just install vue packages with npm install ..., then it should save everything in a tsconfig file? so it's reproducible by npm install
@Todo Get the app running with startproject?

Todos:
- Create Views: Create Django views that will handle the logic to fetch data from the external API. You can use Django Rest Framework's APIView or ViewSet for this purpose.

- Create Serializers: If you need to transform the data before sending it to the frontend, create serializers using Django Rest Framework.

- Configure URLs: Connect your views to URLs in your Django project's urls.py file.

- Configure Vue Frontend: Make sure your Vue frontend is set up to make requests to your Django backend. You might need to configure CORS (Cross-Origin Resource Sharing) if your frontend is on a different domain.

- Testing: Test your views and API endpoints to ensure that data is being fetched and sent to the frontend correctly.

## Setup Instructions

1. First, recreate the virtual environment. Go to terminal to root folder and type the following command:
python3 -m venv .\venv
This will create a virtual environment called venv in the folder 
2. Activate the virtual environment with the following command:
venv\scripts\activate
3. Install the required packages from requirements.txt:
pip install -r requirements.txt
@Todo research what this does
4. (Should be possible to just install vue packages with npm install ..., then it should save everything in a tsconfig file? so it's reproducible by npm install)
