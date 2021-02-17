
my_txt = open("stih.txt")
lines = my_txt.readlines()

for line in lines:
    print(line.strip())

print()
print(f'number of lines is: {len(lines)} ')
print()

my_txt = open("stih.txt")


for  i, num in enumerate(range(len(lines))):
    lines = my_txt.readline()
    lines = lines.split()
    print(f' words in {i + 1} line:  {(len(lines))}')

print()

my_txt = open("stih.txt")
lines = my_txt.read()
lines = lines.split()
print(f'total words: {len(lines)}')

my_txt.close()




