class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += str(len(s)) + "#" + s
        return output


    def decode(self, s: str) -> List[str]:
        rem_s = s
        output = []

        while len(rem_s) > 0:
            # Get number
            end_idx = 0
            for char in rem_s:
                if char == "#":
                    break
                end_idx += 1
            str_len = int(rem_s[0:end_idx])
            # Get next_str
            next_str = rem_s[end_idx + 1: end_idx + 1 + str_len]
            output.append(next_str)
            # Slice begining
            rem_s = rem_s[end_idx + 1 + str_len:]
        
        return output

