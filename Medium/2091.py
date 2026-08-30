class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        
        min_i=nums.index(min(nums))
        max_i=nums.index(max(nums))
        a=max(min_i,max_i)+1
        b=n-min(min_i,max_i)
        c=min(max_i,min_i)+1+n-max(min_i,max_i)

        return min(a,b,c)
