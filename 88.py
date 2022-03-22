class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index_num1 = m-1
        index_num2 = n-1
        for index in range(n+m-1, -1, -1):
            if index_num2 < 0:
                break
            elif index_num1 >=0 and nums1[index_num1] > nums2[index_num2]:
                nums1[index] = nums1[index_num1]
                index_num1 -=1 
            else:
                nums1[index] =  nums2[index_num2]
                index_num2 -=1
        
                
                
            