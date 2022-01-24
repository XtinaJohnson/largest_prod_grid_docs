# https://projecteuler.net/problem=11
# In the 20x20 grid below, four numbers along a diagonal line have been 
# marked in red. The product of these numbers is 26 x 63 x 78 x 14 = 1788696.
# What is the greatest product of four adjacent numbers in the same direction 
# (up, down, left, right, or diagonally) in the 20x20 grid?

# Note to self:
# Multidimensional arrays can be created from one-dimensional 
# arrays using the reshape function. 
# http://www.physics.nyu.edu/pine/pymanual/html/chap3/chap3_arrays.html


from numpy import array,reshape,diagonal

# Set this to True to see debugging messages
verbose = False

# Debug-sensible print function
def show(s):
    if verbose:
        print(s)
  
# Read a table of numbers from a text file. Put all the numbers into one
# list, turn the list into a 1-d array, then reshape the array into a multi-
# dimensional array based on how many rows and columns were in the text file.

def read_table(filename):
    '''
    Given a file that contains a table of numbers, return
    the table as a multidimensional array. 

    :param filename: The name of the file that contains the table. 
    :type filename: str
    :return: The multidimensional array.
    :rtype: reshaped_array : ndarray
    '''

    # Open the file and read its contents into a list of lines (strings).
    # Each line corresponds to a table row.
    f = open(filename, 'r') 
    rows = f.readlines()
    f.close()

    # Create a list to hold all the numbers in the table.
    # This list will be turned into a 1-dimensional array, then
    # reshaped into a multidimensional array.
    table_nums = [] 
    
    # Get the number of table rows.
    num_rows = len(rows)

    # To get the number of table columns, we first need to split each row
    # (now one string) into a list of strings (each string being presumably
    # a number; we'll check that later). Each string/number in the row will 
    # be called a 'col'. We'll count the cols in each row later.
    # For now, we'll say that a row has no (null) cols.
    num_cols = None 

    # For each row, strip any leading and trailing white space and
    # split the row (on the spaces) into a list of strings. For example,
    # a row that consists of the string '10 15 20 25' will become the list
    # ['10', '15', '20', '25']. Getting the length of this list will give us
    # the number of columns in each row.
    for i in range(num_rows):
        row = rows[i].strip()
        show(row)
        cols = row.split(' ') 

        # Error handling: Make sure each row has the same number of columns.
        # Use the first row as a benchmark and compare each successive 
        # row against it. If the number of columns in a row doesn't match
        # the number of columns in the first row, print an error message
        # and exit.
        if num_cols is None: # We're on the first row
            num_cols = len(cols) # Get the number of columns 
        else: # We're past the first row
            if len(cols) != num_cols: # If the number of columns is different
                print('Row %i has %i items; I expected %i.' %(i,len(cols),num_cols))
                exit(1)

        # Error handling: Check each col/string to make sure it's a number. 
        # If it is, append the number to the list of table numbers.
        # If it's not, print an error message and exit. 
        for col in cols:
            try:
                table_nums.append(int(col)) # This will only work for ints 
            except:
                print('Hmm, looks like %s is not a number.' %col)
                exit(1)
  
    # Turn the list into a 1-dimensional array.
    table_nums_1d = array(table_nums)

    # Reshape 1-dim array into a multidimensional array that has the same
    # dimensions of the original table in the file.
    table = reshape(table_nums_1d, (num_rows,num_cols))

    return(table) 


# Other functions that take rows, columns, and diagonals of the table 
# and convert them into lists of numbers send those lists here to 
# compute all the possible products of sets of four adjacent numbers.
def get_products(numbers):
    ''' Given a list of numbers, get the products of every set of four adjacent
    numbers. Return the list of products. '''

    # Create a list to hold all the products. 
    products = []

    show('We got this list: %s' %numbers)

    # Determine how many numbers are in the list sent to this function.
    length = len(numbers)
    show('There are %i numbers in the list. Getting the products.' %length)
    if length < 4:
      show('The list has fewer than 4 numbers. Discarding!')
      return(products)

    # We'll get the products of rolling groups of 4 numbers, starting with 
    # the first number in the list. (Since we'll be using Python's range, 
    # i_max is 4 instead of 3.)
    i_min = 0  
    i_max = 4 

    # Set the starting value of the product variable.
    product = 1

    # Get rolling groups of four consecutive numbers and multiply them. 
    # Once the fourth number is off the end of the list, stop.
    while i_max <= length: # Until the fourth number is off the end of the list
        show('Getting the product of numbers %i to %i' %(i_min, (i_max - 1)))
        for i in range(i_min,i_max):  # From 0 to 3, then 1 to 4, 2 to 5... 
            show('Multiplying %i * ' %numbers[i])
            product *= numbers[i] # Build the product with each number
        products.append(product) # Append the final product to the list
        show('Product is %i' %product)
        product = 1 # Reset the product var for the next set of 4
        # Shift up the min and max to get the next set of 4
        i_min += 1
        i_max += 1

    return(products)


