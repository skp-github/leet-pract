class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        # O(n*n)
        # count = 0
        # for i in range(0, len(nums)):
        #     for j in range(0, len(nums)):
        #         if i !=j and abs(nums[i]-nums[j]) == k and i < j:
        #             count +=1 
        # return count 
        
        # O(n+n) 
        res = 0
        count_map = {key:0 for key in range(0,101) }
        for i in nums:
            count_map[i] = count_map[i]+1
        for i in range(k+1, 101):
            res += count_map[i] * count_map[i-k]
        return res
        
                    
                    