DELIMITER = "$"

class Solution:
    def encode(self, strs: List[str]) -> str:
        lengths = [str(len(word)) + DELIMITER + word for word in strs]
        return "".join(lengths)


    def decode(self, s: str) -> List[str]:
        results = []
        cur_s = s
        while len(cur_s) > 0:
            cur_idx = 0
            # Get first del
            while cur_s[cur_idx] != DELIMITER:
                # if cur_idx >= len(cur_s):
                #     raise Exception("Wrong format")
                cur_idx += 1
            next_str_len = int(cur_s[:cur_idx])

            next_str = cur_s[cur_idx + 1 : cur_idx + 1 + next_str_len]
            results.append(next_str)
            cur_s = cur_s[cur_idx + 1 + next_str_len:]

        return results

