(define (problem hanoi_pb4)
  (:domain hanoi_towers)
  (:objects peg1 peg2 peg3 d1 d2 d3 d4)
  (:init
    (smaller d1 peg1) (smaller d1 peg2) (smaller d1 peg3)
    (smaller d2 peg1) (smaller d2 peg2) (smaller d2 peg3)
    (smaller d3 peg1) (smaller d3 peg2) (smaller d3 peg3)
    (smaller d4 peg1) (smaller d4 peg2) (smaller d4 peg3)
    
    (smaller d1 d2) (smaller d1 d3) (smaller d1 d4)
    (smaller d2 d3) (smaller d2 d4)
    (smaller d3 d4)
    (clear d1) (clear peg2) (clear peg3)
    (on d1 d2) (on d2 d3) (on d3 d4) (on d4 peg1)
  )

  (:goal (and
    (on d1 d2) (on d2 d3) (on d3 d4) (on d4 peg3) (clear peg1) (clear peg2)
  ))
)