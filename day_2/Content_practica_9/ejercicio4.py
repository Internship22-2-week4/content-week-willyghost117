
def bmi (peso, altura):
    bmi = altura*altura
    bmi = round (peso / bmi,2)
    if bmi < 18.5 :
        print(bmi)
        return print('Bajo de peso')

    if bmi >= 18.5 and bmi <= 24.9 :
        print(bmi)
        return print('Normal')

    if bmi >= 25 and bmi <= 29.9:
        print(bmi)
        return print ('Sobrepeso')
    
    if bmi > 30:
        print(bmi)
        return print('Obeso')


bmi(65, 1.8) # "Normal"
bmi(72, 1.6) # "Sobrepeso"
bmi(52, 1.75) # "Bajo de peso"
bmi(135, 1.7) # "Obeso"