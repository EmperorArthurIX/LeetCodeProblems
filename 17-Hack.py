from collections import deque

def openLock(self, deadends: List[str], target: str) -> int:
    
    dead=set(deadends)
    def neighbor(code):
        for i in range(4):
            digit=int(code[i])
            for j in (-1,1):
                next_digit=(digit+j)%10
                yield code[:i]+str(next_digit)+code[i+1:]
                        
    q=deque([('0000',0)])
    vis={'0000'}
    while q:
        code, step=q.popleft()
        if code == target: return step
        if code not in dead:
            for nei in neighbor(code):
                if nei not in vis and nei not in dead:
                    q.append((nei,step+1))
                    vis.add((nei))
    return -1