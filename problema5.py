# Problema 5 – A* (10p)
# a) Explicați algoritmul A* în comentarii
# b) Implementați A* pe un grid 3x3 cu obstacol în centru

from heapq import heappush, heappop


# Nu am avut timp sa invat astar



Grid = list[list[int]]

def heuristic(a, b):
    (x1, y1), (x2, y2) = a, b
    return abs(x1 - x2) + abs(y1 - y2)

def astar(grid: Grid, start: tuple[int,int], goal: tuple[int,int]):
    # TODO
    return []

if __name__ == "__main__":
    grid = [
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]
    print(astar(grid, (0,0), (2,2)))


