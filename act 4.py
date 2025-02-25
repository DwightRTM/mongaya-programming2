num1 = int(input("Enter an amount in one currency: "))
currency = input("Enter the currency code: (USD, EUR, GBP, INR, AUD, CAD, SGD, CHF, MYR, JPY, CNY, NZD: ) ").lower()
target = input("Enter the target currency code: (USD, EUR, GBP, INR, AUD, CAD, SGD, CHF, MYR, JPY, CNY, NZD: ) ").lower()


exchange_rates ={
    "usd": 1,
    "eur": 0.83,
    "gbp": 0.72,
    "inr": 73.13,
    "aud": 1.29,
    "cad": 1.25,
    "sgd": 1.32,
    "chf": 0.91,
    "myr": 4.05,
    "jpy": 105.92,
    "cny": 6.46,
    "nzd": 1.37,
    "hkd": 7.75,
    "php": 48.51,
    "krw": 1124.16,
    "thb": 30.24,
    "vnd": 23000.00,
    "idr": 14200.00,
    "rub": 73.13,
    "zar": 14.78,
    "brl": 5.23,
}

if currency not in exchange_rates or target not in exchange_rates:
    print("Invalid currency code")

print("Money Converter")

target_money = num1 / exchange_rates[currency] * exchange_rates[target]

print(f"{num1} {currency.upper()} = {target_money} {target.upper()}")