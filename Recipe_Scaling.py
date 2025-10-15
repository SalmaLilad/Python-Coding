
cups_milk = 8
cups_rice = 1
cups_sugar = 0.5
tsp_vanilla = 1
scaling_factor = 2.5

try:       
    total_cups_milk = (cups_milk * scaling_factor)
          
    total_cups_rice = (cups_rice * scaling_factor)
           
    total_cups_sugar = (cups_sugar * scaling_factor)
          
    total_tsp_vanilla = (tsp_vanilla * scaling_factor)
          
except ValueError:
    print("Please print an integer value")
    pass

print(f"The recipe needs",total_cups_milk,"of milk.\n",total_cups_rice,"cups of rice.\n",total_cups_sugar,"cups of sugar.\n",total_tsp_vanilla,"teaspoons of sugar.")
