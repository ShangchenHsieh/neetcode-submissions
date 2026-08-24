class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        bucket = [[] for _ in range(len(nums)+1)]

        for n in nums: 
            counter[n] += 1

        for key, val in counter.items(): 
            bucket[val].append(key)

        res = []
        bucket.reverse()
        for i in range(0, len(bucket)+1): 
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res