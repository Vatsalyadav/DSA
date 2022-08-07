# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum, currentSum = None, isLeafNode = True):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return currentSum == targetSum and isLeafNode
        if currentSum is None:
            currentSum = 0
        currentSum += root.val
        
        isLeafNode = root.left is None and root.right is None
        return self.hasPathSum(root.left, targetSum, currentSum, isLeafNode) or self.hasPathSum(root.right, targetSum, currentSum, isLeafNode)
        
                
        