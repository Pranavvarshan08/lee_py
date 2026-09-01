class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set(),for a in range(9)]
        cols=[set(),for b in range(9)]
        boxes=[set(),for c in range(9)]

        for i in range(9):
            for j in range(9):
                num=board[i][j]

                if nums ==".":
                    continue
                box=(i//3)*3+(j//3)
                if num in row[i]:
                    return False
                if num in column[j]:
                    return False

                row[i].add(num)
                row[j].add(num)
                boxes[box].add(num)
            return True


