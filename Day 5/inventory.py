category = []
product = []
stocks = []

num_categories = 3
products = 2
inventory = []

for i in range(num_categories):
    cat = input("\nEnter category name: ")
    category.append(cat)

    product = []
    stocks = []

    print("Enter the products available")

    for j in range(products):
        item = input("Enter product name: ")
        stock = int(input("Enter stock: "))

        product.append(item)
        stocks.append(stock)

    inventory.append([cat, product, stocks])

print("\n------ INVENTORY ------")

for data in inventory:
    print(f"\nCategory: {data[0]}")

    for i in range(len(data[1])):
        print(f"{data[1][i]}: {data[2][i]} units")