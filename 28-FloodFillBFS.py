N = (1,0)
E = (0,1)
W = (0,-1)
S = (-1,0)
DIRS = (N,E,W,S)

class Solution:
    
    def withinBounds(self, row, col):
        return bool(0 <= row < self.rows and 0 <= col < self.cols)
    
    def isSameColor(self, row, col):
        return bool(self.img[row][col] == self.clr)
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.img = image
        self.rows = len(image)
        self.cols = len(image[0])
        self.clr = image[sr][sc]
        self.vis = set()
        self.q = []
        
        self.q.append((sr, sc))
        self.vis.add((sr, sc))
        while self.q:
            row, col = self.q.pop()
            self.img[row][col] = newColor
            for dr, dc in DIRS:
                r = row + dr
                c = col + dc
                if self.withinBounds(r,c) and self.isSameColor(r,c) and (r,c) not in self.vis:
                    self.q.append((r,c))
                    self.vis.add((r,c))
                print(self.q)
        return self.img