from typing import List
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m,n=len(grid),len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]>0:
                    stack=[(i,j)]
                    total =0
                    grid[i][j]=-grid[i][j]

                    while stack:
                        x,y =stack.pop()
                        total += abs(grid[x][y])
                        grid[x][y]=-1

                        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                            a,b =x+dx,y+dy
                            if 0 <= a <m and 0<=b<n and grid[a][b]>0:
                                grid[a][b]=-grid[a][b]
                                stack.append((a,b))
                    if total % k==0:
                        count +=1
        return count

        
