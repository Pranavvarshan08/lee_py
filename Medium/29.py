class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign =-1 if (dividend <0) != (divisor<0)else 1

        dividend =abs(dividend)
        divisor=abs(divisor)

        count =0

        while dividend >= divisor:
            dividend -= divisor
            count +=1

        if sign == -1:
            return -count
        return count
