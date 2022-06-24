# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    pet_shop_name = pet_shop["name"]
    return pet_shop_name 

def get_total_cash(pet_shop):
    total_cash = pet_shop["admin"]["total_cash"]
    return total_cash

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash
    
def get_pets_sold(pet_shop):
    pets_sold = pet_shop["admin"]["pets_sold"]
    return pets_sold

def increase_pets_sold(pet_shop, sold_pets):
    pet_shop["admin"]["pets_sold"] += sold_pets

def get_stock_count(pet_shop):
    stock_count = 0
    for pets in pet_shop["pets"]:
        stock_count += 1
    return stock_count

def get_pets_by_breed(pet_shop, breed):
    pets_by_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pets_by_breed.append(pet)
    return pets_by_breed