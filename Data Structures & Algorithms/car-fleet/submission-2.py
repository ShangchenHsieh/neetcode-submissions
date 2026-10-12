class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s = [] # (position, speed, arriving in)

        for i in range(len(position)): 
            s.append((position[i], speed[i], (target - position[i]) / speed[i]))
        
        res = 0 
        s.sort()
        while s: 
            temp = s.pop() # (pos, speed, arriving)
            while s and s[-1][2] <= temp[2]: 
                s.pop()
            res += 1
        return res