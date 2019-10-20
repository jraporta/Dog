def get_biggest_number (*argument):
    
    max=0
    for i in argument:
        if (type(i) is int) == False:
            return ("Error: Arguments must be integers")
        if i>max:
            max=i
    return (max)


print('The biggest number among the given is: ' , get_biggest_number(1 , 4 , 5 , -4 , 6 , 123 , 0))