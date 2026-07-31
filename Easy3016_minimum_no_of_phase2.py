class Solution:
    def minimumPushes(self, word: str) -> int:
        freq={}
      
        for ch in word:
            freq[ch]=freq.get(ch,0)+1

        counts=list(freq.values())
        counts.sort(reverse=True)

        answer=0

        for i,count in enumerate(counts):
            pushes=(i//8)+1
            answer += pushes*count
        return answer
