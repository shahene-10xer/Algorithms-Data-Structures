class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # input validation
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        island_number = 0
        
        def bfs(r, c):
            queue = collections.deque()
            visited.add((r, c))
            queue.append((r, c))
            
            while queue:
                row, col = queue.pop()
                directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
                
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols) and (r, c) not in visited and grid[r][c] == "1"):
                        queue.append((r, c))
                        visited.add((r, c))
                        
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    island_number += 1
        return island_number
    
    
        
        