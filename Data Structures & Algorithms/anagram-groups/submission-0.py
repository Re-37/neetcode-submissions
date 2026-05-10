class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt = {}

        for s in strs:
            encoding = [0] * 26
            
            for c in s:
                encoding[ord(c) - ord('a')] += 1
            
            key = tuple(encoding)
            
            if key not in dictt:
                dictt[key] = []
                
            dictt[key].append(s)

        return list(dictt.values())
