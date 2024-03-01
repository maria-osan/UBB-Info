;; Cerinta: Sa se construiasca o functie care intoarce suma atomilor numerici dintr-o lista, de la orice nivel.

;; Model matematic:
;;  sumaNumere(x): 
;;		0, daca x este atom si nu ete numeric
;;		x, daca x este atom numeric
;;		+ sumaNumere(xi), i=1,..,n , altfel

(defun sumaNumere (lst)
	(cond
		((numberp lst) lst)
		((atom lst) 0)
		(t (apply #'+ (mapcar #'sumaNumere lst)))
	)
)

;; Exemplu:
(setq lista '(1 a (b c) 3 (2 (4) b) a 5))
(setq rezultat (sumaNumere lista))
(format t "Lista: ~a" lista)
(format t "~%Suma atomilor numerici din lista este: ~a" rezultat)