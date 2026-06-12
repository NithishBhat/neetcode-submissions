# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0

        queue=[]
        nxtQueue=[]
        depth=0
        queue.append(root)
        while queue:
            for node in queue:
                if node.left!=None:
                    nxtQueue.append(node.left)
                if node.right!=None:
                    nxtQueue.append(node.right)
            queue=nxtQueue
            depth=depth+1
            nxtQueue=[]
        return depth
