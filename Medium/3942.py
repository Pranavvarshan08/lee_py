class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        zero=nums.index(0)

        def check(s):
            return all(nums[(zero+i*s)%n] <nums[(zero+(i+1)*s)%n]for i in range(n-1))
        ans=[]
        if check(1):
            ans+= [zero,n-zero+2]
        if check(-1):
            ans+=[zero+2,n-zero]
        return min(ans) if ans else -1

        
