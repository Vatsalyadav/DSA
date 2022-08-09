# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return 0 if root is None else self.findMinDepth(root)
        
        
    def findMinDepth(self, root, depth = 0, isLeafNode = False):
        if isLeafNode:
            return depth
        elif root is None:
            return float("inf")
        isLeafNode = True if root.left is None and root.right is None else False
        return min(self.findMinDepth(root.left, depth+1, isLeafNode), self.findMinDepth(root.right, depth+1,isLeafNode))