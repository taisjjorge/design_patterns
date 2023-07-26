#   instancias diferentes, mas mesmo estado

class Monostate:

    __state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__state
        return obj
    
m1 = Monostate()
print(f'M1 id: {id(m1)}')
print(m1.__dict__)

m2 = Monostate()
print(f'M2 id: {id(m2)}')
print(m2.__dict__)

m1.nome = 'tatá'

print(f'M1: {m1.__dict__}\nM2: {m2.__dict__}')