# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        min_heap = []
        self.dfs(root, min_heap)
        for _ in range(k):
            kth_smallest = heapq.heappop(min_heap)
        return kth_smallest
    
    def dfs(self, node, min_h):
        # left, cur, right
        if not node:
            return 
        if node.left:
            self.dfs(node.left, min_h)
        heapq.heappush(min_h, node.val)
        if node.right:
            self.dfs(node.right, min_h)
        