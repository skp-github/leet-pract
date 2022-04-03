class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        loop_length =  k % len(nums)
        if  loop_length == 0 :
            return
        while loop_length:
            target = nums[-1]
            for i in range(len(nums)-2, -1, -1 ):
                nums[i+1] = nums[i]
            nums[0] = target
            loop_length -= 1
# approach two 
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        result = [0] * len(nums)
        for i in range(len(nums)):
            index = (i+k) % len(nums)
            result[index] = nums[i]
        nums[:] = result

# third approach
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        start = count = 0 
        while count < len(nums):
            current, prev = start, nums[start]
            while True:
                target_index = (current+k)%len(nums)
                nums[target_index], prev = prev, nums[target_index]
                
                current = target_index
                count +=1 
                if start == current:
                    break
            start +=1 