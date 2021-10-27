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

"""
Chaque action ne peut être achetée qu'une seule fois.

Nous ne pouvons pas acheter une fraction d'action.

Nous pouvons dépenser au maximum 500 euros par client.

"""


# Construction d'un tableau des entiers
n = len(TABLE) #nombre d'actions différentes
table_int = [i for i in range(2**n)]

# Conversion binaire
table_bin = [bin (i) [2:] for i in table_int]

# Tableau des combinaisons
table_combinations = ["0" * (n-len(k)) + k for k in table_bin]

# Recherche des combinaisons pour un maximum de 500 €
expense_max = 500
valid_combinations = []
for combi in table_combinations:
    cost = 0
    benefit = 0
    for i in range(n):
        if combi[i] == "1":
            cost = cost + TABLE[i]["Coût"]
            benefit = benefit + TABLE[i]["Coût"] * TABLE[i]["Bénéfice"]
    performance = cost + benefit
    if cost <= expense_max:
        valid_combinations.append((combi, performance))
        
optimal_soluce = valid_combinations[0][0]
optimal_performance = valid_combinations[0][1]
for combi in valid_combinations:
    if combi[1] > optimal_performance:
        optimal_soluce = combi[0]
        optimal_performance = combi[1]
        
actions_list = []        
for i in range(len(optimal_soluce)):
    if optimal_soluce[i] == "1":
        actions_list.append(TABLE[i]["Actions"])
                
print(f"Meilleure conbinaison d'actions est : {actions_list}")
print(f"La perfomance est de {optimal_performance} €")