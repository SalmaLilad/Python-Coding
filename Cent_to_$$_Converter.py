#convert a given amount of pennies to a $$ amount
#cents, total cents, dollars, total dollars


while True:

    try:
        total_cents = int(input("How many cents do you have?"))

        if total_cents < 0:
            print("You can't have negative cents!")
            continue
        else:
            
           total_dollars = int(total_cents / 100)
            
    
       
        cents = total_cents % 100

    
    except ValueError:
        print("Please print an integer value")
        continue


    print(f"You have ${total_dollars}.{cents}")
    break
   
                              

        
    
   
    
   
       
        
