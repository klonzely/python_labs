min=int(input("минуты: "))
min2=min%60
if min2<10:
    min2='0'+ str(min2)
hour=min//60 
print(str(hour)+':'+str(min2))
 