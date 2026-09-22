class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign =-1 if (dividend <0) != (divisor<0)else 1

        dividend =abs(dividend)
        divisor=abs(divisor)

        result =0

        while dividend >= divisor:
            temp=divisor
            count=1

            while dividend >= temp <<1:
                temp <<=1
                count <<=1
            dividend -=temp
            result +=count

        result = result if sign ==1 else -result

        if result >2**31 -1:
            return 2**31-1
        return result
