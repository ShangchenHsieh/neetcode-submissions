class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for n in nums: 
            dic[n] += 1
        
        aar = []
        for key, val in dic.items(): 
            aar.append((val, key))
        aar.sort()
        res = []
        while len(res) < k: 
            res.append(aar.pop()[1])
        return res

