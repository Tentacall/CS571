
professions([baker, tailor, smith, carpenter]).
profession(X) :- professions(L), member(X, L).

professionOf()