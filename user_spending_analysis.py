import random

users = ["A", "B", "C", "D", "E"]
cats = ["food", "tech", "books", "sports"]

data = []

for _ in range(200):
    data.append({
        "user": random.choice(users),
        "cat": random.choice(cats),
        "amount": random.randint(1, 500)
    })


resultado_parc = {}
resultado = {}

for x in data:
    user = x["user"]
    cat = x["cat"]
    amount = x["amount"]

    if user not in resultado_parc:
        resultado_parc[user] = {
            "total": 0,
            "count": 0,
            "values": [],
            "cats": {

            }
        }

    resultado_parc[user]["total"] += amount
    resultado_parc[user]["count"] += 1
    resultado_parc[user]["values"].append(amount)

    if cat not in resultado_parc[user]["cats"]:
        resultado_parc[user]["cats"][cat] = 0

    resultado_parc[user]["cats"][cat] += amount

for x in resultado_parc:
    user = resultado_parc[x]
    resultado[x] = {
        "total": user["total"],
        "promedio": round((user["total"] / user["count"]), 2),
        "top_3": sorted(user["values"], reverse=True)[:3],
        "cat_max": max(user["cats"], key= lambda k: user["cats"][k]),
        "cat_min": min(user["cats"], key= lambda k: user["cats"][k]),
        "transacciones": user["count"]
    }

print(resultado)
