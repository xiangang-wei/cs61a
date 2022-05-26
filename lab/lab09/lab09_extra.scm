;; Extra Scheme Questions ;;


; Q5
(define lst
  'YOUR-CODE-HERE
  ; The png file is broken on the page
)

; Q6
(define (composed f g)
  (define (compose_f_g a)
          (f (g a))
  )
  compose_f_g
)

; Q7
(define (remove item lst)
  (filter (lambda (x) (not (= item x))) lst)
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

; Q8
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
  (if (or (= 0 a) (= 0 b))
      (max a b)
      (if (= 0 (remainder (max a b) (min a b)))
          (min a b)
          (gcd (min a b) (remainder (max a b) (min a b)))
      )
  )
)

;;; Tests
(gcd 24 60)
; expect 12
(gcd 1071 462)
; expect 21

; Q9
(define (no-repeats s)
  (if (null? s)
      nil
      (cons (car s) (no-repeats (filter (lambda (x) (not (= x (car s)))) (cdr s))))
  )
)

; Q10
(define (substitute s old new)
  (if (null? s)
      nil
      (if (pair? (car s))
          (cons (substitute (car s) old new) (substitute (cdr s) old new))
          (if (eq? old (car s))
              (cons new (substitute (cdr s) old new))
              (cons (car s) (substitute (cdr s) old new))
          )
      )
  )
)

; Q11
(define (sub-all s olds news)
  (if (null? olds)
      s
      (sub-all (substitute s (car olds) (car news)) (cdr olds) (cdr news))
  )
)