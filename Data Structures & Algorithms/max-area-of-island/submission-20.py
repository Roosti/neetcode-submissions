class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        res = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            area = 1

            while q:
                row, col = q.popleft()
                directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == 1 and
                        (r, c) not in visited):
                        area += 1
                        visited.add((r, c))
                        q.append((r, c))
            return area

        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == 1) and ((r, c) not in visited):
                    res = max(res, bfs(r, c))
        return res