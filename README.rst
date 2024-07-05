    Coding exercise for Python engineering roles at `Onlife <https://on.life/>`_.

The Problem
===========

We have provided a basic project with some domain models for you to use to deliver a new piece of behaviour.

The project includes the following domain model::

    ./src/coding_exercise/domain/model/cable.py

This class has the following attributes provided as constructor arguments:

* ``length:int``

The new behaviour we are asking you to write is to create a class that will split a cable into ``n`` number of parts.

An empty implementation has been put in place in the following::

    ./src/coding_exercise/application/splitter.py

The associated tests are in::

    ./tests/coding_exercise/application/test_splitter.py

The rules are:

* lengths of the returned ``Cable`` are to be equal

  + if the length cannot be split equally the last ``Cable`` in the result should be longer

Test
====

This project uses `tox <https://tox.wiki/>`_ to automate testing. To run the tests do the following::

    tox

Development Environment
=======================

This project includes a `Vagrant <https://www.vagrantup.com/>`_ development environment for convenience.

If you decide to leverage it, you can do the following::

    colima start
    vagrant up
    vagrant ssh
    cd /vagrant

Tested Configuration
--------------------

========== =======
Technology Version
========== =======
os         ``macOS 14.5``
vagrant    ``2.4.1``
ansible    ``2.17.1``
colima     ``0.6.9``
docker     ``27.0.3``
========== =======
