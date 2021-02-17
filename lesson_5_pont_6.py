obj = {}
with open('dic.txt', 'r') as my_dic:
    lines = my_dic.readlines()

    for el in lines:
       sp_line = el.split()
       sub = sp_line[0]
       sum_lessons = sum([int(x[:x.find('(')]) for x in sp_line[1:] if '(' in x])
       obj[sub[:-1]] = sum_lessons

    print(f'quantity of hours: {obj}')
