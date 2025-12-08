Computation works on a Word Ram Model where RAM is made up of an array of words (w bit length vectors). Accessing RAM is Constant time (Meaning that access are unaffected by where it is in the array and how many times you access it. You can skip directly to the index in RAM and read or write to it)

We think of data structures in terms of an access pattern and it's corresponding implementation. 
-> All data structures are built off of arrays in the Word RAM Model, but that might not be conducive to how we want to keep track of our data/use our data in an algorithm.

2 Main access patterns: Set and Sequence

2 Main approaches to solve these problems: Arrays and Pointers/Linked Data Structures


An Access pattern is how we want to use our data:
The example given by the MIT lectures is like what if we want this set of functionality from out data
-Maintain a sequence of items x0, x1, ... xn-1 subject to these operations
-Build(x): Create an array and put x into the indexes
-Len(): Return n, the length of the array
-Iter_seq(): Return x0, x1, ... xn-1 in sequence order
-Get_at(i): Return the value of xi (x[i])
-Set_at(x, i): Set the value of xi to x

The Data Structures solves this: Static Array

### 2 Main access patterns: 
Set and Sequence

### 2 Main approaches to solve these problems:
Arrays and Pointers/Linked Data Structures
-Array: 
