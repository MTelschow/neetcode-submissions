class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        compl = {}

        for i, num in enumerate(nums):
            if num in compl.keys():
                return [compl[num], i]

            compl[target - num] = i


        return []
                
        