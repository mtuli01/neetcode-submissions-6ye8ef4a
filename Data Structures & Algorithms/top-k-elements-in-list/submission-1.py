class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq

        freq = Counter(nums)
        heap = []
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for count, num in heap]
        # elem_fq = {}
        # for num in nums:
        #     if num in elem_fq:
        #         elem_fq[num] += 1
        #     else: 
        #         elem_fq[num] = 1
        # sorted_elem_fq = {k: v for k, v in sorted(elem_fq.items(), key=lambda x: x[1], reverse=True)}
        # return list(sorted_elem_fq.keys())[:k]