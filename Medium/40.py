class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res=[]

        def backtrack(cur,i,target):
            if target == 0:
                res.append(cur.copy())
                return 
            if target <0:
                return 
            for j in range(i,len(candidates)):
                if j>i and candidates[j] ==candidates[j-1]:
                    continue

                if candidates[j]>target:
                    break

                cur.append(candidates[j])
                backtrack(cur,j+1,target-candidates[j])
                cur.pop()

        backtrack([],0,target)
        return res
        
