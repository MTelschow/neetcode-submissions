class Solution:
    def getCounts(self, word: str) -> Tuple(int):
        counts = [0 for x in range(26)]

        for letter in word:
            counts[ord(letter) - ord('a')] += 1

        return tuple(counts)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for word in strs:
            letter_counts = self.getCounts(word)
            if letter_counts not in groups.keys():
                groups[letter_counts] = []
            groups[letter_counts].append(word)

        return list(groups.values())
        