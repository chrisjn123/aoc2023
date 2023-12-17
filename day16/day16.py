from collections import deque
from utils import get_data
from time import perf_counter
from concurrent.futures import ThreadPoolExecutor
from functools import cache

GRID = get_data('in.txt')

@cache
def DFS(i, j, di, dj):
    global GRID
    n, m = len(GRID), len(GRID[0])
    q = deque([(i, j, di, dj)])
    seen = set()
    while q:
        i, j, di, dj = q.popleft()
        if 0 > i or i >= n or 0 > j or j >= m or (i, j, di, dj) in seen:
            continue
        seen.add((i, j, di, dj))
        match GRID[i][j]:
            case "/":
                q.append((i - dj, j - di, -dj, -di))
            case "\\":
                q.append((i + dj, j + di, dj, di))
            case "|" if dj:
                q.append((i + 1, j, 1, 0))
                q.append((i - 1, j, -1, 0))
            case "-" if di:
                q.append((i, j + 1, 0, 1))
                q.append((i, j - 1, 0, -1))
            case _:
                q.append((i + di, j + dj, di, dj))
    return len(set((i, j) for i, j, _, _ in seen))

def part_one():
    return DFS(0, 0, 0, 1)

def part_two():
    n, m = len(GRID), len(GRID[0])
    res = 0
    for i, j, di, dj in (
        [(x, 0, 0, 1) for x in range(n)]
        + [(x, m - 1, 0, -1) for x in range(n)]
        + [(0, x, 1, 0) for x in range(m)]
        + [(n - 1, x, -1, 0) for x in range(m)]
    ):
        res = max(res, DFS(i, j, di, dj))
    return res

def part_two_threads():
    res = []
    with ThreadPoolExecutor(max_workers=12) as pool:
        n, m = len(GRID), len(GRID[0])
        for i, j, di, dj in (
            [(x, 0, 0, 1) for x in range(n)]
            + [(x, m - 1, 0, -1) for x in range(n)]
            + [(0, x, 1, 0) for x in range(m)]
            + [(n - 1, x, -1, 0) for x in range(m)]
        ):
            res.append(pool.submit(DFS, i, j, di, dj).result())
    return max(res)

start = perf_counter()
print(f"Part 1     : {part_one()}")
print(f'Part 1 time: {perf_counter() - start} sec')
print()

start = perf_counter()
print(f"Part 2     : {part_two()}")
print(f'Part 2 time: {perf_counter() - start} sec')

start = perf_counter()
print(f"Part 2 Tread: {part_two_threads()}")
print(f'Part 2 time : {perf_counter() - start} sec')