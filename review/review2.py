from typing import List, Tuple

#   encapsulamento
class Curso:
    def __init__(self: object, nome: str = 'Curso Padrão', carga_horaria: int = 45) -> None:
        self.__nome = nome
        self.__carga_horaria = carga_horaria


curso1: Curso = Curso()
curso2: Curso = Curso(nome="Padrões de Projetos em Python")
curso3: Curso = Curso(nome="Orquestração de Containers com Kubernetes", carga_horaria=23)

# print(curso1.__dict__)
# print(curso2.__dict__)
# print(curso3.__dict__)

#   polimorfismo
nome: str = 'Tanana'
tupla: Tuple = (1, 2, 3, 4, 5)
lista: List = [1, 2, 3, 4, 5]

# print(nome[:4], tupla[:4], lista[:4])

#   heranca
class Pessoa: 
    def __init__(self: object, nome: str) -> None:
        self.__nome = nome

    def andar(self: object) -> None:
        print('Estoy a andar')

class Aluno(Pessoa):
    def __init__(self: object, nome: str, matricula: str) -> None:
        super().__init__(nome)
        self.__matricula = matricula


tais = Aluno("Taís", '12345')
# tais.andar()

#   abstracao
def gerar_fiboacci(qtd: int) -> None:
    if qtd <= 0:
        print("La quantia deve ser maior que zero")
    else:
        print(f'A sequência Fibonacci para {qtd} termo(s) é: ')
        contador: int = 0
        aux1: int = 0
        aux2: int = 1
        while contador < qtd:
            print(aux1)
            proximo = aux1 + aux2
            aux1 = aux2
            aux2 = proximo
            contador += 1

# gerar_fiboacci(10)


#   composicao
class Motor:
    def ligar(self: object) -> None:
        print('Motor ligado...')

class Pneu:

    def enxer(self: object):
        print('Pneu cheio demais po')

#   carro n herda motor/pneu - acesso por composicao 
class Carro:
    def __init__(self: object, modelo: str) -> None:
        self.__modelo = modelo
        self.__motor = Motor()
        self.__pneu1 = Pneu()
        self.__pneu2 = Pneu()
        self.__pneu3 = Pneu()
        self.__pneu4 = Pneu()

fusca = Carro('Fusca')
fusca._Carro__motor.ligar()