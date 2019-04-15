
import time
start = time.time()
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


end = time.time()

print(end - start)
