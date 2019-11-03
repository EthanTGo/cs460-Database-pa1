# cs460-Database-pa1
This is a programming assignment submission for cs460 is Boston University


Author: Ethan Timoteo and Mina Horner

This project uses Flask for the backend. It uses the psycopg2 library in order to connect with a local postGres database that can be accesed through the pgAdmin3 GUI. In order to run the app, you need to set up a virtual environment that contains psycopg2 and Flask. See the requirements.txt for more information.

We have created a web application that allows users to execute queries as well as insert and delete data. Our database includes the business, users, reviews, and checkins tables as well as a checks-in and writes table to allow users to check into businesses and to write reviews (see PA1_ER.pdf for the ER diagram). 
