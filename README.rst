    Coding exercise for Python engineering roles at `Onlife <https://on.life/>`_.

The Process
===========

You will want to ``fork`` or ``clone`` this repository so you can work on the problem, and share the solution.

You can share the solution by either:

* adding the `@svo <https://github.com/svo>`_ ``GitHub`` user as a collaborator to your copy in ``GitHub``
* archiving your local repository and emailing it back to the talent team

The Problem
===========

We have provided a basic project with some domain models for you to use to deliver a new piece of behaviour.

The project includes the following domain model::

    ./src/coding_exercise/domain/model/cable.py

This class has the following attributes provided as constructor arguments:

* ``length:int``
* ``name:str``

The new behaviour we are asking you to write is to complete a ``class`` that will split a cable ``n`` times into equal integer lengths, i.e. if you have::

    given_cable = Cable(10, "coconuts")
    result = Splitter().split(given_cable, 1))

The ``result`` will be an array with two ``Cable`` with a length of ``5``.

Any remainder will also be split into ``Cable``, with their lengths being the same as the existing splits while possible e.g. if we have a cable with a length of 5 and split it twice we get:

* ``3`` new ``Cable`` of length ``1``
* the remaining length of ``2`` is to be split into two ``Cable`` of length ``1``

  + if the initial splits were of length ``3`` and the remainder was ``4``, the remainder would be split into a ``3`` length and ``1`` length ``Cable``

The following are the minimum/maximum values for ``length`` and ``times`` (all inclusive i.e. these values are allowed):

* times:

  + minimum: ``1``
  + maximum: ``64``

* length:

  + minimum: ``2``
  + maximum: ``1024``

Any request that does not adhere to the constraints is to to raise a ``ValueError``, as is any request that cannot be enacted e.g. a request to split a ``Cable`` a number of times that would result in less than ``1`` for the lengths.

Additionally, the first ``Cable`` will have a ``name`` of ``"coconuts-0"``, the second a ``name`` of ``"coconuts-1"``.

The number in the name should be right-justified and zero-filled e.g. if the ``result`` ``list`` has a length of ``> 9`` and ``< 100``, then the ``name`` would take the form::

    "coconuts-00"
    "coconuts-01"
    ...

An empty implementation has been put in place in the following::

    ./src/coding_exercise/application/splitter.py

The associated tests are in::

    ./tests/coding_exercise/application/test_splitter.py

Test
====

This project uses `tox <https://tox.wiki/>`_ to automate testing. To run the tests do the following::

    tox

Development Environment
=======================

This project includes a `Vagrant <https://www.vagrantup.com/>`_ development environment for convenience.

If you decide to leverage it, you can do the following::

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
