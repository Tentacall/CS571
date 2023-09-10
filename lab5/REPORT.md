## LAB: 5
#### Team
- Sanskriti Singh [ 2001CS60 ]
- Rupak Biswas [ 2001CS57 ]
---
### How to run ?
- `python3 main.py [filename?] [flag?]`
- Avilable filename: `input.py`
- Avilable flag: `--compare n`
- Some examples: 

```
python3 main.py input.py
```
- runs Simulated Annealing on `input.txt`

```
python3 main.py input.py --compare
```
- runs Simulated Annealing and Hill Climbing, each once, on the `input.txt`

```
python3 main.py --compare 4
```
- runs Simulated Annealing and Hill Climbing, each 4 times

## Problem Statement

- Input: Input should be taken from an input file and processed as a matrix.
- Other inputs are Temperature variable T, heuristic function, neighborhood generating function,  probability function to decide state change, and a cooling function.
- Objective functions to be checked:
    - h1 (n)= Number of displaced titles.
    - h2 (n)= Total Manhattan distance.


## Questions

### 1. Running Simulated Annealing
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
Running Simmulated anneling Search with heurestics ( h1 ): 
[■■■■■■■■■■■■■■■■■                       ] 42%
Total steps visited: 77292
Solution Possible: True
Time taken: 3.274096 seconds
Optimal Path distance: 73790
Running Simmulated anneling Search with heurestics ( h2 ): 
[■■■■■■■■■■■■■■■■■■■■                    ] 51%
Total steps visited: 93599
Solution Possible: True
Time taken: 4.557908 seconds
Optimal Path distance: 87938
```

### 2. Take multiple examples (at least 3) of the same start state and goal state combinations and compare both algorithms

```
Initial matrix: 
8 3 2 
1 B 4 
5 6 7 
------

Target matrix: 
1 2 3 
4 5 6 
7 8 B 
------
Running Simmulated anneling Search with heurestics ( h1 ): 
[■■■■■■■■■■■■■■■■■■■■■■■■                ] 61%
Total steps visited: 110695
Solution Possible: True
Time taken: 4.790886 seconds
Optimal Path distance: 101060
Running Simmulated anneling Search with heurestics ( h2 ): 
[■■■■■■■■■■■■■■■■■■■                     ] 48%
Total steps visited: 87351
Solution Possible: True
Time taken: 4.500022 seconds
Optimal Path distance: 82678

Initial matrix: 
8 3 2 
1 B 4 
5 6 7 
------

Target matrix: 
1 2 3 
4 5 6 
7 8 B 
------
Running Hill Climbing Search: heurestics (h1)
[                                        ] 0%
Total steps visited: 655
Solution Possible: True
Optimal Solution Distance: 60
Time taken: 0.031584 seconds
Running Hill Climbing Search: heurestics (h2)
[                                        ] 0%
Total steps visited: 94
Solution Possible: True
Optimal Solution Distance: 34
Time taken: 0.005428 seconds

Initial matrix: 
3 7 8 
1 B 2 
4 5 6 
------

Target matrix: 
1 2 3 
4 5 6 
7 8 B 
------
Running Simmulated anneling Search with heurestics ( h1 ): 
[                                        ] 1%
Total steps visited: 3603
Solution Possible: True
Time taken: 0.153665 seconds
Optimal Path distance: 3528
Running Simmulated anneling Search with heurestics ( h2 ): 
[                                        ] 1%
Total steps visited: 3603
Solution Possible: True
Time taken: 0.188681 seconds
Optimal Path distance: 3528

Initial matrix: 
3 7 8 
1 B 2 
4 5 6 
------

Target matrix: 
1 2 3 
4 5 6 
7 8 B 
------
Running Hill Climbing Search: heurestics (h1)
[                                        ] 0%
Total steps visited: 355
Solution Possible: True
Optimal Solution Distance: 46
Time taken: 0.018956 seconds
Running Hill Climbing Search: heurestics (h2)
[                                        ] 0%
Total steps visited: 277
Solution Possible: True
Optimal Solution Distance: 46
Time taken: 0.017439 seconds

