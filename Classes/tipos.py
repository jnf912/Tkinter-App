# -*- coding: utf-8 -*-
    
"""

"""

from classes.gclass import Gclass

class Tipos(Gclass):
    
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    
    
    att = ['_code','_nomeTipo']
    
    
    def __init__(self, code,nomeTipo):
        super().__init__()
        
        self._code = code
        self._nomeTipo = nomeTipo

        
        Tipos.obj[code] = self
        Tipos.lst.append(code)
    
    @property
    def code(self):
        return self._code
    
    @property
    def nomeTipo(self):
        return self._nomeTipo

    
    
    @code.setter
    def code(self, code):
        self._code = code
    
    @nomeTipo.setter
    def nomeTipo(self, nomeTipo):
        self._nomeTipo = nomeTipo

 
if __name__ == "__main__":    
    
  
    
    teste = Tipos('Futebol','1000')
    teste.write()
    print(teste)
      
    