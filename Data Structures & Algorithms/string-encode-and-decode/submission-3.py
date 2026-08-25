class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs: 
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        return ''.join(res)
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 
        while i < len(s): 
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j]) # slicing because the length of the string can be more than 1 digit long
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res