# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if subRoot is None:
            return True
        if root is None:
            return False
        if subRoot.val == root.val and self.checkSubtree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
    def checkSubtree(self, root, subRoot):
        if root is not None and subRoot is not None:
            if root.val != subRoot.val:
                return False
            return self.checkSubtree(root.left, subRoot.left) and self.checkSubtree(root.right, subRoot.right)
        else:
            return root == subRoot
            