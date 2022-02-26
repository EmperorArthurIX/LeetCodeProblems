"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
N = (-1, 0)
E = (0, 1)
W = (0, -1)
S = (1, 0)

dirs = (N,E,W,S)

class Solution:
    """
    I FOUND THIS SOLUTION ONLINE. MY SOLUTION IS IN `16-Optimal.py`
    """
    def withinBounds(self, row, col):
        return (0 <= row < self.rows) and (0 <= col < self.cols)
    
    def isLand(self, row, col):
        return self.grid[row][col] == "1"
    
    def BFS(self, row, col):
        self.q.append((row,col))
        while self.q:
            row,col = self.q.pop(0)
            for dr, dc in dirs:
                r = row + dr
                c = col + dc
                if not self.withinBounds(r, c):
                    continue
                if self.isLand(r,c) and ((r,c) not in self.vis):
                    self.q.append((r,c))
                    print(*self.q)
                    self.vis.add((r,c))
            
    def numIslands(self, grid: List[List[str]]) -> int:
        if not len(grid):
            return -1
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.grid = grid
        self.q = []
        self.vis = set()
        islands = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if (not self.isLand(row,col)) or (row,col) in self.vis:
                    continue
                self.BFS(row, col)
                islands += 1
        return islands