class Solution:
    def sumGame(self, num: str) -> bool:
        n=len(num)//2
        a=num[:n]
        b=num[n:]

        x=sum(map(int,a.replace('?','0')))
        y=sum(map(int,b.replace('?','0')))
        p=a.count('?')
        q=b.count('?')

        if (p+q)%2 !=0:
            return True

        return x-y !=9*(q-p)//2
