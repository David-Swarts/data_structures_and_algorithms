#!/usr/bin/env python3

# Recursive function
def merge_sort(input_list):
    input_array_length = len(input_list)
    merged_array = [0] * input_array_length


    # Base Case
    # Only 2 values in the list
    if input_array_length == 2:
        print("length 2. input list: " + str(input_list))
        if input_list[0] <= input_list[1]:
            merged_array = input_list
        else:
            merged_array = [input_list[1],input_list[0]]
        print("length 2. output list: " + str(merged_array))

    elif input_array_length == 1:
        print("length 1. input list: " + str(input_list))
        merged_array == input_list
        print("length 1. output list: " + str(merged_array))

    elif input_array_length > 2:
        half_length = input_array_length // 2
        top_length = input_array_length - half_length
        print("Input array length: " + str(input_array_length))
        print("Half array length: " + str(half_length))

        print("Top half unsorted array: " + str(input_list[half_length:input_array_length]))
        print("Bottom half unsorted array: " + str(input_list[0:half_length]))

        top_half_sorted_array = merge_sort(input_list[half_length:input_array_length])
        bottom_half_sorted_array = merge_sort(input_list[0:half_length])

        print("Top half sorted array: " + str(top_half_sorted_array))
        print("Bottom half sorted array: " + str(bottom_half_sorted_array))

        # Merge arrays
        counter_top = 0
        counter_bottom = 0

        bottom_length = len(bottom_half_sorted_array)

        print("Initial for loop")
        print("counter_top = " + str(counter_top))
        print("counter_bottom = " + str(counter_bottom))
        print("top length = " + str(top_length))
        print("bottom length = " + str(half_length))


        for i in range(input_array_length):
            if(counter_bottom == half_length):
                merged_array[i] = top_half_sorted_array[counter_top]
                counter_top = counter_top + 1
            elif(counter_top == top_length):
                merged_array[i] = bottom_half_sorted_array[counter_bottom]
                counter_bottom = counter_bottom + 1
            else:
                if(top_half_sorted_array[counter_top] <= bottom_half_sorted_array[counter_bottom]):
                  merged_array[i] = top_half_sorted_array[counter_top]
                  counter_top = counter_top + 1
                else: 
                  merged_array[i] = bottom_half_sorted_array[counter_bottom]
                  counter_bottom = counter_bottom + 1

    # print(merged_array)
    return merged_array

# Main
# array to sort
input_array = [1, 5, 2, 14, 77, 9, 88]
print("Input array: " + str(input_array))


output_array = merge_sort(input_array)
print("Output array: " + str(output_array))