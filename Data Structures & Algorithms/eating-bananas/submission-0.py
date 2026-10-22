class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # slowest, fastest = 1, max(piles)
        l, r = 1, max(piles)
        res = r

        while l <= r: 
            m = (l + r) // 2
            total = 0

            for p in piles: 
                total += math.ceil(p / m)

            if total > h: # increase eating speed
                l = m + 1
            else: # record, and see if can eat slower
                res = min(res, m)
                r = m - 1

        return res