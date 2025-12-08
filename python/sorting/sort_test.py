#!/usr/bin/env python3

import random
import unittest
# import pysort

# input_list = [1, 5, 2, 14, 77, 9, 88]
# print("Input list: " + str(input_list))

# output_list = pysort.mergesort(input_list)
# print("Output list: " + str(output_list))

# output_list = pysort.quicksort(input_list)
# print("Output list: " + str(output_list))

# Old version above imported the sorting algorithms and ran them in here. New version will
# be imported into each sorting algorithm to test them in there
#
# Functionality:
# Generate arbitrarily large list of unsorted values: input array
# Create another list with the same data as the input array but sorted: sorted array
# Compare the output of the sorting algorithms with the sorted array
# 
# Also - the goal is to incorporate the unittest library into the testing but this is 
# to be done later
#
# Todo: 
# - clean up the print statements
# - Add regression functionality -> Can you make it so it generates several sets of input arrays and compares each
# of them
# - Is there a way to test how many operations/performance of the algorithms?


def gen_input_array(max_n, max_m):
    # Random length n
    n = random.randint(0,max_n)
    print(n)

    # Generate random values 
    input_array = random.choices(range(0,max_m), k=n)
    print(input_array)

    # return input_array
    return input_array

input_array = gen_input_array(50, 50)
print(input_array)

def gen_sorted_array(input_array):
    sorted_array = sorted(input_array)
    print(sorted_array)
    return sorted_array

sorted_array = gen_sorted_array(input_array)
print(type(sorted_array))

def compare_arrays(algorithm_output, sorted_array):
        # print(len(algorithm_output))    
    if len(algorithm_output) != len(sorted_array):
        print("Lengths don't match")
        print("algorithm_output length = " + str(len(algorithm_output)))
        print("sorted_array length = " + str(len(sorted_array)))
    else:
        print("Lengths match!")   
    mismatch = 0
    for i in range(0,len(algorithm_output)):
        if(algorithm_output[i] != sorted_array[i]):
            print("algorithm_output[" + str(i) + "] != sorted_array[" + str(i) + "]")
            mismatch = 1

    if (mismatch == 0):
        print("Values Match!")
    else:
        print("Values Don't Match :(")

    # dif_arrays = list(set(algorithm_output) - set(sorted_array))
    # print(dif_arrays)

compare_arrays(sorted_array, sorted_array)