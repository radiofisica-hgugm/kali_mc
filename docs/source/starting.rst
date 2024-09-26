Starting Kali MC
=====================

.. _installation:

Running from source
--------------------

To use Kali MC, first ensure you have a Python 3 distribution installed in your system and/or activate a virtual
environment, you can check it in a terminal:

.. code-block:: console

    $ python --version
    Python 3.9.19

Clone the repository (or download zip and extract folder) `https://github.com/radiofisica-hgugm/kali_mc.git <https://github.com/radiofisica-hgugm/kali_mc.git>`_

.. code-block:: console

   $ git clone https://github.com/radiofisica-hgugm/kali_mc.git

Install the needed packages using pip:

.. code-block:: console

   $ pip install -r requirements.txt

Start the application:

.. code-block:: console

   $ python main.py

Running the executable
----------------------

A windows package with an executable file can be found in `Releases <https://github.com/radiofisica-hgugm/kali_mc/releases>`_.

Extract to the desired folder and run the executable file ``kali_mc.exe``.

.. warning::

   Do not run from a network drive, the current release suffers from a bug in the `PySide2 package <https://bugreports.qt.io/browse/PYSIDE-1460>`_.
