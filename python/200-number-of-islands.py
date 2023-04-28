def numIslands(self, grid: List[List[str]]) -> int:
    visited = set()
    islands = 0
    rows = range(len(grid))
    cols = range(len(grid[0]))

    def bfs(r, c):
        q = deque()
        visited.add((r, c))
        q.append((r, c))

        while q:
            row, col = q.popleft()
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dir_r, dir_c in directions:
                r, c = row + dir_r, col + dir_c
                if (r in rows 
                    and c in cols 
                    and (r, c) not in visited
                    and grid[r][c] == "1"
                ):
                    visited.add((r, c))
                    q.append((r, c))

    for r in rows:
        for c in cols:
            if grid[r][c] == "1" and (r, c) not in visited:
                bfs(r, c)
                islands += 1
    
    return islands