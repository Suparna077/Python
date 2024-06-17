
def main():

    Count = int(input("Enter the number of values in the list : "))
    Inputdata = []
    UniqueInput = []
    DuplicateInput = []



    for x in range(0, Count):
        Inputdata.append(input("Enter The Element in the List: "))

    Pos = 0
    for x in Inputdata:
        if Inputdata.index(x) == Pos:
            UniqueInput.append(x)
        Pos = Pos + 1

    Pos = 0
    for x in Inputdata:
        if Inputdata.index(x) != Pos:
            DuplicateInput.append(x)
        Pos = Pos + 1

    print("The Unique Elements List is : " , UniqueInput)
    print("The Rejected Records List is : ", DuplicateInput)


if __name__ == "__main__":
    main()



