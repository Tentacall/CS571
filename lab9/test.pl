% Define the valid professions
profession(baker).
profession(carpenter).
profession(miller).
profession(farmer).

% Define the fathers and sons with their professions
father(smith, Fs) :- profession(Fs).
father(baker, Fb) :- profession(Fb).
father(carpenter, Fc) :- profession(Fc).
father(tailor, Ft) :- profession(Ft).

son(son_of(smith), Ss) :- profession(Ss).
son(son_of(baker), Sb) :- profession(Sb).
son(son_of(carpenter), Sc) :- profession(Sc).
son(son_of(tailor), St) :- profession(St).

% Ensure that no father and son have the same profession
not_same_profession(X, Y) :- X \= Y.

% Additional constraints
son(son_of(baker), P) :- father(carpenter, P).
son(son_of(farmer), P) :- father(tailor, P).

% Print the results
goal :-
    writeln("Professions of the parents and sons:"),
    father(smith, Ps), write("Smith's profession: "), writeln(Ps),
    father(baker, Pb), write("Baker's profession: "), writeln(Pb),
    father(carpenter, Pc), write("Carpenter's profession: "), writeln(Pc),
    father(tailor, Pt), write("Tailor's profession: "), writeln(Pt),
    son(son_of(smith), Pss), write("Profession of Smith's son: "), writeln(Pss),
    son(son_of(baker), Pbs), write("Profession of Baker's son: "), writeln(Pbs),
    son(son_of(carpenter), Pcs), write("Profession of Carpenter's son: "), writeln(Pcs),
    son(son_of(tailor), Pts), write("Profession of Tailor's son: "), writeln(Pts).

