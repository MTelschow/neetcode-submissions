class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(str(len(s)) + "#" + s for s in strs)
        
        output = ""

        for s in strs:
            output += str(len(s)) + "#" + s
        
        return output


    def decode(self, s: str) -> List[str]:
        rem_s = s
        output = []

        while len(rem_s) > 0:
            end_idx = 0
            for char in rem_s:
                if char == "#":
                    break
                end_idx += 1
            
            str_len = int(rem_s[0:end_idx])
            o_str = rem_s[end_idx + 1: end_idx + 1 + str_len]
            output.append(o_str)
            rem_s = rem_s[end_idx + 1 + str_len:]
        
        return output

