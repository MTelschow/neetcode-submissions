class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        occurences = []
        results = []
        for i, tmp in enumerate(temperatures[::-1]):
            while len(occurences) > 0 and occurences[-1][0] <= tmp:
                occurences.pop()
            if len(occurences) == 0:
                results.append(0)
            else:
                results.append(i - occurences[-1][1])

            occurences.append([tmp, i])

        return results[::-1]
