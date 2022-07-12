def calcularImpuestos ( edad , ingresos ) :
    if edad >= 18 and ingresos >= 1000:
        ingresos = ingresos * 0.40
        return ingresos
    else:
        return 0

print(calcularImpuestos(18,1000))
print(calcularImpuestos(40,10000))
print(calcularImpuestos(17,5000))
print(calcularImpuestos(30,500))


