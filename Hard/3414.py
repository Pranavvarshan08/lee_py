class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        intervals=[(s,e,w,i)for i,(s,e,w)in enumerate(intervals)]
        intervals.sort()

        n=len(intervals)

        dp=[[([],0)for i in range(5)] for j in range(n+1)]
        for i in range(n-1,-1,-1):
            s,e,w,idx=intervals[i]

            l,r=i+1,n
            while l<r:
                m=(l+r)//2
                if intervals[m][0]>e:
                    r=m
                else:
                    l=m+1

            j=l

            for k in range(1,5):
                take_ids=[idx]+dp[j][k-1][0]
                take_weight=w+dp[j][k-1][1]

            skip_ids=dp[i+1][k][0]
            skip_weight=dp[i+1][k][1]
            if take_weight>skip_weight:
                dp[i][k]=(take_ids,take_weight)
            elif take_weight<skip_weight:
                dp[i][k]=(skip_ids,skip_weight)
            else:
                dp[i][k]=(min(sorted(take_ids),sorted(skip_ids)),take_weight)
    return sorted(dp[0][4][0])
