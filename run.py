from parser import Domain
from planifier import AlphaStarPlannifier
from heuristic import Heuristic_HSP_Neg

if __name__ == '__main__':
    import sys
    domainfile = sys.argv[1]
    problemfile = sys.argv[2]

    domain = Domain(domainfile, problemfile)
    
    hsp = Heuristic_HSP_Neg(domain=domain)
    planif = AlphaStarPlannifier(domain=domain, heuristic_fn=hsp.heuristic_hsp)
    plan = planif.solve()
    print('*** PLAN ***')
    print(' ' + '\n '.join(list(map(str,plan))))