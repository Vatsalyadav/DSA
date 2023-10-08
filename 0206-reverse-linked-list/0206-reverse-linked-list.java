/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode rev = new ListNode();
        
        while(head!=null){
            rev.val = head.val;
            rev = new ListNode(0, rev);
            head= head.next;
        }
        return rev.next;
    }
}