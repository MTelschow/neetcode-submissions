class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = set()
        snums = sorted(nums)
        lnums = len(snums)

        for i in range(lnums - 2):
            lp = i + 1
            rp = lnums - 1
            while lp < rp:
                total = snums[i] + snums[lp] + snums[rp]

                if total == 0:
                    results.add((snums[i], snums[lp], snums[rp]))
                    lp += 1
                elif total < 0:
                    lp += 1
                else:
                    rp -= 1
        
        return [list(x) for x in results]

