from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):

    @abstractmethod
    def falar(self):
        pass

class Cachorro(Animal):

    def falar(self):
        print('Au au!')

class Gato(Animal):

    def falar(self):
        print('Meow!')

class Galinha(Animal):

    def falar(self):
        print('Cocó ricó!')


#   Fábrica
class Factory:

    def criar_animal_falante(self, tipo):
    #   eval: avalia o que for passado e tenta executar como cmd python
        return eval(tipo)().falar() # exemplo: eval('Gato')().falar()
        #return eval(tipo)()
    
#   Cliente
if __name__ == '__main__':
    fab = Factory()
    animal = input('Qual animal você quer que fale? [Cachorro, Gato, Galinha] ')
    fab.criar_animal_falante(animal)



