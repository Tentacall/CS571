solve :-
    initial(Start),
    breadthfirst([[Start]], Solution),
    write(Solution), nl,
    printsol(Solution).

% safe(NumOfMissionaries, NumOfCannibals) is true if NumOfMissionaries is 0 or 3 or equal to NumOfCannibals
safe(0, _).
safe(3, _).
safe(X, X).

% A state is represented by a term: state(NumOfMissionaries, NumOfCannibals, BoatAtEast)
initial(state(3, 3, 1)).
goal(state(0, 0, 0)).

goalpath([Node | _]) :- goal(Node).

% move(State1, State2): making a move in State1 results in State2
move(state(M1, C1, 1), state(M2, C1, 0)) :- M1 > 1, M2 is M1 - 2, safe(M2, C1). % Two missionaries from east to west
move(state(M1, C1, 0), state(M2, C1, 1)) :- M1 < 2, M2 is M1 + 2, safe(M2, C1). % Two missionaries from west to east
move(state(M1, C1, 1), state(M1, C2, 0)) :- C1 > 1, C2 is C1 - 2, safe(M1, C2). % Two cannibals from east to west
move(state(M1, C1, 0), state(M1, C2, 1)) :- C1 < 2, C2 is C1 + 2, safe(M1, C2). % Two cannibals from west to east
move(state(M1, C1, 1), state(M1, C2, 0)) :- C1 > 0, C2 is C1 - 1, safe(M1, C2). % One cannibal from east to west
move(state(M1, C1, 0), state(M1, C2, 1)) :- C1 < 3, C2 is C1 + 1, safe(M1, C2). % One cannibal from west to east
move(state(M1, C1, 1), state(M2, C2, 0)) :- M1 > 0, M2 is M1 - 1, C1 > 0, C2 is C1 - 1, safe(M2, C2). % One missionary and one cannibal from east to west
move(state(M1, C1, 0), state(M2, C2, 1)) :- M1 < 3, M2 is M1 + 1, C1 < 3, C2 is C1 + 1, safe(M2, C2). % One missionary and one cannibal from west to east

printsol([X]) :- write(X), write(': initial state'), nl.
printsol([X | Y]) :- printsol(Y), write(X), explain(Y, X), nl.

explain(state(M1, C1, 1), state(M2, C2, _)) :-
    X is M1 - M2,
    Y is C1 - C2,
    write(': '), write(X), write(' missionaries and '),
    write(Y), write(' cannibals moved from East to West').
    
explain(state(M1, C1, 0), state(M2, C2, _)) :-
    X is M2 - M1,
    Y is C2 - C1,
    write(': '), write(X), write(' missionaries and '),
    write(Y), write(' cannibals moved from West to East').

% An implementation of breadth-first search.
% breadthfirst([Path1, Path2, ...], Solution):
% each Pathi represents [Node | Ancestors], where Node is in the open list and
% Ancestors is a path from the parent of Node to the initial node in the search tree.
% Solution is a path (in reverse order) from initial to a goal.
breadthfirst([Path | _], Path) :- goalpath(Path). % If Path is a goal-path, then it is a solution.
breadthfirst([Path | Paths], Solution) :-
    extend(Path, NewPaths),
    append(Paths, NewPaths, Paths1),
    breadthfirst(Paths1, Solution).

% setof(X, Condition, Set) is a built-in function: it collects all X satisfying Condition into Set.
extend([Node | Path], NewPaths) :-
    setof([NewNode, Node | Path], (move(Node, NewNode), not(member(NewNode, [Node | Path]))), NewPaths),
    !.
extend(_, []). % Set of failed: Node has no successor

not(P) :- \+ P.
not(_).
