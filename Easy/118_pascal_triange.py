class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result =[]

        if numRows==0:
            return result
            
        row=[1]
        result.append(row)
        for i in range(1,numRows):
            previous=result[-1]
            row=[1]
            for j in range(len(previous)-1):
                row.append(previous[j]+previous[j+1])
            row.append(1)
            result.append(row)

        return result

        
