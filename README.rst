mdid3-core
==============================

Just curious how tough it would be to re-do the app so it was the tight core with all the uneccessary stuff stripped out. 

It's kind of tough, actually. 


LICENSE: BSD

Settings
------------

mdid3-core may sort-of rely on environment settings which **will not work with Apache/mod_wsgi setups**. 

But I have been mucking with it. I haven't thought much about the environment settings thing since I started the repo with pydanny's cookiecutter template. 


Getting up and running
----------------------

The steps below will get you up and running with a local development environment. We assume you have the following installed:

* pip
* virtualenv
* mySQL (since the main db used by people running mdid is mysql)

The rest of this guide is from the cookiecutter template by pydanny)

First make sure to create and activate a virtualenv_, then open a terminal at the project root and install the requirements for local development::

    $ pip install -r requirements/local.txt

.. _virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/

You can now run the ``runserver_plus`` command::

    $ python mdid3-core/manage.py runserver_plus

The base app will run but you'll need to carry out a few steps to make the sign-up and login forms work. These are currently detailed in `issue #39`_.

.. _issue #39: https://github.com/pydanny/cookiecutter-django/issues/39


**Live reloading and Sass CSS compilation**

If you'd like to take advantage of live reloading and Sass / Compass CSS compilation you can do so with the included Grunt task.

Make sure that nodejs_ is installed. Then in the project root run::

    $ npm install grunt

.. _nodejs: http://nodejs.org/download/

Now you just need::

    $ grunt serve

The base app will now run as it would with the usual ``manage.py runserver`` but with live reloading and Sass compilation enabled.

To get live reloading to work you'll probably need to install an `appropriate browser extension`_

.. _appropriate browser extension: http://feedback.livereload.com/knowledgebase/articles/86242-how-do-i-install-and-use-the-browser-extensions-

It's time to write the code!!!


