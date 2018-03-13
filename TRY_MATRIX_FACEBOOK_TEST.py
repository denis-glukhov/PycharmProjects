n=int(input())
r=range(n)
m = [[0 for j in r] for j in r]
#m[0][0]=1

for nn in range(n):
    x, y = nn, n-(1+nn)
    for i in r:
        for j in r:
            if m[i][j] == 0:
                if i == x and j <= y: #and j > x:
                    m[i][j] += m[i][j - 1] + 1
                elif j == y and j > x:
                    m[i][j] += m[i - 1][j] + 1
    rr=range(y, x-1,-1)

    for i in rr:
        for j in rr:
            if i == y and j<y:
                m[i][j]+=m[i][j+1]+1
            elif j == x and i < y:#  and i > x:
                m[i][j] += m[i+1][j] + 1

for i in m:
  print(i)
