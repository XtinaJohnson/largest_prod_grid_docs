Implementation
==============

Functions
----------------

.. py:function:: read_table(filename)

   Given a file that contains a table of integers, return the table as a multidimensional array.
   
   :param filename: The name of the file that contains the table.
   :type filename: str
   :return: The multidimensional array
   :rtype: reshaped_array : ndarray

Below this line is template stuff

.. _installation:

Installation
------------

To use Lumache, first install it using pip:

.. code-block:: console

   (.venv) $ pip install lumache

Creating recipes
----------------

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

