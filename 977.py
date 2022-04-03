class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)):
            nums[i] = nums[i] **2 
        nums.sort()
        return nums

# better complexity 
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        left = 0 
        right = len(nums)-1 
        square = 0
        for i in range(len(nums)-1, -1 , -1):
            if abs(nums[left])<abs(nums[right]):
                square = nums[right]
                right -=1
            else:
                square = nums[left]
                left += 1
            result[i] = square * square
        return result
        