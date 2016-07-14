=========================
 Practica verificación
=========================

Synopsis
========
* Ramón Serrano López (`@ramonsl93`_)
Print and save in Database N number of tweets


Installation
============

#. Clone the repo and install and create a new environmet using `virtualenv`_ ::

    1 - pip install virtualenv
    2 - virtualenv venv
    3 - source venv/bin/activate

#. Once you have created and activated the environment you have to install the dependencies::

    pip install -r requirements.txt

.. _virtualenv: https://github.com/pypa/virtualenv

Tests
=====

All the tests are into ``tests`` directory. You can run them using::

    venv/bin/nosetests 

Run the tests means: lint the code using PEP8 and pass all the tests::

    venv/bin/pylint src


If you want to know the coverage use::

    venv/bin/nosetests --with-coverage

BDD/Funcional Test::

    lettuce tests

Contributors
============

* Ramón Serrano López (`@ramonsl93`_)

.. _@ramonsl93: http://twitter.com/ramonsl93

License
=======

All the rights reserved (C) 2016
