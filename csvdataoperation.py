import csv


def main():

    CSVdata = open("10_02_us.csv","r")

    reader = csv.DictReader(CSVdata,delimiter='\t')
    # n = 0
    # for row in reader:
    #     if n < 1:
    #         print(row)
    #         n += 1
    #     else:
    #         break

    writedatacsv = open("result.csv","w+")
    writer = csv.writer(writedatacsv,lineterminator='\n')
    n = 0
    writer.writerow(reader.fieldnames)
    for row in reader:
        if n < 100:
            writer.writerow(row[str(key)] for key in row)
            n += 1
        else:
            break

    writedatacsv.close()
    readfile = open("result.csv","r")
    print(readfile.read())
    readfile.close()

if __name__ == "__main__":
    main()