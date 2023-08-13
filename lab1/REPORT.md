## LAB: 1
#### Team
- Sanskriti Singh [ 2001CS61 ]
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

### Benchmarking on 20 testcase
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

## Observation
- From Benchmark we can say DFS in better in avarage
- Also there are 2 distinct set of states and they are disjoint