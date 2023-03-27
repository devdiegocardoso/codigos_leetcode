from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None

        v1 = 0 if not root1 else root1.val
        v2 = 0 if not root2 else root2.val

        root3 = TreeNode(v1+v2)

        root3.left = self.mergeTrees(root1.left if root1 else None,root2.left if root2 else None)
        root3.right = self.mergeTrees(root1.right if root1 else None,root2.right if root2 else None)

        return root3

def print_tree(root):
    q = [root]
    t = []
    while q:
        n = q.pop(0)
        t.append(n.val)
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)
    r = ','.join(map(str,t))
    print(f'[{r}]')

root1 = TreeNode(1,TreeNode(3,TreeNode(5)),TreeNode(2))
print_tree(root1)

root2 = TreeNode(2,TreeNode(1,None,TreeNode(4)),TreeNode(3,None,TreeNode(7)))
print_tree(root2)

print_tree(Solution().mergeTrees(root1,root2))