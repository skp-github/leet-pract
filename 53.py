class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum_sum = nums[0]
        current_subarray = nums[0]
        for i in range(1, len(nums)):
            current_subarray = max(nums[i], current_subarray+nums[i])
            maximum_sum = max(maximum_sum,current_subarray)
        return maximum_sum 
        