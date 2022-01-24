Implementation
==============

Functions
----------------

.. py:function:: read_table(filename)

   Given a file that contains a table of integers, return the table as a multidimensional array.
   
   :param filename: The name of the file that contains the table.
   :type filename: str
   :return: The multidimensional array.
   :rtype: numpy.ndarray

.. py:function:: get_products(numbers)

   Given a list of numbers, get the products of every set of four adjacent numbers. Return the list of products.
   
   :param numbers: A list of numbers.
   :type numbers: list[str]
   :return: The list of products of every set of four adjacent numbers in the list.
   :rtype: list[str]

.. py:function:: get_row_products(table)

   Given a multidimensional array, turn each row into a list and give it to the get_products function. Add the returned list of products to a list. Return the complete list of row products.
   
   :param table: A multidimensional array.
   :type table: numpy.ndarray
   :return: The list of products from every row of the table.
   :rtype: list[str]

.. py:function:: get_col_products(table)

   Given a multidimensional array, turn each column into a list and give it to the get_products function. Add the returned list of products to a list. Return the complete list of column products.
   
   :param table: A multidimensional array.
   :type table: numpy.ndarray
   :return: The list of products from every column of the table.
   :rtype: list[str]

.. py:function:: get_diagonal_products(table)

   Given a multidimensional array, turn each diagonal (from top left to bottom right) into a list and give it to the get_products function. Add the returned list of products to a list. Return the complete list of diagonal products.
   
   :param table: A multidimensional array.
   :type table: numpy.ndarray
   :return: The list of products from every diagonal of the table.
   :rtype: list[str]

.. py:function:: antidiagonal(table,k)

  Gets the kth "antidiagonal" for the given table. Here we define the antidiagonal of a table as the band running from bottom left to top right, at a right angle to each of the diagonal bands.

   :param table: A multidimensional array.
   :type table: numpy.ndarray
   :param k:
   :type k: int
   :return: The list of products from every diagonal of the table.

.. py:function:: get_antidiagonal_products(table)

   Given a multidimensional array, turn each antidiagonal (from bottom left to top right) into a list and give it to the get_products function. Add the returned list of products to a list. Return the complete list of diagonal products.
   
   :param table: A multidimensional array.
   :type table: numpy.ndarray
   :return: The list of products from every antidiagonal of the table.
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