
n=int(input("Enter the Number: "))
fact=1

if(n<0):
        print("Factorial is not define.")
elif(n==0 or n==1):
        print("factorial is 1")
else:
    for i in range(1,n+1):
        fact=fact*i
    print(fact)

if(n<=1):
    print("Number is not prime")
else:
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            print("not prime")
            break
    else:
         print("prime") 
