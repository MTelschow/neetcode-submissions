class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        index_range = range(len(nums))
        forward_product = [1 for _ in index_range]
        backwards_product = [1 for _ in index_range]

        for i in range(len(nums) - 1):
            forward_product[i+1] *= forward_product[i] * nums[i]

            backwards_idx = len(nums) - i - 1
            backwards_product[backwards_idx - 1] *= backwards_product[backwards_idx] * nums[backwards_idx]
        
        return [forward_product[i] * backwards_product[i] for i in index_range]