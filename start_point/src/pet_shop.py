# WRITE YOUR FUNCTIONS HERE

cc_pet_shop = {
    "pets": [
        {
            "name": "Sir Percy",
            "pet_type": "cat",
            "breed": "British Shorthair",
            "price": 500
        },
        {
            "name": "King Bagdemagus",
            "pet_type": "cat",
            "breed": "British Shorthair",
            "price": 500
        },
        {
            "name": "Sir Lancelot",
            "pet_type": "dog",
            "breed": "Pomsky",
            "price": 1000,
        },
        {
            "name": "Arthur",
            "pet_type": "dog",
            "breed": "Husky",
            "price": 900,
        },
        {
            "name": "Tristan",
            "pet_type": "cat",
            "breed": "Basset Hound",
            "price": 800,
        },
        {
            "name": "Merlin",
            "pet_type": "cat",
            "breed": "Egyptian Mau",
            "price": 1500,
        }
    ],
    "admin": {
        "total_cash": 1000,
        "pets_sold": 0,
    },
    "name": "Camelot of Pets"
}

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

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet

def remove_pet_by_name(pet_shop, pet_name):
    pet_to_remove = find_pet_by_name(pet_shop, pet_name)
    pet_shop["pets"].remove(pet_to_remove)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]: 
        return True 
    else: 
        return False
        
def sell_pet_to_customer(pet_shop, pet, customer):
    if pet != None and customer_can_afford_pet(customer, pet):
        remove_pet_by_name(pet_shop, pet["name"])
        add_pet_to_customer(customer, pet)
        increase_pets_sold(pet_shop, 1)
        get_pets_sold(pet_shop)
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(pet_shop, pet["price"])





    
