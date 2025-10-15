while True:

    try:
        num_apples = int(input("How many apples do you have?"))
        if num_apples < 0:
            print("You can't have a negative amount of apples!")
        

        elif num_apples <= 5:
            print("That's a good amount of apples")

        else:
            print("Good job picking apples!")

    except ValueError:
        print("We are only counting whole apples, please put in your value as an integer")
       


    

scripts = ["Congrats! Now you have picked a bunch of apples from the apple orchard.","\nDo you want to pick some more?"]

for s in scripts:
        print(s)
        time.sleep(3)
        
        
