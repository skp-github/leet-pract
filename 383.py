class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}
        for i in ransomNote:
            if i not in hashmap:
                hashmap[i] = 1
                continue
            hashmap[i] += 1
        for i in magazine:
            if i in hashmap:
                hashmap[i] = hashmap[i] - 1
        for idx, ch in enumerate(ransomNote):
            if hashmap[ch] > 0 :
                return False
        return True