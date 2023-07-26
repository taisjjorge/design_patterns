
from typing import Any


class University(type):

    def __call__(cls, *args, **kwargs):
        print(f'--- Esses são os argumentos: {args}')
        return type.__call__(cls, *args, **kwargs)
    
#   tem mais controle sobre a classe e a instanciaçao de objs
class Geek(metaclass=University):

    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

obj = Geek(42, 23)

print(obj)