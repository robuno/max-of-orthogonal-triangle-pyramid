def removefirstdigit(number):
    strnumber = str(number)
    if strnumber[0] == "0":
        strnumber = strnumber[1:]
        number2 = int(strnumber)
        return number2
    else:
        return number

def isprime(number):
    if number > 1:
        for i in range(2,int((number/2)+1)):
            if (number % i) == 0:  #is not prime
                return False
        else:                      #is  prime
            return True
    else:
        return False

def main():
    openinput = open("triinput.txt", "r")
    inputlines = openinput.read().splitlines()

    z=0
    while(z < len(inputlines)):
        inputlines[z] = inputlines[z].split()
        z+=1

    triarray = []
    for k in range(len(inputlines)):
        subarray =[]
        for t in range(len(inputlines[k])):
            x = removefirstdigit(inputlines[k][t])
            subarray.append(int(x))
            if ( t+1 == len(inputlines[k])):
                triarray.append(subarray)
            else:
                t+=1
        k+=1

    sum = 0
    flag= 0
    for i in range(len(triarray)):
        #print(triarray[i])
        
        if ( len(triarray[i])==1 and isprime(triarray[i][flag])==False):
            sum  += triarray[i][flag]
        elif len(triarray[i]) > 1:
            if( isprime(triarray[i][flag]) == False and isprime(triarray[i][flag+1]) == False):
                if triarray[i][flag] >= triarray[i][flag+1]:
                    sum+=triarray[i][flag]
                    flag = triarray[i].index(triarray[i][flag])
                else:
                    sum+=triarray[i][flag+1]
                    flag = triarray[i].index(triarray[i][flag+1])
            elif ( isprime(triarray[i][flag]) == True and isprime(triarray[i][flag+1]) == False):
                sum+=triarray[i][flag+1]
                flag = triarray[i].index(triarray[i][flag+1])
            elif ( isprime(triarray[i][flag]) == False and isprime(triarray[i][flag+1]) == True):
                sum+=triarray[i][flag]
                flag = triarray[i].index(triarray[i][flag])
            else:
                break
                       
        else:
            break

    print(sum)            

if __name__ == "__main__":
    main()