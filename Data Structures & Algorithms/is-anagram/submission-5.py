import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge case 
        if len(s) != len(t): 
            return False 
        else: 
            s_dic = collections.defaultdict(int) 
            t_dic = collections.defaultdict(int)
            for i in range(len(s)): 
                s_dic[s[i]] += 1
                t_dic[t[i]] += 1

        return s_dic == t_dic
