solution :-
List = [father("Baker" , BakerFatherJob),
           father("Carpenter" , CarpenterFatherJob),
           father("Miller" , MillerFatherJob),
           father("Farmer",FarmerFatherJob)],

   List2 = [son("Baker" , BakerSonJob),
           son("Carpenter" , CarpenterSonJob),
           son("Miller" , MillerSonJob),
           son("Farmer",FarmerSonJob)],

   member(father(_, "Baker"), List),
   member(father(_, "Carpenter"), List),
   member(father(_, "Miller"), List),
   member(father(_, "Farmer"), List),   

   member(son(_, "Baker"), List2),
   member(son(_, "Carpenter"), List2),
   member(son(_, "Miller"), List2),
   member(son(_, "Farmer"), List2),     

   BakerFatherJob <> BakerSonJob,  % No son has the same profession as his father.
   CarpenterFatherJob <> CarpenterSonJob,
   MillerFatherJob <> MillerSonJob,
   FarmerFatherJob <> FarmerSonJob,

   BakerFatherJob <> "Baker",
   CarpenterFatherJob <> "Carpenter",
   MillerFatherJob <> "Miller",
   FarmerFatherJob <> "Farmer",

   BakerSonJob <> "Baker",
   CarpenterSonJob <> "Carpenter",
   MillerSonJob <> "Miller",
   FarmerSonJob <> "Farmer",

   BakerFatherJob = CarpenterSonJob,  % Baker has the same profession as the carpenter's son.
   FarmerSonJob = "Baker",  % The farmer's son is a baker.

   write("Father Baker has job ", BakerFatherJob),nl,
   write("Father Carpenter has job ", CarpenterFatherJob), nl,
   write("Father Miller has job ", MillerFatherJob),nl,
   write("Father Farmer has job ", FarmerFatherJob),nl,
   write("                              "), nl,

   write("Son Baker has job ", BakerSonJob),nl,
   write("Son Carpenter has job ", CarpenterSonJob), nl,
   write("Son Miller has job ", MillerSonJob),nl,
   write("Son Farmer has job ", FarmerSonJob),nl,
   write("                              "), nl,

   fail.

solution:- 
   write(" ALL SOLUTIONS HAVE BEEN FOUND").