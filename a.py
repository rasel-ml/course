a=[
    [1,2],
    [3,4]
]
b=[
    [5,6],
    [7,8]
]
result=[[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len[0]):
        for k in range(len(b)):
            result[i][j]+=a[i][k]*b[k][j]
for row in result:
    print(row)            
        
