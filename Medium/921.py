class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = add =0
        for c in s:
            if c=='(':
                open +=1
            elif open:
                open -=1
            else:
                add +=1

        return open +add

       
