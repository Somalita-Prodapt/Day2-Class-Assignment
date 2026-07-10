stores=3
days=7
for store in range(stores):
    total_sales=0
    for day in range(1, days+1):
        sales=int(input(f"Enter the sales of the day {day}: "))
        total_sales+=sales
    print(f"Total sales for Store {store+1}: {total_sales}")    