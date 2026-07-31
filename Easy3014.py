class Solution:
    def minimumPushes(self, word: str) -> int:
        answer = 0

        n=len(word)


        for i in range (n):

            press=(i//8)+1
            answer +=press

        return answer
