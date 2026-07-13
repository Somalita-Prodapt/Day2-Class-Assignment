numbers=list(map(int(input("Enter a list of integer;s seperated by spaces: ").split())))
even_number=list(filter(lambda x: x % 2 ==0, numbers))
square_evens =list(filter(lambda x: x**2, square_evens))
print("Squared even numbers: ",squared_evens)
