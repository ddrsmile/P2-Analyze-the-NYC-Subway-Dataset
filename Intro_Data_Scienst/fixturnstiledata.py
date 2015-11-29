import csv
def ftd(filenames):
  for name in filenames:
    f_in = open(name, 'r')
    f_out = open('updated_' + name, 'w')
    reader = csv.reader(f_in, delimiter=',', quoting=csv.QUOTE_NONE)
    writer = csv.writer(f_out, delimiter=',', quoting=csv.QUOTE_NONE)
    for row in reader:
      head = row[0:3]
      row = row[3::]
      while len(row) > 0:
        writer.writerow(head + row[0:5])
        del row[0:5]

    f_in.close()
    f_out.close()
