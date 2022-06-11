# NutrieCare Application
NutrieCare is a mobile application that allows users to track their nutritional intake and track their health. 

Using Flask framework to build Restful API for NutrieCare Application. 

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