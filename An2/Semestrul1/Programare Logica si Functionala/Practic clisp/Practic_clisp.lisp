;; Modele matematice:
;; inversa (l1 l2...ln) = { [], daca n = 0
;;			    inversa(l2...ln) + l1, daca l1 este atom
;;			    inversa(l2...ln) + inversaSublista(l1), altfel


(defun inversa (lst)
	(cond
		((null lst) '())
		((atom (car lst)) (append (inversa (cdr lst)) (list (car lst))))
		(t (append (inversa (cdr lst)) (list (inversa (car lst)))))
	)
)