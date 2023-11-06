blockSize = [100,500,200,300,600]
processSize = [212,417,112,426]
m = len(processSize)
n = len(blockSize)
blockNum = [-1]*n

for i in range(m):
    for j in range(n):
        if blockSize[j]>=processSize[i]:
            afterFit = blockSize[j]-processSize[i]
            blockSize[j]= afterFit
            blockNum[j]= j+1
            break
        if processSize[i]>blockSize[j]:
            blockNum[j]='not allocated'
    print(i,'\t',processSize[i],'\t',blockNum[j])