class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        for i, num in enumerate(nums):
            comp = target - num
            if comp in seen:
                j = nums.index(comp)
                return [j,i]
            else:
                seen.add(num)