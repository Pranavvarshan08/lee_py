class Solution:
    def smallestNumber(self, n: int, t: int) -> int:


        def DigitalProduct(number):
            if number ==0:
                return 0
            product =1

            while number>0:
                digit =number%10
                product *= digit
                number //=10
            return product
        while True:
            if DigitalProduct(n) % t == 0:
                return n

            n += 1
