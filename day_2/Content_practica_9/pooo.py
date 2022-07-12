import os

class Obra():
    def __init__(self, nombre, autor, fechaCreacion, valor, tipo):
        self._nombre = nombre
        self._autor = autor
        self._fechaCreacion = fechaCreacion
        self._valor = valor
        self._tipo = tipo
    def mostrar1(self):
        print('nombre: ', self._nombre, 'autor: ', self._autor, 'fecha creacion: ', self._fechaCreacion, 'precio: ',self._valor,'tipo: ', self._tipo)

class Tipo ():
    tipo1 = 'escultura'
    tipo2 = 'pintura'
    tipo3 = 'video'
    tipo4 = 'ciencia'
    def mostrar (self):
        print ('1 :',self.tipo1, '2:',self.tipo2,'3:',self.tipo3, '4:',self.tipo4)
        tipoObra=input('selecciona un tipo de obra')
        return tipoObra

class Exposicion ():
    def __init__(self, nombre, fecha, lugar, descripcion, obras):
        self._nombre = nombre
        self._fecha = fecha
        self._lugar = lugar
        self._descripcion = descripcion
        self._obras = obras
    def __repr__(self):
        return str(self.__dict__)

def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('clear') 
	print ("Selecciona una opción")
	print ("\t1 1 - Ingresar Obra")
	print ("\t2 2 - Ingresar Exposicion")
	print ("\t3 3 - Mostrar Obras")
	print ("\t4 4 - Mostrar Exposicion")
	print ("\t9 - salir")
 
if __name__ == '__main__':
	while True:
	# Mostramos el menu
		menu()
 
	# solicituamos una opción al usuario
		opcionMenu = input("inserta un numero valor >> ")
 
		if opcionMenu=="1":
			nombre = input('Nombre : ')
			autor = input('Autor : ')
			fecha = input('Fecha de creacion :')
			valor = input('Valor :')
			tipo=Tipo()
			seleccion = tipo.mostrar()
			obra1 = Obra (nombre,autor,fecha,valor,seleccion)
			obra1.mostrar1()

		elif opcionMenu=="2":
			print ("")
			print('Ingrese los datos de la exposicion')
			nombre = input('Nombre')
			fecha = input ('Autor')
			lugar = input ('lugar')
			descripcion = input( 'Descripcion : ')
			obras = obra1
			exposicion1 = Exposicion (nombre,fecha,lugar,descripcion,obras)

		elif opcionMenu=="3":
			print ("")
			obra1.mostrar1()
			input("Please press the Enter key to proceed")
			obra1.mostrar1()

		elif opcionMenu=="4":
			print(exposicion1)
			input("Please press the Enter key to proceed")

		elif opcionMenu=="9":
			break
		else:
			print ("")
			input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")