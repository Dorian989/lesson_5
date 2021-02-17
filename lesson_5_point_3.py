my_txt = open("last_name.txt")
lines = my_txt.readlines()

for line in lines:
    print(line.strip())

print()

my_txt = open('last_name.txt', encoding='utf-8')
money = []
min_zp = []
lines = my_txt.readlines()
for i in lines:
    i = i.split()
    if int(i[1]) < 20000:
        min_zp.append(i[0])
        money.append(i[1])
print(f'small:  {min_zp}')
print(f'average {sum(map(int, money)) / len(money)}')
my_txt.close()