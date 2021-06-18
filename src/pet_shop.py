# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_cash(pet_shop, cash_amount):
    pet_shop["admin"]["total_cash"] = (pet_shop["admin"]["total_cash"] + 10)

def remove_cash(pet_shop, cash_amount):
    pet_shop["admin"]["total_cash"] = (pet_shop["admin"]["total_cash"] - 10)
    
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, pets_sold):
    pet_shop["admin"]["pets_sold"] = (pet_shop["admin"]["pets_sold"] + 2)

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed_to_find):
    pets_matching= []
    for pet in pet_shop["pets"]:
        if breed_to_find == pet["breed"]:
            pets_matching.append(pet["name"])
    return pets_matching
