N = int(input('Введите количество участников олимпиады по математике'))
list_1 = set()
for i in range(1,N+1):
    n=input('Введите участника данной олимпиады')
    list_1.add(n)
print(list_1)
a=len(list_1)
print(a)    



N = int(input('Введите количество участников олимпиады по информатике'))
list_2 = set()
for i in range(1,N+1):
    x=input('Введите участника данной олимпиады')
    list_2.add(x)
print(list_2)
b=len(list_2)
print(b)

N = int(input('Введите количество участников олимпиады по физике'))
list_3 = set()
for i in range(1,N+1):
    z=input('Введите участника данной олимпиады')
    list_3.add(z)
print(list_3)
c=len(list_3)
print(c)

Xex = set.union(list_1, list_2, list_3)
print('Количество участников в трёх олимпиадах:',len(Xex))