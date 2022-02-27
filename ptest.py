import trueskill_cpp
from pprint import pprint
from timeit import timeit

players = []
for i in range(2):
    players.append((25., 25./3., i+1))

def test():
    return trueskill_cpp.adjust_players(players)

ITER = 1000000
print('{} iterations in {}s'.format(ITER, timeit(test, number=ITER)))

pprint(test())
