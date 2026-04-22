class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            if num not in freqs:
                freqs[num] = 0
            freqs[num] += 1
        

        orders = [[] for _ in range(max(freqs.values()))]
        for key in freqs.keys():
            orders[freqs[key] - 1].append(key)
        

        kMostFrequent = []
        while k > 0:
            most_freq = orders.pop()
            for num in most_freq:
                kMostFrequent.append(num)
                k -= 1

        return kMostFrequent
        