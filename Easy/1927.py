class Solution:
    def sumGame(self, num: str) -> bool:
        n=len(num)//2
        a=num[:n]
        b=num[n:]

        x=sum(map(int,a.replace('?','0')))
        y=sum(map(int,b.replace('?','0')))
        p=a.count('?')
        q=b.count('?')

        return not (p !=q and abs(x-y)*2 ==9*abs(p-q))or (p == q and x != y)
