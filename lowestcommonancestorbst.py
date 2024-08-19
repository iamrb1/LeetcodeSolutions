class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode):
    cur = root
    while cur:
        if p.val > cur.val and q.val > cur.val:
            cur = cur.right
        elif p.val < cur.val and q.val < cur.val:
            cur = cur.left
        else:
            return cur

if __name__ == '__main__':
    p = TreeNode(3, TreeNode(1, None, TreeNode(2)))
    q = TreeNode(8, TreeNode(7), TreeNode(9))
    root = TreeNode(5, TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4)), TreeNode(8, TreeNode(7), TreeNode(9)))
    print(lowestCommonAncestor(root, p, q))
