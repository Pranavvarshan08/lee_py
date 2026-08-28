class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        def solve(s):
            res=[]


            for i in range(len(s)):
                if s[i] in "+-*":
                    left=solve(s[:i])
                    right=solve(s[i+1:])

                    for a in left:
                        for b in right:
                            if s[i]=="+":
                                res.append(a+b)
                            elif s[i]=="-":
                                res.append(a-b)
                            else:
                                res.append(a*b)
            return res or [int(s)]
        return solve(expression)

        
