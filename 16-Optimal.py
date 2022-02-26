class Solution:
    """
    THIS IS MY ORIGINAL SOLUTION
    """
    def BFS(self, grid, x, y, xlen, ylen):
        grid[x][y] = "0"
        if (y+1) < ylen and grid[x][y+1]=="1":
            self.BFS(grid, x, y+1, xlen, ylen)
        if (y-1) >= 0 and grid[x][y-1]=="1":
            self.BFS(grid, x, y-1, xlen, ylen)
        if (x-1) >= 0 and grid[x-1][y]=="1":
            self.BFS(grid, x-1, y, xlen, ylen)
        if (x+1) < xlen and grid[x+1][y]=="1":
            self.BFS(grid, x+1, y, xlen, ylen)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        xlen = len(grid)
        ylen = len(grid[0])
        
        count = 0
        for xx in range(xlen):
            for yy in range(ylen):
                if grid[xx][yy]=="1":
                    self.BFS(grid, xx, yy, xlen, ylen)
                    count += 1
        
        return count