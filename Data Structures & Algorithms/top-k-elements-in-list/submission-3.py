from collections import deque

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        reversed_queue = deque()
        freq = dict(sorted(freq.items(), key=lambda item:item[1],reverse=True))
        dict_keys = list(freq.keys())
        counter = 0
        for i in range(k):
            reversed_queue.appendleft(dict_keys[counter])
            counter+=1
        return_list = []
        while len(reversed_queue) != 0:
            return_list.append(reversed_queue.pop())
        return return_list