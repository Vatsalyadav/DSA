# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        arr = []
        while head is not None:
            arr.append(head.val)
            head = head.next
        
        cur = ans = ListNode()
        for i in range(len(arr)-1, -1, -1):
            cur.next = ListNode(arr[i])
            cur = cur.next
        return ans.next
    