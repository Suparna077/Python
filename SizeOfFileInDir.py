import os
from os import path

def main():

    totalbyte = 0
    Dir_Name = "D:\\Ielts"
    content = os.listdir(Dir_Name)
    for entry in content:
        if entry.endswith(".txt"):
            totalbyte = totalbyte + path.getsize(Dir_Name + "\\" + entry)

    print("The total Byte size of all TXT files are : ", totalbyte)

    Result = open("Result.txt","a+")
    if Result.mode == 'a+':
        Result.write("The total size of all text file inside Ielts dir is : " + str(totalbyte) + "\n")
        Result.write("The name list of the files are as below : \n ")
        Filelist = os.listdir(Dir_Name)
        for entry in Filelist:
            if entry.endswith(".txt"):
                Result.write("\t\n" + str(entry))

    Result.close()


if __name__ == "__main__":
    main()