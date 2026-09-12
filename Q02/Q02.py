#QUESTION NUMBER 2
#Develop a Python program to generate
#the Fibonacci series using recursive and user-defined functions.

def fibonacci(n):
     if(n<=1):
           return n
     else:
          return fibonacci(n-1)+fibonacci(n-2)
     
n=int(input("Enter the number: "))

#TO PRINT NTH FIBONACCI NUMBER==================================
print(n,"Number","fibonacci Number is=",fibonacci(n))

 #TO PRINT FIBONACCI SERIES===================================
num=int(input("Enter the number of fibonacci term: "))
print("fibonacci series")

for i in range(num):
    print(fibonacci(i),)
