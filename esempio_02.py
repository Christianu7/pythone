r=int(input("dammi un numero: "))
A=input("dammi una lettera: ")

for i in range(1,r+1): 
    print(" "*(r-i) + A*(1+(i-1)*2))
