"""1. Instala coverage.py.
    2. Crea un archivo con una función
      simple, como multiplicar(a, b), y 
      escribe una prueba unitaria para ella.
    3. Ejecuta las pruebas con cobertura y 
    genera un reporte HTML."""
#    1. Añade más funciones a tu archivo de código
#  y escribe pruebas unitarias para ellas.
   # 2. Utiliza coverage.py para medir qué porcentaje 
   # del código es cubierto por las pruebas.
   # 3. Examina el reporte HTML generado y busca áreas 
   # del código que no están siendo cubiertas por las pruebas
"""  1. Configura coverage.py para que excluya las líneas 
de código que contienen comentarios o docstrings.
    2. Añade pruebas parametrizadas utilizando pytest y observa 
    cómo la cobertura de código se ve reflejada en los reportes.
    3. Implementa pruebas adicionales para casos extremos, como
      entradas no válidas.""" 

class calculadora:
    def __init__(self):
        self.resultado=0

    
    def suma(self,n1,n2):
        self.resultado=n1+n2
        return self.resultado # pragma: no cover
    
    def resta(self,n1,n2):
        self.resultado=n1-n2
        return self.resultado

    
    def división(self,dividendo,divisor):
        if divisor ==0:
            return None
        else:
            return dividendo/divisor
        
    def multiplicación(self,n1,n2):
        self.resultado=n1*n2
        return self.resultado
    
    def potenciacion(self,n1,n2):
        self.resultado=n1**n2
        return self.resultado
    
        
    """def opción(op,n1,n2):
        if(op==1):
            suma(n1,n2)"""


    





        


