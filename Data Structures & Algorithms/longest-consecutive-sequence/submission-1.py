class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        set_nums = set(nums)

        for num in nums:
            if num - 1 in set_nums:
                continue
            
            cur = num + 1

            while cur in set_nums:
                cur += 1
            
            longest = max(longest, cur - num)
        
        return longest