class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            middel = (l + r) // 2
            diff = target - nums[middel]

            if diff == 0:
                return middel
            elif diff > 0:
                l = middel + 1
            else:
                r = middel


        return l if target == nums[l] else -1