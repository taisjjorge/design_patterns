#   imagina que vc tem uma app web que cria diversos perfis em redes sociais automaticamente

from abc import ABCMeta, abstractmethod

class Secao(metaclass=ABCMeta):

    @abstractmethod # metodos abstratos, quem executa sao as classes filhas
    def __repr__(self):
        pass

class SecaoPessoal(Secao):

    def __repr__(self):
        return 'Seção Pessoal'
    
class SecaoAlbum(Secao):

    def __repr__(self):
        return 'Seção Álbum'

class SecaoProjeto(Secao):

    def __repr__(self):
        return 'Seção Projeto'

class SecaoPublicacao(Secao):

    def __repr__(self):
        return 'Seção Publicação'
    

class Perfil(metaclass=ABCMeta):

    def __init__(self):
        self.secoes = []
        self.criar_perfil()

    @abstractmethod
    def criar_perfil(self): # FactoryMethod
        pass

    def get_secoes(self):
        return self.secoes
    
    def add_secao(self, secao):
        self.secoes.append(secao)


class Linkedin(Perfil): # Produto concreto

    def criar_perfil(self):
        self.add_secao(SecaoPessoal())
        self.add_secao(SecaoProjeto())
        self.add_secao(SecaoPublicacao())

class Facebook(Perfil): # Produto concreto

    def criar_perfil(self):
        self.add_secao(SecaoPessoal())
        self.add_secao(SecaoAlbum())


if __name__ == '__main__':
    rede_social = input('Qual rede social quer criar o perfil? [Linkedin, Facebook]: ')

    perfil = eval(rede_social)() # eval pra instanciar obj

    print(f'Criando o perfil no(a) {type(perfil).__name__}')
    print(f'O perfil tem as seções: {perfil.get_secoes()}')