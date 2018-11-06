# https://leetcode.com/problems/binary-gap/description/

def binaryGap(self, N):
    count = 0
    nB = bin(N)[2:]
    nBL = len(nB)
    j = 0   #Last recorded instance of '1'        
    for i in range(1, nBL):
        if nB[i] == '1': 
            count= max(count, i - j)
            j = i
    return count
