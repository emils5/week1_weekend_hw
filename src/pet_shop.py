# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_cash(pet_shop, cash_amount):
    pet_shop["admin"]["total_cash"] += cash_amount
    # pet_shop["admin"]["total_cash"] = (pet_shop["admin"]["total_cash"] + cash_amount)

def remove_cash(pet_shop, cash_amount):
    pet_shop["admin"]["total_cash"] += cash_amount
    
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, pets_sold):
    pet_shop["admin"]["pets_sold"] = (pet_shop["admin"]["pets_sold"] + pets_sold)

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed_to_find):
    pets_matching= []
    for pet in pet_shop["pets"]:
        if breed_to_find == pet["breed"]:
            pets_matching.append(pet["name"])
    return pets_matching

def get_pets_by_breed_non_found(pet_shop, breed_to_find):
    pets_matching= []
    for pet in pet_shop["pets"]:
        if breed_to_find == pet["breed"]:
            pets_matching.append(pet["name"])
    return pets_matching

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet_name == pet["name"]:
            return pet

def find_pet_by_name_None(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet_name == pet["name"]:
            return pet
        else: 
            print("None")
# returns None

def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet_name == pet["name"]:
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customers):
    return customers["cash"]
    # return customers[0]["cash"]

def remove_customer_cash(customers, cash_amount):
    customers["cash"] -= cash_amount


def get_customer_pet_count(customers):
    return len(customers["pets"])

def add_pet_to_customer(customers, new_pet):
    customers["pets"].append(new_pet)

# def customer_can_afford_pet(pet_shop, customers):
#     for customer in customers:
#         for pet in pet_shop["pets"]:
#             if customer["cash"]>= pet["price"]:
#                 return True

def customer_can_afford_pet(customer, pets):
    if customer["cash"]>= pets["price"]:
        return True
    else:
        return False



        












        
