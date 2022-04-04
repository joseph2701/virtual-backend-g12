import unittest

#siq ueremos ver el detalle del test usamos:: -v

def numero_par(numero:int):
    return numero%2==0

class PruebaTest(unittest.TestCase):
    
    #LA CLASE tESTcASE, PERMITE HACER VARIAS COMAPRACINES A LA VEZ
    def test_sumatoria(self):
        numero1=1
        numero2=2
        resultado=numero1+numero2
        #compara si 1 +2 = 3
        self.assertEqual(resultado,3)

    #se usa este decorador, cuando sabemos que habra un error
    #y no queremos que lo muestre (error esperado)
    @unittest.expectedFailure
    def test_resta(self):
        numero1=1
        numero2=2
        resultado=numero1-numero2
        #compara si 1 +2 = 3
        self.assertEqual(resultado,3)

class NumeroParTest(unittest.TestCase):
    #los metodos deben siemrpe comenzar con test_
   
    def test_par(self):
        #pasaremos u numero
        resultado =numero_par(2)
        self.assertEqual(resultado,True)

    def test_impar(self):
            #pasaremos u numero
            resultado =numero_par(3)
            self.assertEqual(resultado,False)

    def test_error(self):
        '''Debera arrojar un error si se le pasa una letra en vez de un numero'''                
        with self.assertRaises(TypeError, msg='Error al ingresar un caracter en vez de un numero') as error:
            numero_par('a')
        self.assertEqual(error.msg, "Error al ingresar un caracter en vez de un numero")