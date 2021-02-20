#lang racket

(define gate%
  (class object%
    (init-field name)
    (super-new)
    (define/public (eval)
      (void))))

(define pin%
  (class object%
    (init-field owner
                name
                [activates #f]
                [monitor #f]
                [value #f])
    (define connections '())
    (super-new)
    (define/public (connect pin)
      (set! connections (cons pin connections)))
    (define/public (set val)
      (when (not (equal? value val))
        (set! value val)
        (when activates
          (send owner eval))
        (when monitor
          (printf "Pin ~a-~a set to ~a~n"
                  (get-field name owner)
                  name
                  value))
        (for ([c connections])
          (send c set val))))))

(define 2gate%
  (class gate%
    (init name)
    (field (a (new pin% [name "a"] [owner this] [activates #t])))
    (field (b (new pin% [name "b"] [owner this] [activates #t])))
    (field (out (new pin% [name "out"] [owner this] [monitor #t])))
    (super-new [name name])))
    
(define nand%
  (class 2gate%
    (init name)
    (super-new [name name])
    (inherit-field a b out)
    (define/override (eval)
      (let ([a (get-field value a)]
            [b (get-field value b)])
        (send out set (not (and a b)))))))