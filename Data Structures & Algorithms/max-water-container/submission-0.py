class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        area_max = 0
        while i < j:
            area = (j - i) * min(heights[j], heights[i])
            area_max = max(area, area_max)
            if heights[i] <= heights[j]:
                i+=1
            else:
                j-=1
        return area_max