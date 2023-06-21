# Installation guide

## Linux Users
1. Clone the repo
2. move to the project directory and open terminal there
3. Run `python3 -m venv venv ` to create a virtual environment
4. Run `source venv/bin/activate` to Activate the virtual environment
5. Run `pip install -r requirements.txt` to install libraries
6. Run the server by `python3 manage.py runserver 0.0.0.0:80`
7. Open the browser and visit `http://<your ip adress>`
- NB: Run `ifconfig` to check your ip address

## Windows user
1. Clone the repo
2. move to the project directory and open terminal there
3. Run `python -m venv venv ` to create a virtual environment
4. Run `venv\Script\activate.bat` to Activate the virtual environment
5. Run `pip install -r requirements.txt` to install libraries
6. Run the server by `python3 manage.py runserver 0.0.0.0:80`
7. Open the browser and visit `http://<your ip adress>`
- NB: Run `ipconfig` to check your ip address


# Usage guide

## Importing records from excel file to database

run `python manage.py import_excel <path/to/excel/file.xlsx>` to import the csv file into the database
You should see terminal updating 
```
Successfully imported row ....10 #Number of rows i the excel file
Data import completed.
```
You can confirm the recode through the admin panel

## Exporting database data into excel file

