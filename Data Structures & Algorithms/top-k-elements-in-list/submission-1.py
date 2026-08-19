class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int) 
        for n in nums: 
            dic[n] += 1
        arr = []
        for key, val in dic.items(): 
            arr.append((val, key))
        arr.sort()
        res = []
        for i in range(k): 
            res.append(arr.pop()[1])

        return res