# -*- coding: utf-8 -*-
"""

"""


from classes.gclass import Gclass

class Eventos(Gclass):
    
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    
    
    att = ['_code','_capacidade','_patrocionador']
    
    
    def __init__(self, code,capacidade,patrocionador):
        super().__init__()
        
        self._code = code
        self._capacidade = capacidade
        self._patrocionador = patrocionador

        
        Eventos.obj[code] = self
        Eventos.lst.append(code)
    
    @property
    def code(self):
        return self._code
    
    @property
    def capacidade(self):
        return self._capacidade
    
    @property
    def patrocionador(self):
        return self._patrocionador

    
    
    @code.setter
    def code(self, code):
        self._code = code
    
    @capacidade.setter
    def capacidade(self, capacidade):
        self._capacidade = capacidade
        
    @patrocionador.setter
    def patrocionador(self, patrocionador):
        self._patrocionador = patrocionador

 
if __name__ == "__main__":    
    

    teste = Eventos('Futebol',2000,'Nos')
    teste.write()
    print(teste)