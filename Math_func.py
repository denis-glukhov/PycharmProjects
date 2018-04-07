def f(x):
    if x <=-2:
        return (1-(x+2)**2) #,при x≤−2
    elif (-2<x) and (x<=2):
        return (-x/2) # ,при −2<x≤2
    elif x>2: #при 2<x
        return ((x-2)**2 + 1)

f(4)