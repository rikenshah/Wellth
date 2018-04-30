# Well-thy

DDDM Project Spring 2018

### Abstract

Healthcare costs are one of the primary attributes that impact virtually everyone. The goal of our system is to analyze habits and attributes of users to produce recommendations to improve their health. These recommendations reduce health care costs and show the user how much they could save by making the suggested habit changes. There are current systems that give healthy habit suggestions and financial recommendations separately, but no current application can quantitatively define the health attributes with actual dollar value of savings. Wellthy fully integrates health and finances to help users save money while they become healthier.

### Technology stack

1. Python : We used python in the backend to build the model and other functionalities. The recommendation engine as well as the prediction model is developed in Python.

2. Pandas : We used pandas to load the data and perform different operations on the data. The slicing and other data manipulation methods of pandas were very useful in preprocessing steps.

3. Scikit learn : We used this library to make use of in-built machine learning packages in python.

4. Django : We used django to build the UI and take user input. It provided a nice MVC architecture incorporating separation of concerns as well as faster development.

5. Github : We used github to do version control and collaborate amongst each other.

### Steps to run

- Install dependencies using `pip install -r requirements.txt`.
- Run server using `python manage.py runserver` (Make sure you are in this folder only).
- Go to `127.0.0.1:8000` in your browser and the application should be running.

### Team

- [Riken Shah](https://github.com/rikenshah/)
- [Ankit Jain](https://github.com/ankit13jain)
- [James Henderson](https://github.com/Prohunt)
- [Carolyn Thompson](https://github.com/Carolyn-May)
- [Harry Aneja](https://github.com/hardik42)
