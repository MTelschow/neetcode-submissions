class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        cur = 0

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[cur]:
                l = m + 1
            else:
                r = m
                cur = m

        return nums[cur]
         