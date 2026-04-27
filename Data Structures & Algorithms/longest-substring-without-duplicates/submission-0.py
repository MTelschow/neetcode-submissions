class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        top_len = 0
        cur_len = 0
        seen = set()

        for i, c in enumerate(s):
            while c in seen:
                seen.remove(s[i - cur_len])
                cur_len -= 1

            seen.add(c)
            cur_len += 1
            top_len = max(top_len, cur_len)

        return top_len