# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        prev = ListNode(0)
        dummy = prev  #dummy:steady node
        dummy.next = head
        while head and head.next:
            prev.next = head.next
            tmp = head.next.next
            head.next = tmp
            prev.next.next = head
            prev = head
            head = head.next
        return dummy.next