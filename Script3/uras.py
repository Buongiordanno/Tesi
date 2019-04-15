#iacino
import time
start = time.time()
starti=time.time()
#Legge e scrive bibbia
f = open("bibbia.txt","r")
text = f.read()
print (text.count("Dio"))
file = open("bibbiacopia.txt", "a+") 
file.write(text*5) 
file.close() 

#calcola i numeri primi 
num = 25000
IsPrime = 0
for N in range(0,num):
    #Controlla se e' divisibile per qualche numero...
    for D in range(2,N+1):
        IsPrime = 1
        if ((N % D) == 0) and (N != D):
            IsPrime = 0 #E' divisibile, non e' un numero primo
            break
endi = time.time() 
#ferretti

startferretti = time.time()
num = 70000

# uncomment to take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
#lettura e scrittura italiano
f = open("Baden.txt","r")
text = f.read()
print (text.count("bene"))
print (text.count("meglio"))
file = open("badencopia.txt", "a+") 
file.write(text*10) 
file.close() 
endferretti = time.time()
end=time.time()
print(endi - starti)
print(endferretti - startferretti)
print(end-start)
