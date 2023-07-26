# toda classe python herda de object
class Singleton(object):
  # metodo new é executado antes de init
  def __new__(cls):
    if not hasattr(cls, 'instance'): # hasattr verifica se a classe possui atributo
      cls.instance = super(Singleton, cls).__new__(cls)
      print(f'Criando o objeto {cls.instance}') # cria apenas uma vez 
    return cls.instance
  
# instancias diferentes mas por usar o singleton tem o mesmo identificador
s1 = Singleton()
print(f'Instancia 1: {id(s1)}')

s2 = Singleton()
print(f'Instancia 2: {id(s2)}')
