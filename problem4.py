#Grocery store price checker

key=input("Input an item name within (apple, banana,milk)")
price={'apple': 3,
      'banana': 1,
      'milk': 5
      }
if(key in price):
    print(price[key])
else:
    print("Item not found")