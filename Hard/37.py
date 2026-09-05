class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row =[[0]*9 for i in range(9)]
        col=[[0]*9 for j in range(9)]
        box=[[0]*9 for k in range(9)]
        empty=[]

        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    empty.append((i,j))
                else:
                    n=int(board[i][j])-1
                    row[i][n]=col[j][n]=box[i//3*3+j//3][n]=1
        def dfs(k):
            if k == len(empty):
                return True
            i,j=empty[k]
            b=i//3*3+j//3

            for n in range(9):
                if not row[i][n] and not col[j][n] and not box[b][n]:
                    row[i][n]=col[j][n]=box[b][n]=1
                    board[i][j]=str(n+1)

                    if dfs(k+1):
                        return True
                    row[i][n]=col[j][n]=box[b][n]=0
            return False
        dfs(0)
