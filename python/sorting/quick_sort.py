#!/usr/bin/env python3

# import merge_sort

def quick_sort(input_list):
  input_list_length = len(input_list)
  # basecase
  if (input_list_length == 2):
    if input_list[0] <= input_list[1]:
      output_list = input_list
    else:
      output_list = [input_list[1], input_list[0]]
  else:
    smaller_list = []
    larger_list = []
    pivot_list = []

    # Choose pivot
    pivot = input_list[input_list_length - 1]
    pivot_list.append(pivot)
    print("pivot: " + str(pivot))

    for i in range( input_list_length-1 ):
      if input_list[i] < pivot:
        smaller_list.append(input_list[i])
        print(str(input_list[i]) + " is smaller than pivot")
      elif input_list[i] > pivot:
        larger_list.append(input_list[i])
        print(str(input_list[i]) + " is bigger than pivot")
      elif input_list[i] == pivot:
        pivot_list.append(input_list[i])
        print(str(input_list[i]) + " is equal to pivot")

    if ( len(smaller_list) >= 2 ):
      sorted_smaller_list = quick_sort(smaller_list)
    elif ( len(smaller_list) > 0 ):
      sorted_smaller_list = smaller_list
    else:
      sorted_smaller_list = []

    if len(larger_list) >= 2:
      sorted_larger_list = quick_sort(larger_list)
    elif ( len(larger_list) > 0 ):
      sorted_larger_list = larger_list
    else:
      sorted_larger_list = []

    output_list = sorted_smaller_list + pivot_list + sorted_larger_list

  return output_list


input_list = [1, 5, 2, 14, 77, 9, 100, 787, 88]
print("Input list: " + str(input_list))

output_list = quick_sort(input_list)
print("Output list: " + str(output_list))

# output_list = merge_sort.merge_sort(input_list)
# print("Output list: " + str(output_list))



#Sudo code
# input array
# Base case is input array of 2
# rearage the input array if it's out of order and return it

# other case
# -Choose pivot
# -put each value smaller than pivot into smaller array, each value of pivot larger into larger array, and then create pivot array with then number of
# pivot values
# -if number of smaller values is 2 or greater, than recursivly sort that guy,
# -same with greater,
# -add recursively sorted smaller array, pivot array, and larger array
# -return that guy right there
