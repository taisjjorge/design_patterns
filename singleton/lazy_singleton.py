#   lazy "preguiçoso" - instancia apenas qnd for utilizado
#   padrao lazy utilizado no python usando generators

class Singleton():
  # variavel pra verificar se a instancia ja existe
  __instance = None # atributo de classe inicializado com None

  def __init__(self):
    if not Singleton.__instance:
      print('O método __init__ foi chamado...')
    else:
      print(f'A instancia já foi criada: {self.get_instance()}')

  @classmethod
  def get_instance(cls):
    if not cls.__instance:
      cls.__instance = Singleton()
    return cls.__instance
    
s1 = Singleton() #  a classe é inicializada mas o obj nao é criado

print(f'Objeto criado agora: {Singleton.get_instance()}') # Singleton é criado

s2 = Singleton() # instancia já criada...
