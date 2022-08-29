# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        walk = head
        run = head
        
        while run and run.next:
            walk = walk.next
            run = run.next.next
            if walk == run:
                return True
        return False