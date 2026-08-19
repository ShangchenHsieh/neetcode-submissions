class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs: 
            sorted_string = "".join(sorted(s))
            ans[sorted_string].append(s)
        print(ans)
        return list(ans.values())
