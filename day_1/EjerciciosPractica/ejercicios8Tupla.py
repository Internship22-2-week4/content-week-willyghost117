"""
a = 1, 1,1, 2, 3
print(type(a))

print(a.count(1))
print(a.count(2))
print(a.index(2))
"""
a = set ([1,2,3])

b= {3,4,4}

print(type(a))
print(type(b))

print(b)
a.add(3)
print(a)

a.add(4)
print(a)

print(a.difference(b))
a.remove(4)
print(a)

lista_numeros = list(range(100))

print (lista_numeros)

pares = [numeros for numeros in lista_numeros if numeros % 2 == 0]

print(pares)

student_uid = [1,2,3]

students = ['juand', 'pedro','ricardo']

student_whith_id = { uid : student for uid, student in zip (student_uid, students)}

print(student_whith_id)


import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1,4))

print(random_numbers)

non_repetead = {number for number in random_numbers}

print(non_repetead)




