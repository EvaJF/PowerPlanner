(define (problem tartiflette) (:domain recipies)
(:objects 
    potatoe cheese bacon onion salad - ingredient
    pan1 pan2 - cooker
)

(:init
    (is_clean pan1)
    (free pan1)
    (free pan2)
    (free potatoe)
    (free cheese)
    (free bacon)
    (free onion)
    (free salad)
    
)

(:goal (and
    (cooked potatoe)
    (cooked cheese)
    (cooked bacon)
    (cooked onion)
    (not (cooked salad))
    (is_clean pan1)
    (is_clean pan2)
))
)