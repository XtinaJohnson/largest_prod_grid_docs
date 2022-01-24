Implementation
==============

Functions
----------------

.. py:function:: read_table(filename)

   Given a file that contains a table of integers, return the table as a multidimensional array.
   
   :param filename: The name of the file that contains the table.
   :type filename: str
   :return: The multidimensional array.
   :rtype: reshaped_array : ndarray

.. py:function:: get_products(numbers)

   Given a list of numbers, get the products of every set of four adjacent numbers. Return the list of products.
   
   :param numbers: A list of numbers.
   :type numbers: list[str]
   :return: The list of products of every set of four adjacent numbers in the list.
   :rtype: list[str]

.. py:function:: get_row_products(table)

   Given a multidimensional array, turn each row into a list and give it to the get_products function. Add the returned list of products to a list. Return the complete list of row products.
   
   :param table: A multidimensional array.
   :type numbers: reshaped_array : ndarray
   :return: The list of products from every row of the table.
   :rtype: list[str]






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

#.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

#.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']
