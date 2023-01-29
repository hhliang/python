from random import randint

dies_number = randint(1, 6)
if dies_number == 1:
    result = '唱首歌'
elif dies_number == 2:
    result = '跳個舞'
elif dies_number == 3:
    result = '學狗叫'
elif dies_number == 4:
    result = '做俯臥撐'
elif dies_number == 5:
    result = '念繞口令'
else:
    result = '講冷笑話'
print(result)