class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        result_array = [0]*len(nums)
        temp_index = 0 
        for i in range(0, len(nums)):
            if nums[i] != 0:
                result_array[temp_index] = nums[i]
                temp_index +=1 
        nums[:] = result_array

# second approach
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero_index = 0
        for i in range(len(nums)):
            if nums[i] !=0:
                nums[last_non_zero_index] = nums[i]
                last_non_zero_index +=1 
        for i in range(last_non_zero_index, len(nums)):
            nums[i] = 0 

# third approach
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last = 0
        for curr in range(0, len(nums)):
            if nums[curr] != 0:
                temp = nums[last]
                nums[last] = nums[curr]
                nums[curr] = temp
                last+=1 
        