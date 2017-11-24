import datetime

now = datetime.datetime.now()

print ('Привет, меням зовут поэт Пломбъе!!!')
name=(input('Как тебя зовут?    '))
print('____'*50)
age =input('А сколько тебе лет, '+name+  '?     ')
print('____'*50)

mamy_name=(input(name+ ', а как зовут твою маму?    '))
mamy_age =input(name + ', а сколько лет твоей маме ' + mamy_name +'?   ')
print('____'*50)



#этот год
this_year = now.year


#Вычисляю в каком году тебе будет 100 лет
when_100_year_old = int(this_year)-int(age)+100

#вычимсляю счерез сколько лет тебе будет 100 лет
how_long_it_will_take_you_to_be_100_year_old = when_100_year_old-this_year

print('____'*50)
print('Отлично!!!')
print(name+', тебе пока '+str(age) +' лет.')
print('Через '+str(how_long_it_will_take_you_to_be_100_year_old)+ ' лет тебе будет 100 лет')
print('Это будет '+ str(when_100_year_old) + '-ный год.')
print('____'*50)
print(name, 'твоей маме тогда будет' , str(int(mamy_age)+how_long_it_will_take_you_to_be_100_year_old), 'лет')

