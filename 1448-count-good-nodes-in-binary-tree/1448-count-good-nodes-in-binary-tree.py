# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root, maxTillNow = float("-inf")):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root is None:
            return 0
        maxTillNow = max(maxTillNow, root.val)
        
        return (root.val == maxTillNow) + self.goodNodes(root.left, maxTillNow) + self.goodNodes(root.right, maxTillNow)