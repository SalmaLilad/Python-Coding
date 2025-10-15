def new_set(l,h):
    sum = 0
    for i in range(l,h):

        if i % 2 == 0:
            print("i= ",i)
            sum += i
            



        else:
            print("----------------")
    return 'Your sum:',sum

variable_l = int(input("Enter a number for the start of the range: "))
variable_h = int(input("Enter a number for the end of the range: "))


print(new_set(variable_l,variable_h))

    


