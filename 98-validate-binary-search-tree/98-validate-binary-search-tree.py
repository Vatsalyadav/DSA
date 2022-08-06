# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root, minValue = float("-inf"), maxValue = float("inf")):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if root.val <= minValue or root.val >= maxValue:
            return False
        return self.isValidBST(root.left, minValue, root.val) and self.isValidBST(root.right, root.val, maxValue)
            
        