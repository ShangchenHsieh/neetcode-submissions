class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = [] # (index, value)
        res = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures)): 

            while s and temperatures[i] > s[-1][1]: 
                temp = s.pop() 
                res[temp[0]] = i - temp[0]

            s.append((i, temperatures[i]))

        return res

            