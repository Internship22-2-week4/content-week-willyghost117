#operadores
def operadores(num,num2):
    print(num+num2)
    print(num-num)
    print(num*num2)
    print(num/num2)
    print(num//num2)
    print(2**8)
    print(type(num))
    decimal = 1.1
    print(type(decimal))
    print('a'+'b')
    print('b'*5)
    print('palabra'*3)
    decimal += decimal + 5
    print(decimal)


#  operadores(1,2)

#  variables y expresiones

message = 'Hola mundo'
_age = 20 #  variable privada pero solo es por convencion
PI = 3.14159 #  variable constante pero solo por convencion
__do_not_touch = 'something important'

print(message,_age,PI,__do_not_touch)

#reasignar
my_var = 2
my_var = my_var * 5
print(my_var)

entero = int ('5')
print(entero)

a = bool('a')
b = bool('')

print(a,b)

c = float(5)

print(c)

def suma(x,y):
    return x+y

# suma(2,3)

# print(type(suma))

total = suma(10,10)
print(total)






