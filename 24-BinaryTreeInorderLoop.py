# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solve using Loop instead of Recursion

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        vis = set()
        final = []
        if not root:
            return
        stack.append(root)
        while stack:
            curr = stack[-1]
            while curr.left and curr.left not in vis:
                stack.append(curr.left)
                vis.add(curr.left)
                curr = curr.left
            final.append(stack.pop().val)
            if curr.right and curr.right not in vis:
                stack.append(curr.right)
                vis.add(curr.right)
        return final
            