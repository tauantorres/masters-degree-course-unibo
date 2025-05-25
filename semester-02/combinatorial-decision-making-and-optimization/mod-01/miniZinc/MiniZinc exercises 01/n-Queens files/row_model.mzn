% Row model

include "alldifferent.mzn";

int: n; % number of queens
array[1..n] of var 1..n: rows; %variables & domains 

%column attack constraints

%diagonal attack constraints

%Search
solve satisfy; 

