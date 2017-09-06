Personal Blog
===================

[![Build Status](https://travis-ci.org/goyal-sidd/blog.svg?branch=master)](https://travis-ci.org/goyal-sidd/blog)

Django based fully functional blog.

The blog is built along the lines of Django 1.9 tutorial by Coding for Entrepreneurs [here](https://github.com/codingforentrepreneurs/try-django-19)

The live blog is hosted on Heroku [here](sid22.herokuapp.com/posts/) 
> **Note:**

> - There are 2 versions of the blog, local and production.
> - Local can be cloned and run directly on local server like any django project.
> - The development version has settings changed for working with Heroku. 

#### <i class="icon-file"></i> Running locally

 - Clone the rep.
 - Create a virtualenv with name venv, activate it and run `pip install -r requirements.txt`. If you choose other name modify the .gitignore accordingly.
 - Create local database `python manage.py migrate ` and `python manage.py makemigrations`
 - Create a superuser `python manage.py createsuperuser  
 - Run it python manage.py runserver

Contributor @goyal-sidd
