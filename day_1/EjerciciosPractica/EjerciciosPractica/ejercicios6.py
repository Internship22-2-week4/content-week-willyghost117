import copy
countries =  ['mexico','venezuela']
ages = [12, 18]

print(id (ages))
print(id(countries))

countries1 = countries

countries[0]='guatemala'
print(countries1)
print(countries)

countries3 = copy.copy(countries)

countries[0]= 'nuevo'

print(countries)
print(countries1)
print(countries3)

list = [1]
list.append(2)
print(list)

list.pop()
print(list)

b = [1,2,3,4,1,2]
b.sort()
print(b)


c = [1,2,3,4,5]
 
