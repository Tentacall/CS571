profession(baker).
profession(tailor).
profession(smith).
profession(carpenter).

professions([(smith,Ps), (baker, Pb), (carpenter,Pc), (tailor, Pt)],
 [(son_of(smith),Pss), (son_of(baker),Pbs), (son_of(carpenter), Pcs), (son_of(tailor), Pts)]) :-
  profession(Ps), profession(Pb), profession(Pc), profession(Pt),
  profession(Pss), profession(Pbs), profession(Pcs), profession(Pts),
  

% When profession is different from name
Ps \= smith,
Pb \= baker,
Pc \= carpenter,
Pt \= tailor,

% Profession of son are different from name
Pss \= smith,
Pbs \= baker,
Pcs \= carpenter,
Pts \= tailor,

% No son is having the same profession as his father
Ps \= Pss,
Pb \= Pbs,
Pc \= Pcs,
Pt \= Pts,

% baker has same profession as carpenters son
Pb = Pcs,

% son of smith is baker
Pss = baker,


% No repitition of profession
Ps \= Pb, Ps \= Pc, Ps \= Pt, Pb \= Pc, Pb \= Pt, Pc \= Pt,
Pss \= Pbs, Pss \= Pcs, Pss \= Pts, Pbs \= Pcs, Pbs \= Pts, Pcs \= Pts.

solution :-
    professions(Fathers, Sons),
    format("Professions of Fathers and Sons:\n", []),
    print_professions(Fathers, Sons).

print_professions([], []).
print_professions([(Father, FatherProfession) | RestFathers], [(Son, SonProfession) | RestSons]) :-
    format("~w is a ~w, and their son is a ~w.\n", [Father, FatherProfession, SonProfession]),
    print_professions(RestFathers, RestSons).
