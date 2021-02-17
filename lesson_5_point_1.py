with open("my_txt.txt", "w") as my_txt:
    print("asd\n", "rtyu\n", "cvb\n", file = my_txt)

my_txt = open("my_txt.txt")
lines = my_txt.readlines()

for line in lines:
    print(line.strip())

my_txt.close()

