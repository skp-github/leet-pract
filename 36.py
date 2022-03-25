# naive apporach 
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        # Use hash set to record the status
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                if val == ".":
                    continue
                
                if val in rows[r]:
                    return False 
                rows[r].add(val)
                if val in cols[c]:
                    return False
                cols[c].add(val)
                idx = (r//3)*3+c//3
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)
        return True 
                
# a little better approach
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        # Use hash set to record the status
        rows = [[0]*N for _ in range(N)]
        cols = [[0]*N for _ in range(N)]
        boxes = [[0]*N for _ in range(N)]
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue 
                pos = int(board[r][c])-1
                
                if rows[r][pos] == 1:
                    return False 
                rows[r][pos] = 1
                if cols[c][pos] == 1:
                    return False
                cols[c][pos] = 1
                idx = (r//3)*3+c//3
                if boxes[idx][pos] == 1:
                    return False
                boxes[idx][pos] = 1
        return True 

#bit masking
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        # Use hash set to record the status
        rows = [0]*N 
        cols = [0]*N 
        boxes = [0]*N 
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue 
                pos = int(board[r][c])-1
                
                if rows[r] & (1<<pos):
                    return False 
                rows[r] |= (1<<pos)
                if cols[c] & (1<<pos):
                    return False
                cols[c] |= (1<<pos)
                idx = (r//3)*3+c//3
                if boxes[idx] & (1<<pos):
                    return False
                boxes[idx] |= (1<<pos)
        return True 
              