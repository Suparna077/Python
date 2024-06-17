import calendar

def main():

    Y = int(input("Enter The Year : "))
    M = int(input("Enter The Month : "))

    c = calendar.TextCalendar(calendar.MONDAY)
    str = c.formatmonth(Y, M, 0, 0)
    print(str)

    calculate(Y,M)



def calculate(Y,M):


    for day in calendar.day_name:
         globals()["var_"+str(day)] = []

    week = calendar.monthcalendar( Y, M)
    for x in range(0,5):

        weekarray = week[x]
        i = 0
        for day in calendar.day_name:
            if weekarray[i] != 0:
                globals()["var_" + str(day)].append(weekarray[i])
            i = i + 1


    for day in calendar.day_name:
        print(day , " ==> " , globals()["var_" + str(day)])
















if __name__ == "__main__":
    main()