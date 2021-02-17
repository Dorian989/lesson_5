

my_txt = open("one.txt")
lines = my_txt.readlines()

for line in lines:
    print(line.strip())

print()

russian = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
rus_line = [str]
with open("one.txt") as temp:
    for i in temp:
        i = i.split(' ', 1)
        rus_line.append(russian[i[0]] + ' ' + i[1] )

with open('один.txt', 'w') as new_file:
    print(rus_line, file=new_file)
