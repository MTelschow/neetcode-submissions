class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        current_count = {}

        for num in nums:
            if num not in current_count:
                current_count[num] = 0
            current_count[num] += 1

        occurences = [[] for num in nums]
        for num, count in current_count.items():
            occurences[count - 1].append(num)


        result = []
        while len(result) < k:
            result.extend(occurences[-1])
            occurences.pop()

        return result
        