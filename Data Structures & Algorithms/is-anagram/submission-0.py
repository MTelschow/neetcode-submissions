class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letterCount = {}

        for c in s:
            if c not in letterCount:
                letterCount[c] = 0
            letterCount[c] += 1

        for c in t:
            if c not in letterCount or letterCount[c] == 0:
                return False
            letterCount[c] -= 1
        
        return True
        