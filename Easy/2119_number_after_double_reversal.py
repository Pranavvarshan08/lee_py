class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        temp =num 
        rev1 =0

        while temp > 0:
            digit = temp % 10
            rev1 = rev1 * 10 + digit
            temp = temp // 10
        
        temp = rev1
        rev2 = 0

        while temp >0:
            digit =temp %10
            rev2=rev2*10 + digit
            temp = temp //10
        
        return num == rev2
