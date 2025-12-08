Big O notation is used to describe the upper bound (Worst case) of an algorithm's Time or Space Complexity indicating how the runtime or memory usage grows as the input size increases.
-It helps compare the efficiency of different algorithms by providing a way to express their performance in terms of worst case scenario

Asymptotic Analysis describes the behavior of an algorithm and not precise details about it's performance. (An algorithm with a quadratic growth pattern will eventually perform worse than an algorithm with a linear growth pattern, we don't care specifically about when it starts to perform worse)




Precise definition is 
*To finish*
```
Let f, the function to be estimated be
f(x) = O(g(x))  -  (F(x) is big O of g(x))
if there exists a positive real number M such that |f(x)| <= Mg(x) for all x...

```

But basically its about how fast an algorithm grows with more inputs.
**Note that this notation is specifically talking about growth of a atomic instructions or steps that the processor will have to do with the growth of inputs to the algorithm after a certain amount of time. It will eventually converge into a common pattern of growth, but maybe some of the start up instructions won't follow that pattern**


The point is to try to remove as many possible factors for different performance. 
-First, we don't care what type of computer system we're using. (Let's not take into account Hardware or OS) We want to try to pretend to keep everything equal and compare the algorithms based on basic atomic instructions or generic memory usage.
-Then, we try to make remove all of the extra details and just take the biggest factor. This includes any coefficient and constants.
-We try to express the algorithm's run time or memory in terms of a function of number of inputs. We describe it's growth pattern in terms of how the time or space complexity scales with inputs at a sufficiently large size.

**** I don't know where to put this yet, but one point I want to make, is that if an algorithm is big O of n, it's also big of of every asymptotic function bigger than that too. We're not just solving for an asymptotic function that can be used for the function but the tightest bound that still works.

## **Other Types of Asymptotic Analysis**
-Big theta/Big Omega Notation
### Big Omega Notation
Lower Bound

### Big Theta Notation
Exact growth rate (Both upper and lower bound of an algorithm's growth rate)
So, like if you can choose two different C values to multiply your big Theta growth pattern by where C1 is always above, and C2 is always below, then that function satisfies big Theta

| Function     | Description                          |
| ------------ | ------------------------------------ |
| f(n)         | Specific growth rate of an algorithm |
| O(n)         | Upper bound of growth                |
| $\\Omega$(n) | Lower bound of growth                |
| $\\Theta$(n) | Tight bound of growth                |

## **Time vs Space Complexity**
Time Complexity refers to the number of instructions or the amount of time it takes to complete an algorithm.
Space Complexity refers to the ...


Table of common big O growth patterns

| Growth Pattern Name                                                                                                          | Big O Notation | Example                                                                                                                     |
| ---------------------------------------------------------------------------------------------------------------------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Constant                                                                                                                     | O(1)           | Single Operation: x = 5 + (15*20) - Doesn't care about number of inputs                                                     |
| Logarithmic                                                                                                                  | O(log(n))      |                                                                                                                             |
| Linear                                                                                                                       | O(n)           | For loop: for x in range (O, n) print n - One operation per input.                                                          |
| Linearithmic                                                                                                                 | O(nlog(n))     |                                                                                                                             |
| Polynomial or Quadradic (Quadradic meaning the n^2 specifically, and polynomial referring to n^x where x is just any number) | O(n^2)         | Nested for loop: for x in range (o, n) for y in range (o, n) print x *y - For each n, we have to run through n^2 operations |
| Exponential                                                                                                                  | O(2^n)         |                                                                                                                             |
| Factorial                                                                                                                    | O(n!)          |                                                                                                                             |

How do we analyze an algorithm for it's big Asymptotic Growth Rate?

We have to figure out what expression (Part of the algorithm) is the dominant cause of scaling. To do this, we have to create an expression for the algorithm. 

To create an expression, we would need to figure out how many atomic operations a processor would take to accomplish a step of the algorithm. Like, for example reading and writing from memory might count as some atomic instructions, arithmetic instructions would also count.

Common first algorithms to analyze are sorting algorithms. So let's describe a sorting algorithm and try to analyze it's big O

* Is there a way to display a section of the other note in this section of the text?*
[[Bubble Sort]]



For bubble sort, if we have an array with 2 values, we compare the two values, and if the value in index 0 is greater than the value in index 2, we swap them. That's the worst case scenario, so that would be 1 atomic operation to compare them, and 1 to swap them in memory.

If there are 3 values, we do the same algorithm for index 0-1 pair, then for the index 1-2 pair, then you repeat again for a second iteration for the 0-1 pair. (You can skip the 1-2 pair on the second iteration because you know it's guaranteed to be the biggest) 
-> Worst case scenario, all 3 comparisons need to be swapped. This would be 6 atomic instructions

If there are 4 values, we do the same algorithm. For the first iteration, we might need to compare and swap 0-1, 1-2, 2-3. Then in the second iteration, 0-1, 1-2, then in the third, just 0-1.
-> Worst case scenario, all 6 comparisons need to be swapped. This would be 12 atomic instructions

Let's extrapolate
for each input value n, we might need to run through the algorithm n-1 times. For each time we run through the algorithm, we might need to run through one less compare and swap.
i = number of iterations through the algorithm (n-1)
(n-i) operations per iteration (Because the first iteration makes you run through n-1 swaps, and each iteration after that, you run through 1 less)
The expression would be i(n-i) = (n-1)(n-(n-1)) = (n-1)

Next:
You have to remove all of the lower order components of the expression, and find a value of the constant out in from where you could multiply by to get an asymptotic expression. 

Usually, the final answer will look something like the values in the table above.
g(x) = n^2. i.e. Bubble Sort is big O of n^2

Big Caveat, this is specifically time complexity, and specifically worst case scenario.