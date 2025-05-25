(declare-fun a () (Array Int Real))
(declare-fun b () (Array Int Real))
(declare-fun i () Int)
(declare-fun j () Int)
(declare-fun x () Real)
(declare-fun y () Real)

; write(a,i,x) != b
(assert (not (= (store a i x) b)))      

; read(b, i) = y
(assert (= (select b i) y))

; read(write(b,i,x), j) = y
(assert (= (select (store b i x) j) y)) 

; a = b
(assert (= a b))

; i = j                     
(assert (= i j))                       

(check-sat)
