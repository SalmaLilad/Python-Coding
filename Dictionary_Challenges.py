#DICTIONARY CHALLENGES
#1. CREATE A DICT AND CHANGE ITS VALUE

food = {
    "Billy": "toast"
}

print("Before update:", food)

food["Billy"] = "fish"

print("After update:", food)

#2. MOVE SOMEONE TO A NEW LOCATION
FLIPPED_MORSE_CODE_DICT = flip_dict(MORSE_CODE_DICT)

locations = {
    "Billy": "Home",
    "Zoey": "Home"
}

def move(person, new_location):
    print("Before update:", locations)
    locations[person] = new_location
    print(f"{person} has moved to {new_location}.")

    return locations

move("Billy", "Diner")
move("Zoey", "School")
