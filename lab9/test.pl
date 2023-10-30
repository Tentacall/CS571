% Define the list of possible professions.
professions([baker, tailor, smith, carpenter]).

% Define the relationship between parents and sons.
parent_son(Profession1, Profession2) :-
    professions(Professions),
    select(Profession1, Professions, Remaining1),
    select(Profession2, Remaining1, _).

% Rules for finding the parents and sons professions.
find_professions(Parents, Sons) :-
    findall((Parent, Son), (parent_son(Parent, Son), Parent \= Son), Pairs),
    partition_parents_sons(Pairs, Parents, Sons).

% Helper predicate to partition parents and sons.
partition_parents_sons([], [], []).
partition_parents_sons([(Parent, Son) | Rest], [Parent | Parents], [Son | Sons]) :-
    partition_parents_sons(Rest, Parents, Sons).

% Find the professions of the parents and sons.
solution :-
    find_professions(Parents, Sons), writeln(Parents), writeln(Sons).
