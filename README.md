# PowerPlanner

This repository contains our project with 2 original instances written in PDDL format and our own planner.

__Domain__

We have taken the use cas of cooking to write an original PDDL domain with 2 problem files featuring the recipies of French tartiflette and good ol steak & fries. You can find these files under `domain_recipies.pddl`, `pb_tartiflette.pddl`, `pb_steackfries.pddl`. 

__Parsing__

To parse the pddl files, we have adapted the `PDDL.py` script from this [this GitHub repository](https://github.com/pucrs-automated-planning/pddl-parser).

We also use our own intermediary __parser.py__ script to define useful classes which will be fed to the planner.

__Planner__

Our planner can be found under `planifer.py`and calls heuristics from `heuristics.py`.
