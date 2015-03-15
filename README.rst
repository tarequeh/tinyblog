==============
Tiny Blog Demo
==============

What is it?
-----------

An exercise in creating a minimal blog using django as RESTful backend and
angular as frontend


How do I run it?
----------------

Run the following commands to install different components::

    virtualenv ve
    source ve/bin/activate
    pip install -r requirements.txt
    cd ui
    bower install

Initialize the DB (sqlite)::

    ./api/manage.py migrate

Create a superuser to add blog posts::

    ./api/manage.py createsuperuser

Run the server::

    ./api/manage.py runserver

Now the blog will be up and running at http://127.0.0.1:8000

To add/edit blog posts, visit the URL below and log in using admin creds::

    http://127.0.0.1:8000/admin/
