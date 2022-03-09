# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return
        if not node.neighbors:
            return Node(node.val, node.neighbors)
        visited = {}

        def dfs(node, visited):
            clone = Node(node.val)
            visited[node.val] = clone
            for n in node.neighbors:
                if not visited.get(n.val):
                    dfs(n, visited)
                clone.neighbors.append(visited.get(n.val))
            return clone
        
        return dfs(node, visited)