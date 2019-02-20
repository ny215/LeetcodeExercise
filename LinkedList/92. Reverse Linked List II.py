# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        dummy = prev = ListNode(0)
        dummy.next = head
        for i in range(m-1):
            prev = prev.next
        curr = prev.next
        #reverse
        node = None
        for i in range(n-m+1):
            nxt = curr.next
            curr.next = node
            node = curr
            curr = nxt
        prev.next.next = curr
        prev.next = node
        return dummy.next
            
         
                
        