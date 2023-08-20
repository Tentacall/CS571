## LAB: 2
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

### Problem Statement

- In a general search algorithm, each state (n) maintains a function f(n) = g(n) + h(n) where g(n) is the least cost from the source state to state n found so far and h(n) is the estimated cost of the optimal path from state n to the goal state.
- Implement a search algorithm for solving the 8-puzzle problem with the
following assumptions.
-  - a. g(n) least cost from source state to current state so far.
-  - b. Heuristics
- - - i. h1(n) = 0.
- - - ii. h2(n) = number of tiles displaced from their destined position.
- - - iii. h3(n) = sum of the Manhattan distance of each tile from the goal position.
- - - iv. h4(n) = Devise a heuristics such that h(n) > h∗ (n)

- We took h4 and h5 as:
- - h4(n) = sum of the Chessboard distance of each tile from the goal position.
- - h5(n) = sum of the Euclidian distance of each tile from the goal position.

### Experiments and Benchmarking

#### 20 testcases
```
Benchmarking...
[                                        ] 2%Round 1 completed
[                                        ] 0%Round 2 completed
[                                        ] 0%Round 3 completed
[■                                       ] 2%Round 4 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Round 5 completed
[                                        ] 0%Round 6 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Round 7 completed
[                                        ] 2%Round 8 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Round 9 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Round 10 completed
[■                                       ] 3%Round 11 completed
[■■■■■                                   ] 14%Round 12 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Round 13 completed
[                                        ] 0%Round 14 completed
[                                        ] 0%Round 15 completed
[                                        ] 0%Round 16 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Round 17 completed
[■■■■                                    ] 10%Round 18 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Round 19 completed
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%Round 20 completed

----RESULTS----[20 epochs]
round   h1      h2      h3      h4      h5
0       118806  14464   1897    6117    4422
1       51459   3351    375     1307    919
2       10907   574     136     279     194
3       135293  18681   1787    7217    4801
4       181440  181440  181440  181440  181440
5       74655   5832    1167    2539    1706
6       181440  181440  181440  181440  181440
7       157182  28187   934     8040    4397
8       181440  181440  181440  181440  181440
9       181440  181440  181440  181440  181440
10      118864  15171   2955    7652    5866
11      179620  74069   15986   36301   26321
12      181440  181440  181440  181440  181440
13      4406    271     115     206     185
14      74655   5859    656     2386    1656
15      25092   1388    309     641     464
16      181440  181440  181440  181440  181440
17      176809  58868   7680    25761   18167
18      181440  181440  181440  181440  181440
19      181440  181440  181440  181440  181440

----SCORES-----
h1: 0
h2: 0
h3: 12
h4: 0
h5: 0
<<<<<<< Updated upstream

Q5.
We take a random matrix `[[2,1,8],[3, 'B', 7],[6,5,4]]` to perform this oparetion 
- Hurestic 3
    - total visited = 446 and total step to optimal one = 22
    - lets take some random positions among all visited node
    - lets take 2 random state
        - f(n) = 25, g(n) = 19, h(n) = 6
        - f(m) = 24, gn(m) = 8, h(m) = 16
        - cost(n,m) = 11
        so, 6 <= 11 + 16 ( verified )
- Hurestic 2
    - total visited = 9529 and total step to optimal one = 22
    - lets take 2 random state
        - f(n) = 23, g(n) = 19, h(n) = 4
        - f(m) = 22, gn(m) = 13, h(m) = 9
        - cost(n,m) = 6
        so, 4 <= 6 + 9 ( verified )
- refer to line 35 of `main.py`
=======
```

## 1 Observe and verify that better heuristics expands lesser states.

- According to the observation: h3 > h5 > h4 > h3 > h2 > h1 

## 2 Observe and verify that all the states expanded by better heuristics should also be expanded by inferior heuristics.

- Yes, all states expanded by better heuristics was expanded by also expanded by inferior heuristics

## 3 Observe and verify monotone restrictions on the heuristics.

- Monotone restrictions was followed by h1, h2, and h3

## 4 Observe un-reachability and provide proof.

- Also there are 2 distinct set of states and they are disjoint
- One disjoint set is probably the mirror image of other
- So if there are 9! = 362880 cases, then one disjoint set will have 9!/2 = 181440 nodes
- One can not go from node in one disjoint set to node in another disjoint set
- Hence, if target is fixed and node is random, then probability of finding a path is 50%

## 5 Observe and verify whether the monotone restriction is followed for the following two Heuristics:
### a Monotone restriction: h(n) <= cost(n,m) + h(m)
### i h2(n) = number of tiles displaced from their destined position.
### ii h3(n) = sum of the Manhattan distance of each tile from the goal position.

## 6 Observe and verify that if the cost of the empty tile is added (considering the empty tile as another tile) then monotonicity will be violated
>>>>>>> Stashed changes
