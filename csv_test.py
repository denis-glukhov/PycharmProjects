import csv, datetime



input_file = open ("/home/denis/Downloads/csv.csv", "r", encoding='ascii')
#new_items_by_support_users
rdr = csv.reader(input_file)
output_file = open("/home/denis/Downloads/csv1.csv", "w")
wrtr = csv.writer(output_file)
for rec in rdr:
    try:
        rec[1] = int(rec[1]) + 56556

    except:
        pass
    print(rec)
    now = datetime.datetime.now()
    random = str(str(now)[-2] + str(now)[-1])[-1]
    print(str(random))

    wrtr.writerow(rec)
input_file.close()
output_file.close()


