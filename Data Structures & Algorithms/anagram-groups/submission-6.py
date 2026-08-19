class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) 

        for s in strs: 
            to_string = ''.join(sorted(s))
            res[to_string].append(s)

        return list(res.values())