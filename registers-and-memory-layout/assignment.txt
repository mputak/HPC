Exercise 1.1: "Use of registers"

    - Create a vector X of N random numbers, where N is in the order of 1e6 to 1e8 (depending on the speed of your computer).
    - Create the following implementations to calculate the difference between the consecutive elements in X: (resulting in a vector Y with N-1 elements)
        1. Use a regular for loop and calculate the difference as Y(i) = X(i+1) - X(i), where X and Y are implemented as python lists.
        2. Extend the above program with intermediate variables (e.g. x_next and x_now) to store the X(i+1) value for the next iteration.
        3. Same as 1, but store X and Y as numpy arrays.
        4. Same as 2, but store X and Y as numpy arrays. 
        5. Use a diff-function to compute the result thereby exploiting vector computation (wide registers) - in Python this function is "numpy.diff". Remember to include "import numpy".
    - Measure the execution time of all implementations and explain the difference in performance.

Exercise 1.2: "Memory organization - C vs. Fortran layout"

Part A - theoretical:

    We have 6 elements stored contiguous in memory in the order: 1, 2, 3, 4, 5, 6.  In the following, we read this contiguous data into arrays in different ways.  What do the arrays look like if we read the data as:
        1. a 2x3 matrix treating data as column-major (Fortran style) as F2x3?
        2. a 3x2 matrix treating data as column-major (Fortran style) as F3x2?
        3. a 2x3 matrix treating data as row-major (C style) as C2x3?
        4. a 3x2 matrix treating data as row-major (C style) as C3x2?
    Explain the relations between the different matrices and how this may be utilized.


Part B - practical:

    - Generate a random vector X with dimension N x M and another vector Y with opposite dimensions M x N, where N >> M, e.g. N = 100.000, M = 100. 
    - Make a program with two functions: one that loops over each row and calculates the row-sum (using numpy.sum()) and one that does the same, but loops over each column.
    - Measure execution speed for each orientation for each for the two vectors.
    - Do these results match your expectation given the memory layout difference between Fortran (Matlab) and C (Python)?
        - In Python: if this was implemented with a 2D list, you will probably not see a big difference. Why not? 
    - Extra info: In Python Numpy you can specify the memory layout for an array explicitly using the keyword order=‘C’ or order=‘F’.