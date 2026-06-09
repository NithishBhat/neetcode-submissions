# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        def invert(parent):
            temp=None
            if parent==None:
                return 0
            else:
                temp=parent.left
                parent.left=parent.right
                parent.right=temp
            invert(parent.left)
            invert(parent.right)
            
        invert(root)
        return root