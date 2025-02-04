foods = []
prices = []
total = 0 

while True :
    food = input("Enter name of food to buy (Enter q to Quit): ")
    if food.lower() == 'q':
        break 
    else: 
        price = float(input("Enter the price of Food item {food} : "))
        foods.append(food)
        prices.append(price)

print("--------Your Cart--------")
for food in foods :
    print(food , end=" " )
for price in prices :
    total += price
print (" ")
print("Total value of cart is :" , total) 




