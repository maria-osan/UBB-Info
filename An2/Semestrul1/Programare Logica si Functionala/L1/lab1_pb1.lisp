;; a)
(defun insert (lst elem &optional (index 1))
	(if (null lst)
		lst
		(if (evenp index)
			(cons (car lst) (cons elem (insert (cdr lst) elem (1+ index))))
			(cons (car lst) (insert (cdr lst) elem (1+ index)))
		)
	)
)

;; Exemplu:
(setq lista '(1 2 3 4 5 6 7 8)) ; Lista initiala
(setq elem_de_inserat 'x) ; elemul de inserat
(setq lista_modificata (insert lista elem_de_inserat))
(print lista_modificata)



;; b)
(defun invers_aux (lst rez)
	(cond
		((null lst) rez)
		((atom (car lst))
			(invers_aux (cdr lst) (cons (car lst) rez))
		)
		(t (invers_aux (cdr lst) (cons (invers_aux (car lst) ()) rez)))
	)
)

(defun invers (lst)
	(invers_aux lst ())
)

;; Exemplu:
(setq lista '(((A B) C) (D E))) ; Lista data
(setq lista_inversata (invers lista)) ; Lista in ordine inversa
(format t "~%")
(print lista_inversata)



;; c) 
(defun cmmdc (a b)
	(if (= b 0)
		a
		(cmmdc b (mod a b))
	)
)

(defun cmmdc_list (lst)
	(cond
		((null lst) 0)
		((atom lst) lst)
		(t
			(cmmdc (car lst) (cmmdc_list (cdr lst)))
		)
	)
)

;; Exemplu:
(setq lista '(12 18 24)) ; Lista neliniara de numere
(format t "~%~%Lista: ~A" lista)
(let ((x (cmmdc_list lista)))
	(format t "~%CMMDC al listei este ~A~%" x)
)



;; d)
(defun numar_aparitii (lst elem)
	(cond
		((null lst) 0)
		((atom lst)
			(if (equal lst elem) 1 0)
		)
		(t
			(+ (numar_aparitii (car lst) elem)
			   (numar_aparitii (cdr lst) elem))
		)
	)
)

;; Exemplu:
(setq lista '(((A B) C) (D E (F G)) A B C)) ; Lista neliniara
(setq elem_cautat 'A) ; Elementul cautat
(format t "~%~%Lista: ~A" lista)
(format t "~%Elementul ~A apare de " elem_cautat)
(print (numar_aparitii lista elem_cautat))
(format t " ori in lista.")