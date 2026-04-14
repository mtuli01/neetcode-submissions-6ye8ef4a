class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) < 2: return nums
        left_product = 1
        right_product = 1
        res = [1] * len(nums)
        for i in range(0, len(nums)):
            res[i] = right_product
            right_product *= nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            res[i] *= left_product
            left_product *= nums[i]
        return res