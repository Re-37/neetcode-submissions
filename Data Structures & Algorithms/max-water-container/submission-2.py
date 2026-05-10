class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_size = 0
        size = 0 
        l, r = 0, len(heights) - 1

        while l < r:
            size = (r - l) * min(heights[l], heights[r])
            max_size = max(max_size, size)

            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
    
        return max_size



