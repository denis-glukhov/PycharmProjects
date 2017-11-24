def l(x):
    s=str(x)
    ln=len(s)
    return(ln)

lst= list(range(1,7))

lst2 = []

for i in lst:
    dgt = i**(i**i)
    t = l(dgt)
    new_list = []
    new_list.append(i)
    new_list.append(t)
    new_list.append(dgt)
    lst2.append(new_list)
#print (lst2)

len_temp = []
len_lst2= (len(lst2))

#Вариант 1 - оператор reversed
#rev_lst2 = list(reversed(lst2))

#Вариант 2 - функция обратного перечисления в списке
rev_lst2 = lst2[::-1]

for x in rev_lst2:
    y= x[1]/x[1]
    print ( x[1])