(define (problem steakfries) (:domain recipies)
(:objects 
    beef potatoe ketchup salad - ingredient
    pan1 pan2 pan3 - cooker
)

(:init
    (is_clean pan1)
    (free pan1)
    (free pan2)
    (free pan3)
    (free beef)
    (free potatoe)
    (free ketchup)
    (free salad)
    
)

(:goal (and
    (cooked potatoe)
    (cooked beef)
    (not (cooked salad))
    (not (cooked ketchup))
    (is_clean pan1)
    (is_clean pan2)
))
)