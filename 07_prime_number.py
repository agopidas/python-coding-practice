def prime_number(num):
    if num>1:

        for i in range (2,num):

            if(num%i) == 0:
                print(num, "is not a prime number")
                break

        else:
            print(num, "is a prime number")
    else:
        print(num,"is not a prime number")



num = input("Insert Number to check if it is a Prime Number : ")
try:
    prime_number(int(num))

except:
    print("An exception occured")