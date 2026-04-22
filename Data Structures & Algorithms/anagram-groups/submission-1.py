class Solution:
    def get_word_counts(self, word):
        counts = [0 for _ in range(26)]

        for char in word:
            counts[ord(char) - ord('a')] += 1

        return tuple(counts)


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            counts = self.get_word_counts(word)

            if counts not in groups.keys():
                groups[counts] = []
            groups[counts].append(word)
            
        return list(groups.values())
        