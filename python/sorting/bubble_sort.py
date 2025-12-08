#!/usr/bin/env python3

import sort_test

def bubble_sort(x):
  if (len(x) < 2):
    return x

  elif (len(x) >= 2):
    for i in range (0,len(x)-1):
      for j in range (0,(len(x)-1) - i):
        if x[j] > x[j+1]:
          temp = x[j]
          x[j] = x[j+1]
          x[j+1] = temp

    return x


# Main
# # array to sort
# input_array = [1, 5, 2, 14, 77, 9, 88]
# print("Input array: " + str(input_array))


# output_array = bubble_sort(input_array)
# print("Output array: " + str(output_array))

# sort_test
input_array = sort_test.gen_input_array(8, 50)
print("Input array: " + str(input_array))

sorted_array = sort_test.gen_sorted_array(input_array)
print("Sorted input array: " + str(sorted_array))


output_array = bubble_sort(input_array)
print("Output array: " + str(output_array))


sort_test.compare_arrays(output_array, sorted_array)