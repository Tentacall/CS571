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

Q2.
```python
def verify_q2(self):
        visited_states = [None, None, None, None, None]
        hurestics = [self.h1, self.h2, self.h3, self.h4, self.h5]
        for i in range(5):
            visited_states[i] =  self.search(self.matrix, self.posx, self.posy, hurestics[i] )

        for key in visited_states[3]:
            if key not in visited_states[4]:
                print("h4 is not admissible")
                break
            if key not in visited_states[2]:
                print("h3 is not admissible")
                break

            if key not in visited_states[1]:
                print("h2 is not admissible")
                break
        print("All hurestics are admissible")
```

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