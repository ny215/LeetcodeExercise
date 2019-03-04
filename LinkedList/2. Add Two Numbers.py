# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummy = res = ListNode(0)
        while l1 or l2 or carry:
            val1 = val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            val = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) / 10
            res.next = ListNode(val)
            res = res.next
        return dummy.next
#time:  O(max(m,n))
#space:  O(max(m,n)) + 1