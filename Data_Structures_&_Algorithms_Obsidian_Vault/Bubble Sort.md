Bubble Sort compares adjacent indexes of an input and swaps them if they are in the wrong order.

## Pseudo code
```
bubble_sort(input array x)

	# Can't sort an array of 0 or 1
	If x.length() < 2
		return x

	# One Swap Cycle if there are exactly 2 
	Else if x.length() >= 2
		ittrate n-1 times: Outside loop 
			for y in x.length - itteration: Inside loop
				if x[y] > x[y+1] Swap x[y] and x[y+1]
			end Inside loop
		end Outside loop
		
		return x 
```

## Basic Implementation
Will put like how to implement bubble sort in python, C++ and rust in this section
-> Need to figure out how to create code blocks in Obsidian

### Python
```
#!python
def bubble_sort(x):
	if (x.length() < 2):
		return x
	else if (x.length() >= 2):
		for i in range n-1:
			for j in range x.length() - i:
				if x[j] > x[j+1]:
					temp = x[j]
					x[j] = x[j+1]
					x[j+1] = temp
		return x
					
```

### C++
```
#!cpp

					
```

## Time and Space Complexity
Worst case Time Complexity: O(n^2) - Quadratic
Best case Time Complexity: O(n) - Linear 
(Happens if the input is already in order)
Average case Time Complexity: O(N^2) - Quadratic
Space Complexity: O(1) - Constant Space Complexity

## Optimized Algorithm
In basic version of this algorithm, we compare each value and run through each iteration no matter what. If it's already sorted coming in, then we still run through each iteration. Instead, we can keep track if there have been any swaps during an iteration and if there haven't been, it's sorted and we can return the sorted algorithm


Will put optimized implementation of bubble sort in python, C++ and rust here
