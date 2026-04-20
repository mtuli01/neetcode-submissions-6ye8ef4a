class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        num_set = set(nums)
        res = 1
        for num in nums:
            length = 1
            if num - 1 in num_set:
                curr = num - 1
                while  curr in num_set:
                    curr -= 1
                    length += 1
            res = max(res, length)
        return res