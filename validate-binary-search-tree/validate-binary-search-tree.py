# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, left_b = -math.inf, right_b = math.inf):
            if not node:
                return True
            
            if node.val <= left_b or node.val >= right_b:
                return False
            
            return validate(node.left, left_b, node.val) and validate(node.right, node.val, right_b)
        
        return validate(root)
    

        
        