#Fattoriale

import time
start = time.time()
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
end = time.time()
print(end - start)
