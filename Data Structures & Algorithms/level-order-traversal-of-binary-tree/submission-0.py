# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        cur_list=[root]
        nxt_list=[]
        output=[]
        temp=[]
        if root is None:
            return []
        while cur_list:
            for i in cur_list:
                if i.left is not None:
                    nxt_list.append(i.left)
                if i.right is not None:
                    nxt_list.append(i.right)
                temp.append(i.val)
            output.append(temp)
            cur_list=nxt_list
            nxt_list=[]
            temp=[]
        return output