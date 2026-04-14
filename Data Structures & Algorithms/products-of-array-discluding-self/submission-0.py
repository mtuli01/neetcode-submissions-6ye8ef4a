class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) < 2: return nums
        right_product = [1] * len(nums)
        left_product = [1] * len(nums)

        right_product[0] = nums[0]
        left_product[-1] = nums[-1]
        for i in range(1, len(nums)):
            right_product[i] = right_product[i-1] * nums[i]
        
        for i in range(len(nums) - 2, -1, -1):
            left_product[i] = left_product[i+1] * nums[i]

        res = [1] * len(nums)
        for i in range(0, len(nums)):
            if i == 0:
                res[i] = left_product[i+1]
            elif i == len(nums) - 1:
                res[i] = right_product[i-1]
            else:
                res[i] = right_product[i-1] * left_product[i+1]
        return res