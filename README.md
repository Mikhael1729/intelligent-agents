# Exercises

## Exercise 3

Consider the problem of finding a path in the grid shown in Figure 3.14 from the position $s$ to the position $g$. A piece can move on the grid horizontally or vertically, one square at a time. No step may be made into a forbidden shaded area.

<center>
<img src="images/x373.png" style="background-color: white;"/>
</center>

1. On the grid shown in Figure 3.14, number the nodes expanded (in order) for a depth-first search from $s$ to $g$, given that the order of the operators is up, left, right, and down. Assume there is cycle pruning. What is the first path found?
1. On a copy of the same grid, number the nodes expanded, in order, for a greedy best-first search from $s$ to $g$. Manhattan distance should be used as the evaluation function. The Manhattan distance between two points is the distance in the x-direction plus the distance in the y-direction. It corresponds to the distance traveled along city streets arranged in a grid. Assume multiple-path pruning. What is the first path found?
1. On a copy of the same grid, number the nodes expanded, in order, for a heuristic depth-first search from $s$ to $g$, given Manhattan distance as the evaluation function. Assume cycle pruning. What is the path found?
1. Number the nodes in order for an A∗ search, with multiple-path pruning, for the same grid. What is the path found?
1. Show how to solve the same problem using dynamic programming. Give the cost_to_goal value for each node, and show which path is found.
1. Based on this experience, discuss which algorithms are best suited for this problem.
1. Suppose that the grid extended infinitely in all directions. That is, there is no boundary, but $s$, $g$, and the blocks are in the same positions relative to each other. Which methods would no longer find a path? Which would be the best method, and why?
