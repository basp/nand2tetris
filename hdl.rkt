#lang racket

(define gate%
  (class object%
    (init-field name)
    (super-new)
    (define/public (eval)
      (void))))

(define pin%
  (class object%
    (init-field owner name [activates #f] [monitor #f] [value #f])
    (define edges '())
    (super-new)
    (define/public (connect pin)
      (set! edges (cons pin edges)))
    (define/public (set val)
      (when (not (equal? value val))
        (set! value val)
        (when (and activates owner)
          (send owner eval))
        (when monitor
          (let ([owner (get-field name owner)])
            (printf "Pin ~a-~a set to ~a~n" owner name value)))
        (for ([edge edges])
          (send edge set val))))))

(define 2gate%
  (class gate%
    (init name)
    (field (a (new pin% [name "a"] [owner this] [activates #t])))
    (field (b (new pin% [name "b"] [owner this] [activates #t])))
    (field (out (new pin% [name "out"] [owner this])))
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

(define 1gate%
  (class gate%
    (init name)
    (field (in (new pin% [name "in"] [owner this] [activates #t])))
    (field (out (new pin% [name "out"] [owner this])))
    (super-new [name name])))

(define not-bi%
  (class 1gate%
    (init name)
    (super-new [name name])
    (inherit-field in out)
    (define/override (eval)
      (let ([in (get-field value in)])
        (send out set (not in))))))

(define (internal-name obj owner) (format "~a[~a]" owner obj))

(define not%
  (class 1gate%
    (init name)
    (super-new [name name])
    (inherit-field in out)    
    (define nand (new nand% [name (internal-name "nand" name)]))
    (send in connect (get-field a nand))
    (send in connect (get-field b nand))
    (send (get-field out nand) connect out)))

(define and%
  (class 2gate%
    (init name)
    (super-new [name name])
    (inherit-field a b out)
    (define nand (new nand% [name (internal-name "nand" name)]))
    (define not (new not% [name (internal-name "not" name)]))
    (send a connect (get-field a nand))
    (send b connect (get-field b nand))
    (send (get-field out nand) connect (get-field in not))
    (send (get-field out not) connect out)))