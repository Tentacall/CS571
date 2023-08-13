## LAB: 1
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
- In case of single pass, run the `.run()` funtion
- For benchmarking run the `.benchmark(epoch)` function

### Benchmarking

#### 20 testcases
```
Benchmarking...
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 1 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 2 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■      ] 86%Epoch 3 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 4 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 5 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ] 98%Epoch 6 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 7 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 8 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 9 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 10 completed
[■■■                                     ] 7%Epoch 11 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■   ] 93%Epoch 12 completed
[■■■■■■■■■■■■■■■■■■■■                    ] 50%Epoch 13 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■       ] 84%Epoch 14 completed
[■■■■■■■■                                ] 22%Epoch 15 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 16 completed
[■■■■■■■■■■■■■■■■■■■                     ] 48%Epoch 17 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■               ] 64%Epoch 18 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Epoch 19 completed
[■■■■■■■■■■■■■■■■■■■■■■■■                ] 62%Epoch 20 completed

----RESULTS----[20 epochs]
DFS     BFS     result  deviation
181440  181440  False   0
181440  181440  False   0
126817  156687  True    -29870
181440  181440  False   0
181440  181440  False   0
66299   178287  True    -111988
181440  181440  False   0
181440  181440  False   0
181440  181440  False   0
181440  181440  False   0
91464   13759   True    77705
2432    170482  True    -168050
47811   91012   True    -43201
118809  152795  True    -33986
94571   40753   True    53818
181440  181440  False   0
19665   87451   True    -67786
104693  116655  True    -11962
181440  181440  False   0
91431   113201  True    -21770
--------------
Average
DFS     BFS
128919.6        146774.1

----SCORES-----
DFS: 8
BFS: 2
``` 

#### 100 testcases
```
Average
DFS     BFS
126476.13       143867.44

----SCORES-----
DFS: 35
BFS: 12
```

## Observation

### 1.
- From Benchmark we can say DFS in better in average than BFS in this case

### 2.
- By running both BFS and DFS 20 times, 10 times a path was found
- DFS was better in 80% of the cases than BFS

### 3.
- By running both BFS and DFS 100 times, 47 times a path was found
- DFS was better in 74% of the cases than BFS

## Intuition and Conclusion

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