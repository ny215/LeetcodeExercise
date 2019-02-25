# NlogN use sort
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        return sorted(points, key = lambda x:x[0]**2 + x[1]**2)[:K]



# NlogK use heap
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        return heapq.nsmallest(K ,points , key = lambda x:x[0]**2 + x[1]**2)


# N divide and qonquer
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        dist = lambda i: points[i][0]**2 + points[i][1]**2

        

    
        def partition(i,j, points):
            oi = i
            pivot = dist(i)
            i+= 1
            while True:
                while i < j and dist(i) < pivot:
                    i += 1
                while i <= j and dist(j) >= pivot:
                    j -= 1
                if i >= j:
                    break
                points[i], points[j] = points[j], points[i]    

            points[oi], points[j] = points[j], points[oi]
            return j  
    
        def sort(i, j, K, points):
            if i >= j:
                return
            k = random.randint(i, j)
            points[i], points[k] = points[k], points[i]
            mid = partition(i, j, points)
            if K < mid - i + 1:
                sort(i, mid - 1, K, points)
            elif K > mid - i + 1:
                sort(mid + 1, j, K - (mid - i + 1), points)
        
        sort(0, len(points) - 1, K,points)
        return points[:K]


