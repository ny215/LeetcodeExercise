
import heapq
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        #use two heap.
        #smaller part: maxHeap, larger part: minHeap
        self.maxHeap = []
        self.minHeap = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        #push the largest element in the maxHeap into minHeap.
        heapq.heappush(self.maxHeap, -num)
        heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        #if minHeap is larger, then pop one from minHeap and push back to maxHeap
        if len(self.maxHeap) < len(self.minHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))


    def findMedian(self):
        """
        :rtype: float
        """
        #if the # is odd: pop the largest one in maxHeap. else: get mean of two elements
        if len(self.maxHeap) > len(self.minHeap):
            return float(-self.maxHeap[0])
        return ((-self.maxHeap[0] + self.minHeap[0])* 1.0 / 2)



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()