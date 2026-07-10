list = []
list.extend(["Laptop", "Mouse", "Keyboard"])
print("Current products:", list)

# Insert an urgent product at the end
x = input("Enter an urgent product name: ")
list.insert(len(list), x)
print(list)

# Add a new product
new_prod = input("Enter a new product name: ")
list.append(new_prod)
print(list)

# Remove a product
a = input("Enter a product name to remove: ")
if a in list:
    list.remove(a)
    print(list)
else:
    print(f"{a} is not in the inventory.")

# Ship a product
b = input("Enter a product to be shipped: ")
if b in list:
    print(f"{b} has been shipped.")
    list.remove(b)
    print(list)
else:
    print(f"{b} is not available for shipping.")

# Check quantity
c = input("Enter a product name to check quantity: ")
if c in list:
    print(f"Quantity of {c}: {list.count(c)}")
else:
    print(f"{c} is not in the inventory.")

# Sort products
list.sort()
print("Sorted products:", list)

# Reverse products
list.reverse()
print("Reversed products:", list)

# Copy the list
l = list.copy()
print("Copied products:", l)

# Clear the copied list
l.clear()
print("Cleared copied products:", l)

