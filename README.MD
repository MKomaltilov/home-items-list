This is the application for creating your own home items list, put them into categories and rooms

#HOW TO RUN DEVELOPMENT SERVER
prerequisites:
*python 3.8+, pip*

1. in project root folder create virtualenv (https://docs.python.org/3/library/venv.html)
1. enter to this virtualenv
1. run *pip install -r requirements.txt*
1. copy *settings_template.py* from **home_items_list** as *settings.py*
1. add your SECRET_KEY in *settings.py*
1. run *python manage.py migrate*
1. run *python manage.py createsuperuser*
1. run *python manage.py runserver*