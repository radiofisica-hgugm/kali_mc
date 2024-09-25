Configuration file
====================

Some parameters can be tweaked for customization of reports and configuration of Record & Verify systems.

In order to customize Kali MC, the user has to create a text file named ``local_conf.py`` and place it in the same
folder as the program main file ``main.py`` if running from source, or inside the ``_internal`` folder if running from
the executable file. The configuration will be loaded on startup:

.. code-block:: console

   python main.py
        local_conf imported
        Starting Kali MC v.1.1.0

.. automodule:: conf
    :members:
