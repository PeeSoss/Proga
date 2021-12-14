import random
x=random.randint(1,100)
y=-1
while y!=x:
    y=int(input("Угадай число от 1 до 100"))
    if y > x:
        print("Число должно быть меньше")
    elif y < x:
        print("Число должно быть больше")
    else:
        print("Вы угадали, это число = " + str(x))
        break