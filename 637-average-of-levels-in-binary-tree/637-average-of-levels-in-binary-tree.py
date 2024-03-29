# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        res = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            currSum = 0
            levelLen = len(queue)
            for i in range(len(queue)):
                node = queue.popleft()
                currSum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(currSum/float(levelLen))
        return res