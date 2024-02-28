Exercise 2.1: "Loop unrolling"

    - Implement the example of loop-unrolling in section 1.7.3 (p. 52-54) in Python. Ignore the use of pointers and use a while loop instead of for loop. The reason is that Python for loops are automatically optimized in the background. 
    - You should try to unroll at least 2 and 4 steps. See my results for 16 steps below.
    - Measure the execution time.

Exercise 2.2: "Cache blocking"

    - Implement the example in the top of section 1.7.4 (p. 55) in Python. Use while loop instead of for loop. Also, use Numba to compile your Python function for highest performance. Interpreted Python is too slow to reveal the difference in cache latency.
    - Increase the l1size parameter, measure the execution time and calculate the time per operation. At some point, when exceeding the L1 cache size (often 32 KB), the time per operation should increase.
    - Extend the code to use the cache blocking principle and verify that the time per operation goes down.
