# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p!= None and q!=None:
            if p.val != q.val:
                print("here")
                return False
            return self.isSameTree(p.left, q.left) == True and self.isSameTree(p.right, q.right) == True
        else:
            if p!=None:
                return False
            elif q!=None:
                return False
            else:
                return True