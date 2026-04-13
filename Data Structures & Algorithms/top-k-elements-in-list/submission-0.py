class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elem_fq = {}
        for num in nums:
            if num in elem_fq:
                elem_fq[num] += 1
            else: 
                elem_fq[num] = 1
        sorted_elem_fq = {k: v for k, v in sorted(elem_fq.items(), key=lambda x: x[1], reverse=True)}
        return list(sorted_elem_fq.keys())[:k]