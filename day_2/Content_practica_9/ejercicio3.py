def likes (numero) :
    if numero < 1000 :
        return print( '${} likes'. format (numero) )

    if numero  < 999999 :
        numero = numero // 1000
        return print( '${}K likes '.format(numero) )
    else:
        numero = numero // 1000000
        return print( '${}M likes '.format(numero) )

print(likes(983)) # "983"
print(likes(1900)) # "1K"
print(likes(54000)) # "54K"
print(likes(120800)) # "120K"
print(likes(25222444)) # "25M"

