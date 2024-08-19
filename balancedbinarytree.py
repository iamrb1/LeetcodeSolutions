# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root) -> bool:

        def dfs(root):
            if not root:
                return (True, 0)
            left, right = dfs(root.left), dfs(root.right)
            if left[0] and right[0]:
                if abs(left[1] - right[1]) <= 1:
                    balanced = True
                else:
                    balanced = False
            else:
                balanced = False
            return (balanced, 1 + max(left[1], right[1]))

        return dfs(root)[0]




