# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root, rev = None):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        rev = TreeNode(root.val)
        rev.left = self.invertTree(root.right, rev.right)
        rev.right = self.invertTree(root.left, rev.left)
        return rev
        
        