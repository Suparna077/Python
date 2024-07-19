Substringdict = {}

def calculatestring(inputstr , k):

    tempstr = inputstr
    lenstr = len(inputstr)
    for pos in range(0,lenstr):
        subpos = pos
        count = 0
        globals()[f"Substrng_{pos}"] = []
        temp = []
        while subpos != lenstr and count != k:
            if tempstr[subpos] == '1':
                temp.append('1')
                count = count + 1
            else :
                temp.append('0')
            subpos = subpos + 1
        if count == k:
            globals()[f"Substrng_{pos}"] = temp.copy()
        del temp
        if len(globals()[f"Substrng_{pos}"]) != 0:
            key = 'key_{}'.format(pos)
            Substringdict[key] = globals()[f"Substrng_{pos}"]

def getsortsubstring():
    lst = 9999999
    lstkey = ''
    for key in Substringdict:
        lsttemp = len(Substringdict.get(key))
        if lsttemp < lst:
            lst = lsttemp
            lstkey = key
    resultlst = Substringdict[lstkey].copy()
    for key in Substringdict:
        if len(Substringdict.get(key)) == lst:
            resultlst = sortstringlexical(resultlst,Substringdict[key],lst)
    return resultlst


def sortstringlexical(rsultlst,otherlst,lst):

    for i in range(0,lst):
        if rsultlst[i] == '0' and otherlst[i] == '1':
            return rsultlst
        elif otherlst[i] == '0' and rsultlst[i] == '1':
            return otherlst
    return rsultlst




def main():

    inputstr = input("Enter The Binary String : ")
    K = int(input("Enter the length of 1 in Substring: "))
    calculatestring(inputstr,K)
    result = getsortsubstring()
    print("The lexically least string is : - " , result)























































if __name__ == "__main__":
    main()