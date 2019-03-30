class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        area = 0
        maxleft = 0
        maxright = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] < maxleft:
                    area += maxleft - height[left]
                else:
                    maxleft = height[left]
                left += 1
            else:
                if height[right] < maxright:
                    area += maxright - height[right]
                else:
                    maxright = height[right]
                right -= 1
        return area
#O(n)
#O(1)
#two pointers, depends on the smaller side. (maxOfSide - curr)