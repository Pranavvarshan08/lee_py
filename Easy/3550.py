class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i  in range(len(nums)):
            digit_sum =sum(int(digit)for digit in str(nums[i]))

            if digit_sum ==1:
                return i

        return -1
