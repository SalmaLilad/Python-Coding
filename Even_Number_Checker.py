
numbers = [20, -5, 11, -36, 45]

def check_list(numbers):
    even_numbers = []

    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            even_numbers.append(numbers[i])

    return even_numbers          
            

