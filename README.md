# NutriCARE Application
#### NutriCARE is a mobile application that allows users to track their nutritional intake and track their health.

This project repository is a Back-End Application that is used to store and retrieve data from the database to NutriCARE Application.

Using Flask framework to build the Back-End Application for NutriCARE. 

## How to run the application
#### Create a virtual environment: 
```
virtualenv env
```

#### Enter the virtual environment: 
for linux: 
```
source env/bin/activate
```
for windows: 
```
./env/Scripts/activate
```

#### install the required packages: 
```
pip install -r requirements.txt
```

#### Copy .env.example to .env and change the values to your own:
```
cp .env.example .env
```

#### Run the application: 
```
python main.py
```