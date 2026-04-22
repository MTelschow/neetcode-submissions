class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letter_counts = [0 for _ in range(26)]

        for i in range(len(s)):
            letter_counts[ord(s[i]) - ord('a')] += 1
            letter_counts[ord(t[i]) - ord('a')] -= 1
        
        return len([count for count in letter_counts if count != 0]) == 0