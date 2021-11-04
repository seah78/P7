import csv
import time

start_time = time.time()

stocks  = []

with open("dataset.csv", "r") as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    for line in reader:
        if line[1] != "price":
            stocks.append({"name": line[0], "price" : float(line[1]), "profit": float(line[2])})


def profit(stock):
    return stock["profit"]

def price(stock):
    return stock["price"]
    
# algorithme glouton

expense_max = 500

def glutton(table, expense_max):
    total_price = 0
    glutton_soluce = []
    i=0
    
    sorted_table =  sorted(table, key=profit, reverse=True)
    
    while i < len(sorted_table) and total_price < expense_max:
        stock = sorted_table[i]
        stock_price = price(stock)
        if total_price + stock_price <= expense_max:
            glutton_soluce.append(stock)
            total_price += stock_price
        i += 1
    return glutton_soluce

def performance(glutton_soluce):
    total_price = 0
    total_profit = 0
    total_performance = 0
    for stock in glutton_soluce:
        total_price += stock["price"]
        total_profit += (stock["price"] * stock["profit"]/100)
    total_performance = total_price + total_profit
    return total_price, total_profit, total_performance    

glutton_soluce = glutton(stocks, expense_max)
total_price, total_profit, total_performance  = performance(glutton_soluce)

print(f" La solution optimisée est {glutton_soluce}")
print(f" Le prix total est de : {total_price} €")
print(f" Le bénéfice est de : {total_profit} €")
print(f" La performance totale est de : {total_performance}")

print("--- %s seconds ---" % (time.time() - start_time))


