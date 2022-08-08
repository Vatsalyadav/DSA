# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        maxTree = self.createMaxTree(root)
        return self.inorderTravers(maxTree)
    
    def createMaxTree(self, root, rev = None):
        if root is None:
            return None
        rev = TreeNode([root.val,root.val])
        rev.right = self.createMaxTree(root.right, rev.right)
        rev.left = self.createMaxTree(root.left, rev.left)
        left = rev.left if rev.left is not None else TreeNode([0,0])
        right = rev.right if rev.right is not None else TreeNode([0,0])
        
        rev.val = [max(rev.val[0], rev.val[0] + left.val[1] + right.val[1], rev.val[0] + left.val[1], rev.val[0] + right.val[1]),max(rev.val[0], rev.val[0] + left.val[1], rev.val[0] + right.val[1])]
        return rev
    
    def inorderTravers(self, maxTree, maxSum = float("-inf")):
        if maxTree is None:
            return None
        maxSum = max(maxTree.val)
        return max(maxSum, self.inorderTravers(maxTree.left, maxSum), self.inorderTravers(maxTree.right, maxSum))
        