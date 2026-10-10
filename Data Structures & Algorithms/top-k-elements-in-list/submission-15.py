class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        freq_bucket = [[] for _ in range(len(nums) + 1)]

        for n in nums: 
            map[n] = 1 + map.get(n, 0)
        for key, val in map.items(): 
            freq_bucket[val].append(key)
        res = []
        for i in range(len(freq_bucket) - 1, 0, -1): 
            for n in freq_bucket[i]: 
                res.append(n)
                if len(res) == k: 
                    return res

        