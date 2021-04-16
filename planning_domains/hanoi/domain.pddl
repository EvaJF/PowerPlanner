(define (domain hanoi_towers)
  (:requirements :strips )
  (:predicates (clear ?x) (on ?x ?y) (smaller ?x ?y) )
  (:action move
    :parameters (?disc ?from ?to)
    :precondition (and
       (smaller ?disc ?to) (smaller ?disc ?from)
       (on ?disc ?from)
       (clear ?disc) (clear ?to)
       (not (equal ?from ?to))
    )
    :effect (and
      (clear ?from)
      (on ?disc ?to)
      (not (on ?disc ?from))
      (not (clear ?to))
    )
  )
)