# Given a multidimensional array, turn each row into a list and give it to
# the get_products function. Add the returned list of products to a list.
# Return the complete list of row products.

# Slicing examples:
# # View the first column of the matrix
# array_name[:,0]  # all the rows, first column (rows, cols)
# View the second row of the matrix
# array_name[1,:] # second row, all the columns
# https://chrisalbon.com/python/basics/indexing_and_slicing_numpy_arrays/

def get_row_products(table):

    # Get the number of rows and columns in the table.
    rows,cols = table.shape

    # Create a list for all the products in the row.
    row_products = []

    row_num = 0
    while row_num < rows:
        row = table[row_num,:] # Slice all the cols for the row
        # Get the products for each row from the get_products function
        # and add them to the product list.
        show('Sending row %i to get its products' %row_num)
        row_products.extend(get_products(row))
        row_num += 1
    return(row_products)
  
  

# Given a multidimensional array, turn each column into a list and
# give it to the get_products function. Add the returned list of products
# to a list. Return the complete list of column products.

def get_col_products(table):

    # Get the number of rows and columns in the table.
    rows,cols = table.shape

    # Create a list for all the products in the column.
    col_products = []

    col_num = 0
    while col_num < cols:
        col = table[:,col_num] # slice all the rows for the given column
        col_products.extend(get_products(col))
        col_num += 1
    return(col_products)


# Given a multidimensional array, get all the diagonal slices from top left 
# to bottom right. Give each list to the get_products function. Add the returned
# list of products to a list. Return the complete list of diagonal products. 

# Diagonal takes a paramater that indicates which diagonal we want.
# The 0 diagonal is the main diagonal.
# For an NxN array, need to check diagonals from -(N-1) to (N-1).


# TODO: Figure out why some lists don't have leading whitespace removed.

def get_diagonal_products(table):
    rows,_ = table.shape
    products = []
    diag_start = (1 - rows)
    diag_end = (rows - 1)
    diag = diag_start
    while diag <= diag_end:
        products.extend(get_products(table.diagonal(diag)))
        diag += 1
    return(products)

# Since there's no diagonal function in numpy that gets diagonals that go
# from bottom left to top right, I made my own below.

def antidiagonal(table, k):
    '''antidiagonal(table, k) -> fetches the kth "antidiagonal" for the given
table. Here we define the antidiagonal of a table as the band running from
bottom left to top right, at a right angle to each of the diagonal bands.'''
    n, _ = table.shape
    antidiag = []
    start_row = min(n-1, n - 1 - k)
    start_col = max(0, -k)
    num_antidiags = start_row + 1
    for i in range(num_antidiags):
        row = max(0, start_row - i)
        col = start_col + i
        if col > n - 1:
            break
        antidiag.append(table[row,col])
    return antidiag


# Given a multidimensional array, get all the diagonal slices from bottom left 
# to top right. Give each list to the get_products function. Add the returned
# list of products to a list. Return the complete list of diagonal products. 

def get_antidiagonal_products(table):
    rows,cols = table.shape
    products = []
    diag_start = (1 - rows)
    diag_end = (rows - 1)
    diag = diag_start
    while diag <= diag_end:
        products.extend(get_products(antidiagonal(table,diag)))
        diag += 1
    return(products)


if __name__ == '__main__'

    # Get the table data from the file and turn it into a multidimensional array.
    table = read_table('number_table.txt')
    show('Table from file as a multidimensional array:')
    show(table)

    # Create an empty list to extend with all the other lists as we get them
    all_products = []

    # Get the row products and add them to the all_products list.
    get_row_products(table)
    rows_products = get_row_products(table)
    all_products.extend(rows_products)

    # Get the column products and add them to the all_products list.
    cols_products = get_col_products(table)
    all_products.extend(cols_products)

    # Get the products of all the diagonals that run from the upper left to
    # the lower right and add them to the all_products list.
    diag_products = get_diagonal_products(table)
    all_products.extend(diag_products)

    # Get the products of all the diagonals that run from the upper left to
    # the lower right and add them to the all_products list.
    antidiag_products = get_antidiagonal_products(table)
    all_products.extend(antidiag_products)

    # Sort the big list and get the last (largest) one.
    all_products.sort()
    show('List of products: %s' %all_products)
    show('Length of product list: %s' %len(all_products))
    print('The largest product from the table is %i' %all_products[(len(all_products) - 1)])


