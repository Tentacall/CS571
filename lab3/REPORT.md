## LAB: 3
#### Team
- Sanskriti Singh [ 2001CS60 ]
- Rupak Biswas [ 2001CS57 ]
---
### How to run ?
```
if __name__ == '__main__':
    sol = Solution()
    sol.benchmark(20)
    # sol.run()
```
- In case of single pass, run the `.run()` function
- For benchmarking run the `.benchmark(epoch)` function

### Benchmarking

#### 50 testcases
```
Benchmarking...
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 1 completed
[■■■■■■■■■■■■■■■■■■■■■■                  ] 56%Epoch 2 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 3 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 4 completed
[■■■■■■■■                                ] 21%Epoch 5 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 6 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 7 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■           ] 74%Epoch 8 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■           ] 74%Epoch 9 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 10 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■           ] 74%Epoch 11 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 12 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 13 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■      ] 86%Epoch 14 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■         ] 79%Epoch 15 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■    ] 92%Epoch 16 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 17 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 18 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 19 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 20 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 21 completed
[■■■■■■■■■■■■■■■■                        ] 41%Epoch 22 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 23 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 24 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 25 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 26 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■    ] 92%Epoch 27 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 28 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 29 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■  ] 97%Epoch 30 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 31 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 32 completed
[                                        ] 1%Epoch 33 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■         ] 79%Epoch 34 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■         ] 79%Epoch 35 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■         ] 79%Epoch 36 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■              ] 65%Epoch 37 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■              ] 65%Epoch 38 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 39 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■         ] 79%Epoch 40 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 41 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 42 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 43 completed
[■■■■■■■■■■■■■■■■                        ] 41%Epoch 44 completed
[■■■■■■■■■■■■■■■■■■■■                    ] 50%Epoch 45 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 46 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 47 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 48 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 49 completed
[■■■■■■■■                                ] 21%Epoch 50 completed

----RESULTS----[50 epochs]
DFS     BFS     UFS     IDS     result
0       0       0       0       False
34157   85568   101740  171017  True
0       0       0       0       False
0       0       0       0       False
584     37779   39782   40942   True
0       0       0       0       False
0       0       0       0       False
122056  129240  135257  99293   True
6637    138711  135257  105689  True
0       0       0       0       False
57751   122554  135232  165026  True
0       0       0       0       False
0       0       0       0       False
132500  159690  157161  77969   True
21157   134268  144099  7725    True
6595    159085  167246  166310  True
0       0       0       0       False
0       0       0       0       False
0       0       0       0       False
0       0       0       0       False
0       0       0       0       False
50105   61995   74654   38410   True
0       0       0       0       False
0       0       0       0       False
0       0       0       0       False
0       0       0       0       False
129358  168983  167255  66393   True
0       0       0       0       False
0       0       0       0       False
105096  175890  176809  102926  True
0       0       0       0       False
0       0       0       0       False
114731  3127    3109    156734  True
23899   146814  144099  128215  True
62462   143895  144099  2050    True
3314    128861  144099  120099  True
93438   122135  118864  76457   True
28980   116432  118864  169354  True
0       0       0       0       False
38679   138679  144099  101186  True
0       0       0       0       False
0       0       0       0       False
0       0       0       0       False
53172   78876   74655   106993  True
88130   79008   91092   50665   True
0       0       0       0       False
0       0       0       0       False
0       0       0       0       False
0       0       0       0       False
11800   40754   39782   128099  True

----SCORES-----
DFS: 11
BFS: 0
UFS: 11
IDS: 0

## Observation

### 1.
- From Benchmark we can say DFS in better in average than BFS in this case

### 2.
- By running both BFS and DFS 20 times, 10 times a path was found
- DFS was better in 80% of the cases than BFS

### 3.
- By running both BFS and DFS 100 times, 47 times a path was found
- DFS was better in 74% of the cases than BFS

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