
# convert celsius degrees F
# C = (F-32)5/9

def conversion(f):
    return (f-32) * (5/9)
# Converting F to C

def reconversion(c):
    return (c * 9/5) + 32

def case_1():
    a = conversion(int(input("How much degrees F do you have?")))

    print(a)

def case_2():
       b = reconversion(int(input("How much degrees C do you have?")))

       print(b)


# Converting C to F

def main():
    try:
        
        case_1()
        
                             
    except ValueError:
        print("Please pick a number")
        case_1()
        

    try:
        case_2()
        
    except ValueError:
        print("Please print a number")
        case_2()
        
                                 
main()
