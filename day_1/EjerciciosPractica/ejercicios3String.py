country = 'Guatemala'
print(country[0])

second_letter = country[1]
third_letter = country[2]
print (second_letter)
print (third_letter)


print(id(second_letter))
print(id(third_letter))

# string inmutable

country_2 = 'Mexico'
country_2 += 's'

print(id(country_2))
print(country_2)
print(id(country_2))

platzi = 'platzi'
print(platzi.upper())
print(platzi.find('a'))
print(platzi.startswith('p'))
print(platzi.startswith('l'))
print(dir(platzi))
help (print)

help(__main__)


