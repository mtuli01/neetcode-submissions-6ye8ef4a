class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_set:
                return [num_set[diff], i]
            num_set[num] = i