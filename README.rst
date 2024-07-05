    Coding exercise for Python engineering roles at `Onlife <https://on.life/>`_.

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
---------- -------
Technology Version
========== =======
os         ``macOS 14.5``
vagrant    ``2.4.1``
ansible    ``2.17.1``
colima     ``0.6.9``
docker     ``27.0.3``
========== =======
