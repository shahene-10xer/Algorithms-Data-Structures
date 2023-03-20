# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        queue = collections.deque()
        self.preorder(root, queue)
        if not queue: return
        
        prev = queue.popleft()
        for _ in range(len(queue)):
            prev.left = None
            if queue:
                n_prev = queue.popleft()
                prev.right = n_prev
                prev = n_prev
    
    def preorder(self, root, queue):
        if not root: return
        queue.append(root)
        if root.left:
            self.preorder(root.left, queue)
        if root.right:
            self.preorder(root.right, queue)
        