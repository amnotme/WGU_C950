# 3.7 Dynamic programming: Get to a location

# Specification

Write a program that uses dynamic programming to solve the following problem.

Given a point P (`p`) on a cartesian plane, take a given amount of steps along the x-axis and y-axis for each iteration and get as close to `p` as possible. After every 3rd iteration, take a given amount of steps backwards in the x and y directions. Arrive at a point (x, y) whose distance is closest to `p` (using the distance formula). Start at the origin (0,0).

## `Point` class

The `Point` class is provided for you. The class has two data members:

- `x` - The x-coordinate of a point
- `y` - The y-coordinate of a point

## The main program

`p` has been defined and code to read in the x and y coordinates (integers) for point `p` is also provided.

1) Output `p`.

2) Read in the number of steps the be taken:

- forwards along the x-axis
- forwards along the y-axis
- backwards along both axes every 3rd iteration

3) Define a dynamic programming algorithm that advances and retreats the required number of steps along the x and y axes and determines the closest point to `p`. After each iteration, calculate the distance between point `p` and the current location using the distance function:`d = sqrt((x_p - x_1)^2 + (y_p - y_1)^2)`Count the number of iterations. *Hint: Keep track of the previous location.*

4) Output the final arrival point (the point closest to `p`), the distance between the arrival point and `p`, and the number of iterations taken.

Ex: For the input

```
4
5
2
3
1

```

where (4,5) is point `p`, 2 is number of steps to take along the x-axis each iteration, 3 is the number of steps to take along the y-axis each iteration, and 1 is the number of steps to take backwards along both the x and y axes each 3rd iteration, the output is
