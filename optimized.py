import csv
import time

start_time = time.time()



"""
stocks  = []

with open("dataset.csv", "r") as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    for line in reader:
        stocks.append({"name": line[0], "price" : line[1], "profit": line[2]})
"""

TABLE = [{"Actions": "Action-1", "Coût": 20, "Bénéfice": 0.05},
         {"Actions": "Action-2", "Coût": 30, "Bénéfice": 0.10},
         {"Actions": "Action-3", "Coût": 50, "Bénéfice": 0.15},
         {"Actions": "Action-4", "Coût": 70, "Bénéfice": 0.20},
         {"Actions": "Action-5", "Coût": 60, "Bénéfice": 0.17},
         {"Actions": "Action-6", "Coût": 80, "Bénéfice": 0.25},
         {"Actions": "Action-7", "Coût": 22, "Bénéfice": 0.07},
         {"Actions": "Action-8", "Coût": 26, "Bénéfice": 0.11},
         {"Actions": "Action-9", "Coût": 48, "Bénéfice": 0.13},
         {"Actions": "Action-10", "Coût": 34, "Bénéfice": 0.27},
         {"Actions": "Action-11", "Coût": 42, "Bénéfice": 0.17},
         {"Actions": "Action-12", "Coût": 110, "Bénéfice": 0.09},
         {"Actions": "Action-13", "Coût": 38, "Bénéfice": 0.23},
         {"Actions": "Action-14", "Coût": 14, "Bénéfice": 0.01},
         {"Actions": "Action-15", "Coût": 18, "Bénéfice": 0.03},
         {"Actions": "Action-16", "Coût": 8, "Bénéfice": 0.08},
         {"Actions": "Action-17", "Coût": 4, "Bénéfice": 0.12},
         {"Actions": "Action-18", "Coût": 10, "Bénéfice": 0.14},
         {"Actions": "Action-19", "Coût": 24, "Bénéfice": 0.21},
         {"Actions": "Action-20", "Coût": 114, "Bénéfice": 0.18}
]

def profit(stock):
    return stock["Bénéfice"]

def price(stock):
    return stock["Coût"]
    
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
        total_price += stock["Coût"]
        total_profit += (stock["Coût"] * stock["Bénéfice"])
    total_performance = total_price + total_profit
    return total_price, total_profit, total_performance    

glutton_soluce = glutton(TABLE, expense_max)
total_price, total_profit, total_performance  = performance(glutton_soluce)

print(f" La solution optimisée est {glutton_soluce}")
print(f" Le prix total est de : {total_price} €")
print(f" Le bénéfice est de : {total_profit} €")
print(f" La performance totale est de : {total_performance}")

print("--- %s seconds ---" % (time.time() - start_time))
