class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_cum_prod = [1]
        right_cum_prod = [1]

        for num in nums:
            left_cum_prod.append(num * left_cum_prod[-1])
        for num in nums[::-1]:
            right_cum_prod.append(num * right_cum_prod[-1])
        right_cum_prod = right_cum_prod[::-1]
        

        total_len = len(nums)
        # return right_cum_prod
        return [left_cum_prod[idx] * right_cum_prod[idx +  1] for idx in range(total_len)]
        
        