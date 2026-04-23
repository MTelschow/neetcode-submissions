class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences = [[] for num in nums]
        current_count = {}

        for num in nums:
            if num not in current_count:
                current_count[num] = 0
                occurences[0].append(num)
                continue
            current_count[num] += 1
            new_pos = current_count[num]
            occurences[new_pos].append(num)
            occurences[new_pos - 1].remove(num)

        result = []

        while len(result) < k:
            result.extend(occurences[-1])
            occurences.pop()

        return result
        