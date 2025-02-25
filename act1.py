#Write a function create_car(brand, model, year) 
#that returns a dictionary representing a car with keys "brand", "model", and "year". 
# Include a conditional that prints a message if the car is older than 2000.

def create_car():
    try:
        brand = input("Enter a brand:")
        model = input("Enter a model:")
        year = int(input("Enter a year:"))
    
    except KeyboardInterrupt:
        print("Try agian: ")
        return create_car()
    except ValueError: 
        print("Please enter a valid year: ")
        return create_car()        


    print(f"Brand: {brand}")
    print(f"Model: {model}")
    print(f"Year: {year}")

    dict = {
        "brand": brand,
        "model": model,
        "year": year
    }

    if year < 2000:
        print("This car is older than 2000")

create_car()