class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans=[]

        def backtrack(path):
            if len(path) == len(nums):
                ans.append(path[:])
                return 
            for num in nums:
                if num not in path:
                    path.append(num)
                    backtrack(path)
                    path.pop()

        backtrack([])

        return ans


        
