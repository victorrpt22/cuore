# cuore
school project
Install [git](https://git-scm.com/downloads)
Install [python3](https://www.python.org/downloads/)
Install [pip](https://pip.pypa.io/en/stable/installing/)

go to easy to your workspace folder and clone the repo:
[How to clone a repo](https://help.github.com/en/articles/cloning-a-repository)

open terminal and type:
{code}
//go into proyect folder
$ cd /project-folder
// Install virtualenv:
$ pip install virtualenv
// Create a virtual enviroment and activate it:
$ virtualenv ENV
$ source ENV/bin/activate
// install django inside the virtual enviroment
(ENV)$ pip install django
// run project
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
{code}