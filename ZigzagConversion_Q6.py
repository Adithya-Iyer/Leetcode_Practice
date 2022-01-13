class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows==1):
            return s #no zigzag possible with just 1 row
        c = (len(s)//numRows)+numRows
        x = [[0 for m in range(len(s))] for n in range(numRows)] #initializing zigzag matrix, number of columns longer than needed
        i = j = 0
        for ch in s:
            #print(ch)
            if ((j%(numRows-1))==0): #column number which is multiple of (numRows-1) is populated fully
                if(x[0][j]==0):
                    i=0 #bring index to start of column
                x[i][j]=ch
                if (i<(numRows-1)):
                    i+=1 #increment row till last row is reached
                else:
                    j+=1 #increment column when last row is reached
            else: #traverse diagonally upwards
                i-=1
                x[i][j]=ch
                j+=1
            #print(x)
        out = []
        for l in x:
            for c in l:
                if not (c==0):
                    out.append(c) #read non-zero values of matrix into 1D list
        return (''.join(out)) #list to string conversion
