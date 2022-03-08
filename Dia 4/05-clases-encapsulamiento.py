class Producto:
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio
        self.__ganancia=self.precio*0.30

    def mostrar_info(self):
        return{
            'nombre': self.nombre,
            'precio': self.precio,
            'ganancia': self.__ganancia,
            # {:.3f} redondea a 3 decimales
            'igv':'{:.3f}'.format(self.__calcular_igv())
        }

    def aumentar_ganancia(self):
        self.__ganancia=self.__ganancia*1.10
    
    def __calcular_igv(self):
        resultado=self.precio*0.18
        return resultado

cepillo=Producto('Cepillo dental',3.80)
#atributo publico
cepillo.nombre
#atributo privado
cepillo.__ganancia=100

print(cepillo.mostrar_info())
cepillo.aumentar_ganancia()
print(cepillo.mostrar_info())
