import sys
rae = {}
rae ['pizza'] = 'La comida mas deliciosa del mundo'

print(rae)

print(rae['pizza'])

print(rae.get('helado',None))
print(rae.get('pizza',None))

print(rae.keys())
print(rae.items())

for key in rae.values():
    print(key)

for key, value in rae.items():
    print(key, value)



