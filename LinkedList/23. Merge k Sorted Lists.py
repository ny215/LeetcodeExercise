# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        dummy = res = ListNode(0)
        tmp = PriorityQueue()
        for l in lists:
            if l:
                tmp.put((l.val,l))
        while not tmp.empty():
            val, node = tmp.get()
            res.next = ListNode(val)
            res = res.next
            node = node.next
            if node:
                tmp.put((node.val, node))
        return dummy.next

# time: O(NlogK)
# space: O(N)