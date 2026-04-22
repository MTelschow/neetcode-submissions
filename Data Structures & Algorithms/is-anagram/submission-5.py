class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts1, counts2 = [0 for x in range(26)], [0 for x in range(26)]
        for c in s:
            counts1[ord(c) - ord('a')] += 1
        for c in t:
            counts2[ord(c) - ord('a')] += 1
        return counts1 == counts2
        