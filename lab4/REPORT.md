## LAB: 4
#### Team
- Sanskriti Singh [ 2001CS60 ]
- Rupak Biswas [ 2001CS57 ]
---
### How to run ?
```python
if __name__ == '__main__':
    sol = Solution()
    sol.benchmark(10)
    #sol.matrix = [[2,1,8],[3, 'B', 7],[6,5,4]]
    #sol.posx, sol.posy = 1, 1
    #sol.run()
```
- In case of single pass, run the `.run()` funtion
- For benchmarking run the `.benchmark(epoch)` function

## Problem Statement

- A local search algorithm tries to find the optimal solution by exploring the states in the local region. Hill climbing is a local search technique that always looks for a better solution in its neighborhood

- Implement the Hill Climbing Search Algorithm for solving the 8-puzzle problem

- Check the algorithm for the following heuristics: 
    - i. h1(n) = number of tiles displaced from their destined position. (h2 from LAB2)
    - ii. h2(n) = sum of the Manhattan distance of each tile from the goal position. (h3 from LAB2)

## Experiments and Benchmarking

### Test run
```

Initial matrix: 
2 1 8 
3 B 7 
6 5 4 
------

Target matrix: 
1 2 3 
4 5 6 
7 8 B 
------
Running Hill Climbing Search: 

Total steps visited: 447
Solution Possible: True
Optimal Solution Distance: 38
Time taken: 0.018060 seconds
Running Hill Climbing Search: 

Total steps visited: 714
Solution Possible: True
Optimal Solution Distance: 66
Time taken: 0.036869 seconds

```

### 10 test cases
```
Benchmarking...
Round 1 completed
Round 2 completed
Round 3 completed
Round 4 completed
Round 5 completed
Round 6 completed
Round 7 completed
Round 8 completed
Round 9 completed
Round 10 completed

----RESULTS----[10 epochs]
round   h2      h3
0       181440  181440
1       628     516
2       181440  181440
3       633     675
4       181440  181440
5       542     187
6       181440  181440
7       572     321
8       181440  181440
9       414     325

----SCORES-----
h2: 1
h3: 4
```

### 20 test cases
```
Benchmarking...
Round 1 completed
Round 2 completed
Round 3 completed
Round 4 completed
Round 5 completed
Round 6 completed
Round 7 completed
Round 8 completed
Round 9 completed
Round 10 completed
Round 11 completed
Round 12 completed
Round 13 completed
Round 14 completed
Round 15 completed
Round 16 completed
Round 17 completed
Round 18 completed
Round 19 completed
Round 20 completed

----RESULTS----[20 epochs]
round   h2      h3
0       630     301
1       534     265
2       181440  181440
3       267     163
4       181440  181440
5       181440  181440
6       181440  181440
7       969     860
8       296     247
9       300     257
10      173     720
11      745     507
12      181440  181440
13      181440  181440
14      181440  181440
15      181440  181440
16      586     476
17      205     236
18      1199    158
19      952     64

----SCORES-----
h2: 2
h3: 10
```

## Observation

- In the test run, optimal path was different each time

- Ran code 10 times
    - 5 times (50%) a path was found
    - h3 was better in 80% cases

- Ran code 20 times
    - 12 times (60%) a path was found
    - h3 was better in 83.33% cases

## Intuition and Conclusion

### 1.
- Also there are 2 distinct set of states and they are disjoint
- One disjoint set is probably the mirror image of other
- So if there are 9! = 362880 cases, then one disjoint set will have 9!/2 = 181440 nodes
- One can not go from node in one disjoint set to node in another disjoint set
- Hence, if target is fixed and node is random, then probability of finding a path is 50%

### 2.
- Global Optimal can be or cannot be reached using Hill Climbing Algorithm
- It uses local minima to find an optimal path
- If a local minima is reached which is not a global minima, then global minima will not be found

### 3.
- h3 (sum of the Manhattan distance of each tile from the goal position) is much better heuristic than h2 (number of tiles displaced from their destined position) to search the target in this case


## Time Complexity
- The actual time complexity can vary widely based on the specific problem and the nature of the search space
- In the worst case, Hill Climbing can get stuck in local optima or plateaus, which can result in it taking a long time to find a solution
- However, in many cases, especially if the search space is relatively smooth and the initial state is close to an optimal solution, Hill Climbing can be quite efficient
- In a general sense, the time complexity of Hill Climbing is typically notated as follows:
    - Time Complexity: O(iterations * neighbor_generation)
    - Here, "iterations" represents the number of iterations the algorithm performs, and "neighbor_generation" is the time it takes to generate neighboring states or solutions from the current state
