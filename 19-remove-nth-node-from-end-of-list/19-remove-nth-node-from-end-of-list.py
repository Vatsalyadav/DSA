# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 0
        curr = dummy = ans = ListNode()
        while head:
            curr.next = head
            curr = curr.next
            head = head.next
            count+=1
        point = 0
        
        while dummy:
            if point == count-n:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next
            point+=1
        return ans.next