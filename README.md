# TFF API
### Installation Guide
* Clone this repository.
* The main branch is the most stable branch at any given time, ensure you're working from it.
* Verify Python is installed, type 'python' in terminal and press enter. 
(Version 3.11.5, you can downloaded it [here](https://www.python.org))
* Run 'python -m venv env' to setup the virtual environnement.
* Run 'source env/bin/activate' on Mac or 'env\scripts\activate' on Windows to activate the virtual environnement.
* Use the command 'pip install -r requirements.txt' to install the packages according to the configuration file.
* Create an .env file in your project root folder and add your variables. See .env.sample for assistance.
### Usage
* Run 'python manage.py makemigrations' and 'python manage.py migrate' to apply modifications from models or initialize the database.
* Run 'python manage.py createsuperuser' to create a superuser, it prompts for email, username and password.
* Run 'python manage.py runserver' to start the server.
* Access administration panel at http://127.0.0.1:8000/admin.
* Access API at http://127.0.0.1:8000/api.
### Headers
* x-api-key: "your apiKey"
### API Endpoints
+ Auth   
   * [/auth/register/](https://github.com/Mirodeon/TFF-API/blob/main/documentation/auth/auth_register.md)   
   * [/auth/login/](https://github.com/Mirodeon/TFF-API/blob/main/documentation/auth/auth_login.md)   
   * [/auth/refresh/](https://github.com/Mirodeon/TFF-API/blob/main/documentation/auth/auth_refresh.md) 
   * [/auth/verification/](https://github.com/Mirodeon/TFF-API/blob/main/documentation/auth/auth_verification.md) 
+ User   
   * [/user](https://github.com/Mirodeon/TFF-API/blob/main/documentation/user/user.md) 
   * [/user/info](https://github.com/Mirodeon/TFF-API/blob/main/documentation/user/user_info.md)
   * [/user/details](https://github.com/Mirodeon/TFF-API/blob/main/documentation/user/user_details.md)
   * [/user/data](https://github.com/Mirodeon/TFF-API/blob/main/documentation/user/user_data.md)
+ Clan 
   * [/clan](https://github.com/Mirodeon/TFF-API/blob/main/documentation/clan/clan.md) 
   * [/clan/user](https://github.com/Mirodeon/TFF-API/blob/main/documentation/clan/clan_user.md)
   * [/clan/cat](https://github.com/Mirodeon/TFF-API/blob/main/documentation/clan/clan_cat.md)
+ Surroundings 
   * [/surroundings](https://github.com/Mirodeon/TFF-API/blob/main/documentation/surroundings/surroundings.md)
+ Cat
   * [/cat/user/map](https://github.com/Mirodeon/TFF-API/blob/main/documentation/cat/cat_user_map.md) 
   * [/cat/user/bag](https://github.com/Mirodeon/TFF-API/blob/main/documentation/cat/cat_user_bag.md)
   * [/cat/drop](https://github.com/Mirodeon/TFF-API/blob/main/documentation/cat/cat_drop.md)
+ Interact
   * [/interact/interest](https://github.com/Mirodeon/TFF-API/blob/main/documentation/interact/clan.md) 
   * [/interact/cat](https://github.com/Mirodeon/TFF-API/blob/main/documentation/interact/clan_user.md)
   * [/interact/reset](https://github.com/Mirodeon/TFF-API/blob/main/documentation/interact/clan_cat.md)
+ HealthCheck
   * [/health](https://github.com/Mirodeon/TFF-API/blob/main/documentation/healthCheck/surroundings.md)
### Author
* [Mirodeon](https://https://github.com/Mirodeon)

