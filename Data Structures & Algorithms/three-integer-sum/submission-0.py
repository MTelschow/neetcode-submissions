class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = set()
        nums_len = len(nums)
        s_nums = sorted(nums)

        for i, num1 in enumerate(s_nums):
            left_p = i + 1
            right_p = nums_len - 1

            while left_p < right_p:
                sum_3 = num1 + s_nums[left_p] + s_nums[right_p]
                if sum_3 == 0:
                    results.add(
                        (num1, s_nums[left_p], s_nums[right_p])
                    )
                    left_p += 1
                elif sum_3 < 0:
                    left_p += 1
                else:
                    right_p -= 1
        return [list(x) for x in results]