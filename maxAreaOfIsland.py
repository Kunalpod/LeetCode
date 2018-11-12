# https://leetcode.com/problems/max-area-of-island/

def get_neighbors(grid, n, m, visited, i, j):
    count = 0
    unvisited= [(i, j)]
    while(unvisited):
        x,y = unvisited.pop()
        if visited[x][y]: continue
        visited[x][y] = True
        count += 1
        if x > 0 and not visited[x - 1][y] and grid[x - 1][y] == 1: unvisited += [(x - 1, y)]
        if y > 0 and not visited[x][y - 1] and grid[x][y - 1] == 1: unvisited += [(x, y - 1)]
        if x < n - 1 and not visited[x + 1][y] and grid[x + 1][y] == 1: unvisited += [(x + 1, y)]
        if y < m - 1 and not visited[x][y + 1] and grid[x][y + 1] == 1: unvisited += [(x, y + 1)]
    return count, visited

def maxAreaOfIsland(grid):
    n = len(grid)
    m = 0
    if n != 0: m = len(grid[0])
    count = 0
    visited = [[False for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] == 1:
                c, visited = get_neighbors(grid, n, m, visited, i, j)
                count = max(count, c)
    return count
