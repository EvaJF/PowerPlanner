(define (problem reves_puzzle_6)
  (:domain hanoi_towers)
  (:objects peg1 peg2 peg3 peg4 peg5 peg6 d1 d2 d3 d4 d5 d6)
  (:init
    (smaller d1 peg1) (smaller d1 peg2) (smaller d1 peg3) (smaller d1 peg4) (smaller d1 peg5) (smaller d1 peg6)
    (smaller d2 peg1) (smaller d2 peg2) (smaller d2 peg3) (smaller d2 peg4) (smaller d2 peg5) (smaller d2 peg6)
    (smaller d3 peg1) (smaller d3 peg2) (smaller d3 peg3) (smaller d3 peg4) (smaller d3 peg5) (smaller d3 peg6)
    (smaller d4 peg1) (smaller d4 peg2) (smaller d4 peg3) (smaller d4 peg4) (smaller d4 peg5) (smaller d4 peg6)
    (smaller d5 peg1) (smaller d5 peg2) (smaller d5 peg3) (smaller d5 peg4) (smaller d5 peg5) (smaller d5 peg6)
    (smaller d6 peg1) (smaller d6 peg2) (smaller d6 peg3) (smaller d6 peg4) (smaller d6 peg5) (smaller d6 peg6)
    
    (smaller d1 d2) (smaller d1 d3) (smaller d1 d4) (smaller d1 d5) (smaller d1 d6)
    (smaller d2 d3) (smaller d2 d4) (smaller d2 d5) (smaller d2 d6)
    (smaller d3 d4) (smaller d3 d5) (smaller d3 d6)
    (smaller d4 d5) (smaller d4 d6)
    (smaller d5 d6)
    
    (clear d1) (clear peg2) (clear peg3) (clear peg4) (clear peg5) (clear peg6)
    (on d1 d2) (on d2 d3) (on d3 d4) (on d4 d5) (on d5 d6) (on d6 peg1)
  )

  (:goal (and
    (on d1 d2) (on d2 d3) (on d3 d4) (on d4 d5) (on d5 d6) (on d6 peg6) (clear peg1) (clear peg2) (clear peg3) (clear peg4) (clear peg5)
  ))
)