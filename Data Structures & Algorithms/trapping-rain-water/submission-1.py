class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0]
        right_max = [0]
        total_water = 0

        for num in height[::-1]:
            right_max.append(max(right_max[-1], num))
        right_max = right_max[::-1]
        for num in height:
            left_max.append(max(left_max[-1], num))


        for i, num in enumerate(height):
            water_surface = min(left_max[i], right_max[i + 1])
            water = max(0, water_surface - num)
            total_water += water

        return total_water
        