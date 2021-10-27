table = [{"Actions": "Action-1", "Coût": 20, "Bénéfice": 0.05},
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


n = len(table) #nombre d'actions
tab_int = [i for i in range(2**n)]
print(tab_int)                               