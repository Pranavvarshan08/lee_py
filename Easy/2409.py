from datetime import datetime
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        a=max(arriveAlice,arriveBob)
        b=min(leaveAlice,leaveBob)
        if a>b:
            return 0
        return(datetime.strptime(b,"%m-%d")-
                datetime.strptime(a, "%m-%d")).days +1
        
