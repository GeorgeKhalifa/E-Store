# E-Store
Readme:
Follow the following steps to run the project on your OS:
The First step is to install an IDE for the project:
-	Install any available IDE: Visual Studio Code, Sublime Text, or Atom…or PyCharm  Intelligent Python Assistance.
For VS code:  https://code.visualstudio.com/download
For Pycharm: https://www.jetbrains.com/pycharm/download/#section=windows

The Second step is to set up the IDE:
-	Anaconda Installation:
In order to install Anaconda version 4.3.0+ to be compatible with Python version 3.6+
Follow the installation documentation to download Anaconda for macOs or Windows or Linux
https://docs.anaconda.com/anaconda/install/

Note: Python installation is included while installing the Anaconda
(Anaconda is the world`s most popular Python distribution platform with over 20 million users worldwide)

-	Setup Anaconda path to the system environment:
Follow the following documentation:
 https://www.geeksforgeeks.org/how-to-setup-anaconda-path-to-environment-variable/ 

-	Setup Anaconda path to the IDE:
For VS Code follow the following documentation: https://code.visualstudio.com/docs/python/environments

For PyCharm follow the following documentation:
https://www.jetbrains.com/help/pycharm/conda-support-creating-conda-virtual-environment.html#conda-requirements

-	Create a Virtual Environment to work with conda:
1-	Open the IDE terminal
2-	Create the Virtual Environment using the following commands:
conda create –-name EnvName django  #Here we created an environment called EnvName
activate EnvName  #Now anything is installed with pip or conda when this environment is activated, will only be installed for this environment

-	Django Installation in the Virtual Environment:
1-	In the IDE terminal, after activating the Virtual Environment
2-	Using the following command to install Django:
conda install django or pip install django 


-	Libraries used in the Project:
1-	In the IDE terminal, after activating the Virtual Environment
2-	Using the following commands to install the packages and libraries used:
For Password Encryption:
       pip install bcrypt  #for more information: https://pypi.org/project/bcrypt/
       pip install django[argon2] #for more information: https://pypi.org/project/argon2/

For Imaging Library:
       pip install pillow –global-option=”build_ext”
       --global-option=”—disable-jpeg”
Finally after setting up the IDE:
-	Run the following commands in the project`s IDE terminal:
       activate EnvName 
python manage.py runserver
 

Then open the following URL:
http://127.0.0.1:8000/



For accessing Django Administration Panel:
-	Create a Super User to access the admin panel by running the following commands:
python manage.py createsuperuser
user-name #Enter the username
email-address #Enter the email address
password #Enter the password

 

-	For logging in the admin panel:
1-	Run the server on the terminal using: python manage.py runserver
2-	Open the URL http://127.0.0.1:8000/admin
3-	Log in with the super user username and password
 

4-	Now you have granted the access to the administration panel

  
