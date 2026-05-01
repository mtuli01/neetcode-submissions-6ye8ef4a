class Solution:
    def trap(self, height: List[int]) -> int:
        dp = [0] * len(height)
        left_max = 0
        for i in range(len(height)):
            if height[i] > left_max:
                dp[i] = left_max
                left_max = height[i]
            else:
                dp[i] = left_max
        right_max = 0
        for i in range(len(height)-1, -1, -1):
            if height[i] > right_max:
                dp[i] = max(min(height[i], dp[i]) - height[i], 0)
                right_max = height[i]
            else:
                dp[i] = max(min(dp[i], right_max) - height[i], 0)
        return sum(dp)