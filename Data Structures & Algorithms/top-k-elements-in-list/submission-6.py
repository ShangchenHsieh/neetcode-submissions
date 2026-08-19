class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int) 
        for n in nums: 
            frequencies[n] += 1
        
        temp = sorted(frequencies, key=frequencies.get)
        return temp[-k:]