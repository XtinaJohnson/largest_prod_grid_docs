Implementation
==============

For reference, the source code is `here <https://github.com/XtinaJohnson/largest_prod_grid>`_.

The ``read_table`` function reads a text file that contains a square table of integers and converts it into a multidimensional array. The functions ``get_row_products``, ``get_col_products``, ``get_diagonal_products``, and ``get_antidiagonal_products`` send the numbers from each row, column, diagonal, and "antidiagonal" to the ``get_products`` function. (Here we define the antidiagonal of a table as the band running from bottom left to top right, at a right angle to each of the diagonal bands.) The ``get_products`` function computes the products of each set of four adjacent numbers and returns the list of products for each row, column, etc. to the calling function. The calling function collects all the products in a list and returns the list. A list of all products is sorted in ascending order, and the last (largest) product is printed.

Functions
----------------

.. py:function:: read_table(filename)

   Given a file that contains a square table of integers, returns the table as a multidimensional array. If the table isn't square (that is, the number of rows does not equal the number of columns), or if the table contains anything other than integers, the program prints an error message and exits.
   
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

   Given a multidimensional array, turns each row into a list and give it to the get_products function. Adds the returned list of products to a list. Returns the complete list of row products.
   
   :param table: A multidimensional array.
   :type table: numpy.ndarray
   :return: The list of products from every row of the table.
   :rtype: list[str]

.. py:function:: get_col_products(table)

   Given a multidimensional array, turns each column into a list and give it to the get_products function. Adds the returned list of products to a list. Returns the complete list of column products.
   
   :param table: A multidimensional array.
   :type table: numpy.ndarray
   :return: The list of products from every column of the table.
   :rtype: list[str]

.. py:function:: get_diagonal_products(table)

   Given a multidimensional array, turns each diagonal (from top left to bottom right) into a list and give it to the get_products function. Adds the returned list of products to a list. Returns the complete list of diagonal products.
   
   :param table: A multidimensional array.
   :type table: numpy.ndarray
   :return: The list of products from every diagonal of the table.
   :rtype: list[str]

.. py:function:: antidiagonal(table,k)

  Gets the kth "antidiagonal" for the given table. Here we define the antidiagonal of a table as the band running from bottom left to top right, at a right angle to each of the diagonal bands.

   :param table: A multidimensional array.
   :type table: numpy.ndarray
   :param k: The index of the antidiagonal band to be extracted (similar to that for NumPy's ``diagonal`` method).
   :type k: int
   :return: The list of products from every antidiagonal of the table.
   :rtype: list[int]

.. py:function:: get_antidiagonal_products(table)

   Given a multidimensional array, turns each antidiagonal (from bottom left to top right) into a list and give it to the get_products function. Adds the returned list of products to a list. Returns the complete list of antidiagonal products.
   
   :param table: A multidimensional array.
   :type table: numpy.ndarray
   :return: The list of products from every antidiagonal of the table.
   :rtype: list[str]
