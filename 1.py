class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        int_index_map = {}
        for i, num in enumerate(nums):
            lookup_value = target-num
            if lookup_value in int_index_map:
                return [i, int_index_map[lookup_value]]
            int_index_map[num] = i
        return []