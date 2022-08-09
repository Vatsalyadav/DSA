# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root, depth = 0, isLeafNode = True):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root is None:
            if isLeafNode:
                return depth
            else:
                return float("inf")
        isLeafNode = True if root.left is None and root.right is None else False
        return min(self.minDepth(root.left, depth+1, isLeafNode), self.minDepth(root.right, depth+1,isLeafNode))