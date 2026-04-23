class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        current_best = 0

        for num in nums:
            if num - 1 in num_set:
                continue
            cur_len = 1
            while num + cur_len in num_set:
                cur_len += 1
            current_best = max(current_best, cur_len)

        return current_best