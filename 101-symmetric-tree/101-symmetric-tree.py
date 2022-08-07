# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isSymmetricHelper(root.left, root.right)
    
    def isSymmetricHelper(self, p, q):
        
        if p!= None and q!= None:
            if p.val != q.val:
                return False
            return self.isSymmetricHelper(p.left, q.right) and self.isSymmetricHelper(p.right, q.left)
        else:
            return p == q