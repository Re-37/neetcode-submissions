class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for word in strs:
            chars = [0] * 26
            for w in word:
                chars[ord(w) - ord('a')] += 1
            
            key = tuple(chars)
            if key not in groups:
                groups[key] = []
            groups[key].append(word)

        return list(groups.values())
