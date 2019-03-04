# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next:
            return head
        dummy = head
        prev = None
        slow = fast = ListNode(-1)
        slow.next = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        con = slow
        front = slow.next
        end = fast.next
        while front:
            tmp = front 
            front = front.next
            tmp.next = prev
            prev = tmp
        con.next = prev
        return dummy
    