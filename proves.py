numbersList=[]

try:
    while True:
        numbersList.append(int(input()))
except:
    pass
#    print(nenters)

#get_biggest_number()


max=0
for i in numbersList:
    if i>max:
        max=i

print('The biggest number among the given is:' , max , '\n')