Initial matrix: 
8 B 6 
2 3 7 
1 5 4 
------

Target matrix: 
1 2 3 
4 5 6 
7 8 B 
------
Running Simmulated anneling Search with heurestics ( h1 ): 
[■■■■■■■■■■■■■■■■■                       ] 44%
Total steps visited: 79865
Solution Possible: True
Time taken: 4.014278 seconds
Optimal Path distance: 76265
Running Simmulated anneling Search with heurestics ( h2 ): 
[■■■■■■■■■■■■■■■■■■■■■■■■■               ] 64%
Total steps visited: 116299
Solution Possible: True
Time taken: 6.895539 seconds
Optimal Path distance: 102325

Initial matrix: 
8 B 6 
2 3 7 
1 5 4 
------

Target matrix: 
1 2 3 
4 5 6 
7 8 B 
------
Running Hill Climbing Search: heurestics (h1)
[                                        ] 0%
Total steps visited: 559
Solution Possible: True
Optimal Solution Distance: 47
Time taken: 0.041585 seconds
Running Hill Climbing Search: heurestics (h2)
[                                        ] 0%
Total steps visited: 54
Solution Possible: True
Optimal Solution Distance: 25
Time taken: 0.004311 seconds

----SCORES-----
    SA  HC
h1: 1   0
h2: 2   3

SA: 0
HC: 3
```
### 3. Heuristics

#### a. Analyze the results obtained with proper justifications

- Analysis
    - h2 works better than h1 in case of Simulated Annealing
- Justification
    - The Manhattan heuristic is admissible
    - it never overestimates the true cost to reach the goal state
    - It is also consistent

#### b. Describe your results on both algorithms and state the reasons for the difference of approach in both algorithms.

- Results
    - We ran Simulated Annealing 3 times
    - h2 was better in 2/3rd of the cases
    - h2 works better than h1 in case of Simulated Annealing
- Difference in Approach
    - The misplaced tiles heuristic does not take into account the specific movements required to solve the puzzle
    - In contrast, the Manhattan distance heuristic (h2) considers the distance each tile needs to travel to reach its correct position
    - This makes h2 a more informed and accurate measure of the problem's complexity.

#### c. Describe your views on what algorithm should have performed better for this particular problem and does your intuition match the results?

- In our view, the Manhattan distance heuristic (h2) would have performed better
- yes, our intuition match the results

### 4. Simulated Annealing and Hill Climbing Algorithms

#### a. Analyze the results obtained with proper justifications

- Analysis
    - Hill Climbing works better than Simulated Annealing
- Justification
    -  SA has a probabilistic nature and can escape local optima by accepting worse solutions early in the search
    - It lead to finding better overall solutions

#### b. Describe your results on both algorithms and state the reasons for the difference of approach in both algorithms.

- Results
    - We ran SA and HC 3 times
    - HC was better in all of the cases
- Difference in Approach
    - SA is a probabilistic search algorithm that allows for stochastic movements
    - It accepts worse solutions with a certain probability based on a cooling schedule
    - This probabilistic nature enables SA to explore a wider search space, potentially escaping local optima
    - Whereas, HC is a deterministic search algorithm that always chooses the best neighbor state according to the heuristic function
    - It focuses on improving the current state iteratively by moving to the best neighbor
    - It can get stuck in local optima

#### c. Describe your views on what algorithm should have performed better for this particular problem and does your intuition match the results?

- In our view, SA is expected to perform better than Hill Climbing
- This is because SA has the ability to explore a wider solution space due to its probabilistic acceptance of worse solutions

- No, out intuition does not match the results 
- It can be because in SA, the cost is increased and a larger number of states is explored 
- The choice between SA and Hill Climbing may depend on the specific problem requirements

