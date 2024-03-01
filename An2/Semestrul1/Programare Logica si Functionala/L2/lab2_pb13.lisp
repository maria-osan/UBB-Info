(defun apartine (elem lst)
	(cond
		((null lst) nil)  ; daca lst este vida
		((eql elem (car lst)) t)  ; elem = l1
		((e_lista (car lst))
			(or (apartine elem (car lst))
			    (apartine elem (cdr lst))
			)
		)
		(t
			(apartine elem (cdr lst))  ; continuam cautarea in restul listei
		)
	)
)


(defun e_lista (x)
	(if (null x)
		(if (eq x '())
			t
			nil)
		(and (consp x) (e_lista (cdr x)))
	)
)


(defun cale (elem lst)
	(cond
		((null lst) nil)  ; daca lst e vida
		((equal (car lst) elem) (list elem))  ; daca elem = lst
		((apartine elem (cadr lst))
			(cons (car lst) (cale elem (cadr lst)))
		)
		((apartine elem (caddr lst))
			(cons (car lst) (cale elem (caddr lst)))
		)
		(t nil)
	)
)


; Exemple:
; (cale 'D '(A (B) (C (D) (E)))) → (A C D)

(setq arb '(a (b () (f)) (d (e () (k)) (l))))
; (cale 'm arb) → NIL
; (cale 'f arb) → (a b f)
; (cale 'k arb) → (a d e k)

(setq arbore '(a (b () (f)) (d (e))))