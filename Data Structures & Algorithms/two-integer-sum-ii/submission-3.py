class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        right = 1
        while left <= len(numbers) - 2 and left < right:
            while right <= len(numbers) - 1 and numbers[right] <= target - numbers[left]:
                if numbers[right] == target - numbers[left]:
                    return [left + 1, right + 1]
                elif numbers[right] > target - numbers[left]:
                    break
                else:
                    right += 1
            left += 1
            right = left + 1