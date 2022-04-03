class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1,j+1]
# second apporach 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        right = len(numbers)-1
        for i in range(len(numbers)):
            summation = numbers[left] + numbers[right]
            if summation == target:
                return [left+1, right+1]
            elif summation > target:
                right-=1 
            else:
                left +=1 
    
                