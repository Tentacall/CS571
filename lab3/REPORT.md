## LAB: 3
#### Team
- Sanskriti Singh [ 2001CS60 ]
- Rupak Biswas [ 2001CS57 ]
---
### How to run ?
```python
if __name__ == '__main__':
    sol = Solution()
    sol.benchmark(20)
    # sol.run()
```
- In case of single pass, run the `.run()` function
- For benchmarking run the `.benchmark(epoch)` function

### Benchmarking

#### 20 testcases
```
Benchmarking...
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 1 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 2 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 3 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■              ] 65%Epoch 4 completed
[■■■■■■■■■■■■■■■■                        ] 41%Epoch 5 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■      ] 86%Epoch 6 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■           ] 74%Epoch 7 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■   ] 94%Epoch 8 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 9 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■              ] 65%Epoch 10 completed
[■■■■■■■■■■■■■                           ] 32%Epoch 11 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 12 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 13 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■    ] 92%Epoch 14 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 15 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 16 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■      ] 86%Epoch 17 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 18 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 19 completed
[■■■■■■■■■■■■■                           ] 32%Epoch 20 completed

----RESULTS----[10 epochs]
DFS     BFS     UFS     IDS     result
0       0       0       0       False
0       0       0       0       False
0       0       0       0       False
20386   114430  118806  575244  True
107297  60485   74654   161240  True
41140   149888  157161  250127  True
122816  118409  135232  446400  True
42522   171531  171598  506167  True
0       0       0       0       False
36051   103914  118806  146909  True
49345   62147   59660   259418  True
0       0       0       0       False
0       0       0       0       False
52521   156111  167255  145926  True
0       0       0       0       False
0       0       0       0       False
141114  160993  157182  136992  True
0       0       0       0       False
0       0       0       0       False
116767  62111   59660   192463  True

----SCORES-----
DFS: 6
BFS: 2
UFS: 1
IDS: 1
```

## Observation

### 1.
- From Benchmark we can say DFS in better in average than the rest

### 2.
- By running all algorithms 20 times, 10 times a path was found
- DFS was better in 60% of the cases, BFS in 20%, and UFS and IDS in 10% of the cases each.

### 3.
- Overall, in the terms of the performance (cost)
    - DFS > BFS > UFS > IDS


## Intuition

### 1.
- Also there are 2 distinct set of states and they are disjoint
- One disjoint set is probably the mirror image of other
- So if there are 9! = 362880 cases, then one disjoint set will have 9!/2 = 181440 nodes
- One can not go from node in one disjoint set to node in another disjoint set
- Hence, if target is fixed and node is random, then probability of finding a path is 50%

### 2.
- Here, the graph will have more of a web-like structure than a tree-like structure
- Hence DFS is better at times than BFS
- BFS can be more effective in a tree-like structure

### 3.
- Order of traversing the node (ie moving the blank 'B' up, down, left or right) can effect the output of DFS more drastically than in BFS
- The 'luck' factor can make DFS drastically faster and slower, whereas, BFS performs average every time

### 4.
- Behavior of IDS is similar to that of DFS because it is iterative
- Due to high inter-connectivity between the nodes (states), the number of states visited in higher depth can be lower than the nearly lower depth
- Overall, on an average, the number of states visited is increasing as the depth increases, but not monotonically
- IDS is giving result usually in the range of depth of 30

### 5.
- UFS works like Dijikstra algorithm
- But in this case it doesn't affect the performance much due to the complex structure of the state graph

## Time complexity

### BFS

- Time Complexity: **O(V + E)**, where V is the number of vertices and E is the number of edges in the graph.
- BFS explores nodes level by level, visiting all the neighbors of a node before moving to the next level. In the worst case, it may have to visit all vertices and edges.

### DFS

- Time Complexity: **O(V + E)**, where V is the number of vertices and E is the number of edges in the graph.
- DFS explores as far as possible along a branch before backtracking. The time complexity is similar to BFS but can vary based on the structure of the graph and the chosen traversal path.

### UCS

- Time Complexity: **O(b^(C/e))**, where b is the branching factor of the graph, C is the cost of the optimal solution, and e is the minimum edge cost.
- UCS explores nodes in increasing order of path cost. The time complexity depends on the costs associated with the edges and the optimal solution.

### IDS

- Time Complexity: **O(b^d)**, where b is the branching factor of the graph and d is the depth of the shallowest goal.
- IDS combines DFS and BFS. It performs multiple DFS searches with increasing depth limits. The time complexity is bounded by the DFS complexity at the maximum depth.