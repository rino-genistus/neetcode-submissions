class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        word1 = {}
        word2 = {}
        for char in s:
            if char not in word1.keys():
                word1[char] = 1
            else:
                word1[char] += 1
        for char in t:
            if char not in word2.keys():
                word2[char] = 1
            else:
                word2[char] += 1
        word1 = dict(sorted(word1.items()))
        word2 = dict(sorted(word2.items()))
        print(word1.values())
        print(word2.values())
        return word1 == word2