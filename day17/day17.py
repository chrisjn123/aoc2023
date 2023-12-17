from heapq import heappush, heappop
from utils import get_data

GRID = get_data('in.txt')
def get_near(state):
    global GRID
    x,y,dx,dy,v = state
    left,right = (-dy,dx),(dy,-dx)
    if v < 10 and 0<=x+dx<len(GRID) and 0<=y+dy<len(GRID[0]):
        yield (x+dx,y+dy,dx,dy,v+1), int(GRID[x+dx][y+dy])
    for dx,dy in left,right:
        if 0<=x+dx<len(GRID) and 0<=y+dy<len(GRID[0]) and v > 3:
            yield (x+dx,y+dy,dx,dy,1), int(GRID[x+dx][y+dy])

def search():
    ''' Uses a heapq which is a priority q.
    The first element is the cost of a state (sum of prev).
    Seond is the state itself. '''
    global GRID
    q = [(0, (0, 0, 0, 1, 0)),
         (0, (0, 0, 1, 0, 0))]
    seen = set()
    losses = {(0, 0, 0, 1, 0): 0, 
              (0, 0, 1, 0, 0): 0}

    while len(q):
        _, (i, j, di, dj, dc) = heappop(q)
        end = (len(GRID)-1, len(GRID[0])-1)

        # If out of range or already been here
        if 0 > i or i >= len(GRID) or 0 > j or j >= len(GRID[0]) or (i, j, di, dj, dc) in seen:
            continue
            
        seen.add((i, j, di, dj, dc))
        # If at the end, set end to curr state and quit search
        # AND  count in direction is >3 
        if (i,j) == end and dc > 3:
            end = (i, j, di, dj, dc)
            break 
        for neigh_state, cost in get_near((i, j, di, dj, dc)):
            if neigh_state in seen:
                continue
            cost_total = losses[(i, j, di, dj, dc)] + cost
            if neigh_state not in losses:
                losses[neigh_state] = cost_total
                heappush(q, (cost_total, neigh_state))

    return losses[end]

print(search())