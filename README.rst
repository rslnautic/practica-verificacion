=========================
 Practica verificación
=========================

.. image:: https://github.com/rslnautic/practica-verificacion.svg?branch=master
    :target: https://github.com/rslnautic/practica-verificacion

Synopsis
========

Read words from a font and show it.


Installation
============

#. Clone the repo and install and create a new environmet using virtualenv_::

    source venv/bin/activate

#. Once you have created and activated the environment you have to install the dependencies::

    pip install -r requirements.txt

.. _virtualenv: https://github.com/pypa/virtualenv

Tests
=====

All the tests are into ``tests`` directory. You can run them using::

    venv/bin/nosetest

Run the tests means: lint the code using PEP8 and pass all the tests

If you want to know the coverage you can use paver too::

    venv/bin/coverage

Contributors
============

* Ramón Serrano López (`@rslnautic`_)

.. _@rslnautic: http://twitter.com/ramonsl93

License
=======

All the rights reserved (C) 2016