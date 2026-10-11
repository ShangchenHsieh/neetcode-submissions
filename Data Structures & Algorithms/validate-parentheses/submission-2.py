class Solution:
    def isValid(self, s: str) -> bool:
        mem = []

        for par in s: 
            if par == "(":
                mem.append(par)
            elif par == "[":
                mem.append(par)
            elif par == "{":
                mem.append(par)
            elif par == ")":
                if len(mem) != 0 and mem.pop() == "(": 
                    continue
                else: 
                    return False
            elif par == "]":
                if len(mem) != 0 and mem.pop() == "[": 
                    continue
                else: 
                    return False
            else: # }
                if len(mem) != 0 and mem.pop() == "{": 
                    continue
                else: 
                    return False

        return len(mem) == 0