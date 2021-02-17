

with open("nums.txt", "w+") as my_txt2:
    lines = input('enter nums: ')
    my_txt2.writelines(lines)
    my_numb = lines.split()
    print(f' summ nums is: {sum(map(int, my_numb))}')

