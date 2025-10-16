# a script favorite_pet.py that imports and uses the pet_names nodule

import pet_names # imports the pet_names module

print("My favorite pet is", pet_names.pet_name1, "-")
print("I remember when he weightd only", pet_names.pet_weight1, "pounds.")
print("I love", pet_names.pet_name2, "too, of course.")

if __name__ == "__main__":
    print("This is the __main__ code from favorite_pet.py")