import pytest
from coverageprueba import calculadora

class TestCalculadora:
    def setup_method(self): 
        self.calculador =calculadora()


    @pytest.mark.parametrize("sum1, sum2, result_esperado", [
        (5, 4, 9), # pragma: no cover
        (-6, -8, -14),
        (-8, 4, -4),# pragma: no cover
        (0, 0, 0),
        (2, 0, 2)  
    ])
    def test_suma(self, sum1, sum2, result_esperado):
        assert self.calculador.suma(sum1,sum2) == result_esperado

    @pytest.mark.parametrize("res1,res2,result_esperado",[
        (7,2,5),
        (-5,9,-14),
        (-6,-4,-2),# pragma: no cover
        (5,0,5),
        (0,0,0)


    ])
    def test_resta(self,res1,res2,result_esperado):
        assert self.calculador.resta(res1,res2)==result_esperado
# pragma: no cover
    @pytest.mark.parametrize("dividendo,divisor,res",[
        
        (6,0,None),
        (9,3,3),
        (18,-9,-2),# pragma: no cover
        (100,5,20)
    ])
    def test_division(self,dividendo,divisor,res):
     assert self.calculador.división(dividendo,divisor)==res
# fin de pragma
    @pytest.mark.parametrize("mul1,mul2,resM",[
        (5,5,25),
        (-4,6,-24),
        (-9,-8,72),# pragma: no cover
        (9,0,0),
        (0,0,0)
    ])
    def test_multiplicación(self,mul1,mul2,resM):
        assert self.calculador.multiplicación(mul1,mul2)==resM
    
    @pytest.mark.parametrize("po1,po2,resp",[
        (5,2,25),
        (-8,2,64),
        (2,2,4),# pragma: no cover
        (2,0,1)

    ])
    def test_potenciacion(self,po1,po2,resp):
        assert self.calculador.potenciacion(po1,po2)==resp




