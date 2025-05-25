int: n;
array[0..n-1] of var 0..n-1: x;
 
 
% meta constraint

% the first implied constraint

% the second implied constraint

solve satisfy;

output [ "x = \(x);\n" ] ;