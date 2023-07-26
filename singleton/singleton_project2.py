#   crie apenas uma instancia de sanidadeCheck

class SanidadeCheck:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not SanidadeCheck.__instance:
            SanidadeCheck.__instance = super(SanidadeCheck, cls).__new__(cls, *args, *kwargs)
        return SanidadeCheck.__instance
    
    def __init__(self):
        self.__servidores = []

    def check_servidor(self, servidor):
        print(f'Checando o {self.__servidores[servidor]}')

    def add_servidor(self):
        self.__servidores.append('Servidor 1')
        self.__servidores.append('Servidor 2')
        self.__servidores.append('Servidor 3')
        self.__servidores.append('Servidor 4')

    def mudar_servidor(self):
        self.__servidores.pop()
        self.__servidores.append('Servidor substituto')

sc1 = SanidadeCheck()
sc2 = SanidadeCheck()

sc1.add_servidor()
print('Cronograma de checagem de sanidade de servidores A...')
for servidores in range(4):
    sc1.check_servidor(servidores)

sc2.mudar_servidor()
print('Cronograma de checagem de sanidade de servidores B...')
for servidores in range(4):
    sc2.check_servidor(servidores)

    
