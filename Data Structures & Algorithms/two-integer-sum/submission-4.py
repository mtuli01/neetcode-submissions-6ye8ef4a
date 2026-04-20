class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_set = {}
        for i, num in enumerate(nums):
            if target - num in map_set:
                return [map_set[target-num], i]
            map_set[num] = i