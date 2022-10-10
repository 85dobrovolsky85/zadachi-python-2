# Задача 3. Реализуйте алгоритм перемешивания списка. 
# Список размерностью 10 задается случайными целыми числами, 
# выводится на экран, затем перемешивается, опять выводится на экран.
#  SHUFFLE нельзя юзать!
# from random import randint
# l = [[randint(1,1000)] for i in range(10)]

m = []
n = int(input())
for i in range (n):
    m.append(int(input()))
print(m)
m.revers()
print(m)
