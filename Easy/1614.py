class Solution:
    def maxDepth(self, s: str) -> int:
        depth=0
        ans=0
        for x in s:
            if x=='(':
                depth +=1
                ans =max(ans,depth)
            elif x==')':
                depth -=1
        return ans
