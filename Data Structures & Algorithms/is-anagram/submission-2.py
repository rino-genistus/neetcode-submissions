class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        word1 = {}
        word2 = {}
        for char_s, char_t in zip(s, t):
            print(char_s, char_t)
            if char_s not in word1.keys():
                word1[char_s] = 1
            else:
                word1[char_s] += 1
            if char_t not in word2.keys():
                word2[char_t] = 1
            else:
                word2[char_t] += 1
        word1 = dict(sorted(word1.items()))
        word2 = dict(sorted(word2.items()))
        return word1 == word2