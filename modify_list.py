def modify_list(l):
    r=[]
    r=[j for j in l if j%2!=1]
    l.clear()
    for x in r:
        l.append(int(x/2))


    #    l.remove(l[0])

lst =  [4,1,4,1,4,1]
modify_list(lst)
print(lst)               # [5, 4]