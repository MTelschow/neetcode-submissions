class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        
        max_length = 0

        for num in nums:
            if num - 1 in nums_set:
                continue
                
            curr_len = 1
            curr_num = num + 1

            while curr_num in nums_set:
                curr_len += 1
                curr_num += 1

            if max_length < curr_len:
                max_length = curr_len

        return max_length

        