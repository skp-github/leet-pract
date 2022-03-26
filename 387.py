class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        target_index = -1 
        for i in s:
            if i not in hashmap:
                hashmap[i] = 1
                continue
            hashmap[i] = hashmap[i] + 1
        for idx, ch in enumerate(s):
            if hashmap[ch] == 1:
                return idx
        return -1 