class Solution:
    def maxDepth(self, s: str) -> int:
        res = cnt = 0 
        for i in s:
            if i == '(':
                cnt += 1 
                res = max(res, cnt)
            elif i == ')':
                cnt -= 1 
        return res