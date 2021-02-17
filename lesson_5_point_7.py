import json
firm_dict = {}
avg_prof = []

with open('firm.txt') as f:
    lines = f.readlines()

for el in lines:
    name, firm, rev, costs = el.split() # - выдает здесь ValueError: not enough values to unpack (expected 4, got 0).
    profit = int(rev) - int(costs)      #   Но мы же и даем 4 значения
    firm_dict[name] = profit
    if profit > 0:
        avg_prof.append(profit)
avg_prof = sum(avg_prof) / len(avg_prof)
out = [firm_dict, {'avg_prof': avg_prof}]
print(f'dict {out}')

with open('firm.json', 'w') as f_json:
    json.dump(out, f_json)
with open('firm.json') as f_json:
    print(json.load(f_json))

