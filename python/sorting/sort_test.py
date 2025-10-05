#!/usr/bin/env python3

import pysort

input_list = [1, 5, 2, 14, 77, 9, 88]
print("Input list: " + str(input_list))

output_list = pysort.mergesort(input_list)
print("Output list: " + str(output_list))

output_list = pysort.quicksort(input_list)
print("Output list: " + str(output_list))