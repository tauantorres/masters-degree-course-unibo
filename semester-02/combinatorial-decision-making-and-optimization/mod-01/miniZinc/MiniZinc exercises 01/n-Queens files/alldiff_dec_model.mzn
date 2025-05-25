% Alldiff decomposition model

include "alldifferent.mzn";

int: n ; % number of queens
array [1..n] of var 1..n: q; % variables & domains 


% aldiff decomposition

solve :: int_search(q, input_order, indomain_min)  satisfy;

