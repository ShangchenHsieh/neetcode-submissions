class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums: 
            count[n] += 1
        res = []
        for key, val in count.items(): 
            res.append((key, val))
        res.sort(key=lambda x: x[1], reverse=True)
        return [res[i][0] for i in range(k)]