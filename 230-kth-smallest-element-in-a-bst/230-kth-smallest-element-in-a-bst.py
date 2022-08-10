# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        return self.inorderTraversal(root, [], k)[k-1]
        
    def inorderTraversal(self, root, array, k):
        if len(array) == k:
            return array
        if root is not None:
            self.inorderTraversal(root.left, array, k)
            array.append(root.val)
            self.inorderTraversal(root.right, array, k)
        return array