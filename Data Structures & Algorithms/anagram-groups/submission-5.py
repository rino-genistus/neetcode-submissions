class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        anagram_dict = {}
        for word in strs:
            curr = "".join(sorted(word))
            if curr in anagram_dict:
                anagram_dict[curr].append(word)
            else:
                anagram_dict[curr] = []
                anagram_dict[curr].append(word)
        return_list = []
        return list(anagram_dict.values())