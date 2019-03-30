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


#divide and conquer
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge(lists[i], lists[i + interval])
            interval *= 2
        return lists[0]
        
    def merge(self, l1, l2):
        head = dummy = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        if l1:
            head.next = l1
        elif l2:
            head.next = l2
        return dummy.next
# time: O(NlogK)
# space: O(1)            