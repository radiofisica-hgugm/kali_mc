Usage
=====

.. _installation:

Running from source
--------------------

To use Kali MC, first install the requirements using pip:

.. code-block:: console

   (.venv) $ pip install -r requirements.txt

.. code-block:: console

   (.venv) $ python main.py

Running the executable
----------------------

A windows executable can be found in `Releases <https://github.com/radiofisica-hgugm/kali_mc/releases>`_



To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

