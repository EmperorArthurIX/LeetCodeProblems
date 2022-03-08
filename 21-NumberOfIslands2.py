N = (-1, 0)
E = (0, 1)
W = (0, -1)
S = (1, 0)

dirs = (N,E,W,S)

class Solution:
    def withinBounds(self, row, col):
        return (0 <= row < self.rows) and (0 <= col < self.cols)
    
    def isLand(self, row, col):
        return self.grid[row][col] == "1"
    
    def DFS(self, row, col):
        self.vis.add((row,col))
        for dr, dc in dirs:     # Notice here we are not BFSing by simply adding neighbours to queue.
            r = row + dr
            c = col + dc
            if self.withinBounds(r,c) and self.isLand(r,c) and (r,c) not in self.vis:
                self.DFS(r,c)   # We are adding neighbours of neighbours until we have no valid neighbours
                    
    def numIslands(self, grid) -> int:
        if not len(grid):
            return -1
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.grid = grid
        self.vis = set()                        # Notice we have not made stack. We are using system stack
        islands = 0
        for row in range(self.rows):            # This part is similar to the BFS method
            for col in range(self.cols):
                if self.isLand(row,col) and (row,col) not in self.vis:
                    islands += 1
                    self.DFS(row, col)
        return islands
