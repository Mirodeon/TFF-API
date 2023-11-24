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
### API Endpoints
+ Auth   
   * [/auth/register](https://github.com/Mirodeon/TFF-API/blob/main/auth_register.md)   
   * [/auth/login](https://github.com/Mirodeon/TFF-API/blob/main/auth_login.md)   
   * [/auth/refresh](https://github.com/Mirodeon/TFF-API/blob/main/auth_refresh.md) 
+ User   
   * [/user](https://github.com/Mirodeon/TFF-API/blob/main/user.md) 
   * [/user/info](https://github.com/Mirodeon/TFF-API/blob/main/user_info.md)
   * [/user/details](https://github.com/Mirodeon/TFF-API/blob/main/user_details.md)
   * [/user/data](https://github.com/Mirodeon/TFF-API/blob/main/user_data.md)
+ Clan 
   * [/clan](https://github.com/Mirodeon/TFF-API/blob/main/clan.md) 
   * [/clan/user](https://github.com/Mirodeon/TFF-API/blob/main/clan_user.md)
   * [/clan/cat](https://github.com/Mirodeon/TFF-API/blob/main/clan_cat.md)
+ Surroundings 
   * [/surroundings](https://github.com/Mirodeon/TFF-API/blob/main/surroundings.md)
### Author
* [Mirodeon](https://https://github.com/Mirodeon)

