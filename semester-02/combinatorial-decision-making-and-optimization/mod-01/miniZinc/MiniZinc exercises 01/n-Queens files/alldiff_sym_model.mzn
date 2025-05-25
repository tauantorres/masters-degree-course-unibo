% alldiff_sym model

include "alldifferent.mzn";

int: n; % number of queens
array[1..n] of var 1..n: q; %variables & domains 

%column attack constraints

%diagonal attack constraints

%dual model 
include "lex_lesseq.mzn";
array[1..n, 1..n] of var bool: qb; %dual variables & domains 

%chanelling constraints

%symmetry breaking constraints 


%Search
solve satisfy;