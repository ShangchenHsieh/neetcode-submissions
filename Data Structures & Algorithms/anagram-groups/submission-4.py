class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs: 
            sorted_s = ''.join(sorted(s))
            ans[sorted_s].append(s)

        return list(ans.values()) 