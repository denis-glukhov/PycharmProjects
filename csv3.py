import csv

l= []

with open("/home/denis/Downloads/csv1.csv", "r", encoding='utf8') as input_file:
    rdr = csv.reader(input_file)
    for rec in rdr:
        l.append(rec)

with open("/home/denis/Downloads/csv1.csv", "a") as output_file:
    wrtr = csv.writer(output_file)
    for rcrd in l:
        wrtr.writerow(rcrd)
        if rcrd == 'name,number,text':
            continue
        print(rcrd)
print (l)


