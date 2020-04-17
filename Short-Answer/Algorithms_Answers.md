#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
O(n)

This loop will the number of times equal to what n is.
For example, if n == 4:
The first iteration of the function will run as a, which is 0, < 4^3, which is 64.
a is then set to itself plus n^2, which is now 16.

IT 2 now compares 16 to 64.
a is now 32.

IT3 compares 32 to 64.
a is now 64.

IT4 compares 64 to 64.
a is now greater than n^3, so the loop breaks.

The loop runs n times, as that is how many loops need to take place for for a to equal n.

This can be tested by adding count += 1 and returning the count at the end of the function.


b)
O(nlogn)

If the loop were to only run n times, it would be O(n).

However, as the value of n increase, the number of times the while loop must be performed increases exponentially, making the while loop O(logn), as the number of times it must loop is not linear based on it's inital value being set to 1, instead of some deviation of n.

This causes the function to run at O(nlogn).


c)
O(n)

The loop using recursion to run the number of times equal to n, as can be seen by each time the function is called recursively, the number of bunnies decrements by 1.

If we pass in 4, each time the function will decrement the number of bunnies by 1, until bunnies == 0, which will cause the loop to break, making it O(n).

## Exercise II

We would want to take our number of floors, f, and find the middle point and test if the egg breaks there. This operation would be O(n) as we are simply moving through the number of elements in the list to find the middle element and splitting the list there.

Next we would want to break the egg at each halfway point of of our now split list. If we had 40 floors, we are breaking the egg first at floor 20, then and floors 10 and 30. These sub tests will run at O(n), however, the the end runtime would not be O(n^2) because we are not performing the split test linearly based on n, but as n increases, so must the number of times we must split to find the floor where the egg doesn't break, causing this to run at O(logn).

Psuedo Code:
1. If there are 40 floors, split it into floors 1-20 and 21-40.
2. Throw egg off middle floor (floor 20).
3. If egg breaks, go to middle floor of bottom half (floor 10).
4. Repeat step 2 (floor 10).
5. If egg does not break, go to middle of bottom half (floor 15).
6. Repeat step 2.
7. If egg does not break, repeat step 2-5 until egg breaks.
8. Perform same operations on upper half if egg does not break during step 3.


