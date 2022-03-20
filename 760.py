class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for i, b in enumerate(nums2):
            if b not in d:
                d[b] = []
            d[b].append(i)
            
        return [d[a].pop() for a in nums1]