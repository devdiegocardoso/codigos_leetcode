# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        q = [root]
        while q:
            for i in range(len(q)-1):
                q[i].next = q[i+1]
            q = [c for n in q for c in (n.left,n.right) if c]
        
        return root



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

root1 = Node(1,Node(2,Node(4),Node(5)),Node(3,Node(6),Node(7)))
#print_tree(root1)

rootR = Solution().connect(root1)
print_tree(rootR)