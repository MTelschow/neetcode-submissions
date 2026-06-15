class Solution:
    def checkEatingSpeed(self, piles: List[int], h: int, k: int) -> bool:
        time = 0
        for pile in piles:
            if pile == 0:
                continue
            if k == 0:
                return False
            time += math.ceil(pile / k)
        return time <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left_b = 0
        right_b = max(piles) 

        while left_b < right_b:
            middel = (left_b + right_b) // 2

            if self.checkEatingSpeed(piles, h, middel):
                right_b = middel
            else:
                left_b = middel + 1
        return left_b
        

        