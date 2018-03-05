n=int(input())
r=range(n)

rr=range(0,n,-1)
m = [[0 for j in r] for j in r]

x, y = 0, n-1

m[0][0]=1
for i in r:
    for j in r:
        if i == x and j<=y and j>x:
            m[i][j]+=m[i][j-1]+1
        elif j == y and j>=x:
            m[i][j]+=m[i-1][j]+1

for i in (rr):
  print (int(i))


#for i in m:
#  print(i)