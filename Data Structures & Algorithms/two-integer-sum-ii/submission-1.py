class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp = 0
        rp = len(numbers) - 1

        while lp < rp:
            diff = target - numbers[lp] - numbers[rp]

            if diff == 0:
                return [lp + 1, rp + 1]
            elif diff > 0:
                lp += 1
            else:
                rp -= 1
        
        return False
        