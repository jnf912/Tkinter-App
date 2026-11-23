# -*- coding: utf-8 -*-

"""

"""
import datetime
from datetime import timedelta
from classes.gclass import Gclass

class Class_evento(Gclass):
    
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    
    
    att = ['_code','_diahora','_tipo','_consumiveis','_preco_c','_preco_b']
    
    def __init__(self, code, diahora, tipo, consumiveis, preco_c, preco_b):
        
        self._code = code
        self._diahora = self.str2datetime(diahora)
        self._tipo = tipo
        self._consumiveis = consumiveis
        self._preco_c = preco_c
        self._preco_b = preco_b

        
        Class_evento.obj[code] = self
        Class_evento.lst.append(code)
    
    @property
    def code(self):
        return self._code
    
    @property
    def diahora(self):
        return self._diahora
    
    @property
    def tipo(self):
        return self._tipo
    
    @property
    def consumiveis(self):
        return self._consumiveis
    
    @property
    def preco_c(self):
        return self._preco_c
    
    @property
    def preco_b(self):
        return self._preco_b
    
    
    @property
    def dia(self):
        return self.diahora.date()
    
    @code.setter
    def code(self, code):
        self._code = code
    
    @diahora.setter
    def diahora(self, diahora):
        self._diahora = diahora
    
    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo
    
    @consumiveis.setter
    def consumiveis(self, consumiveis):
        self._consumiveis = consumiveis
        
    @preco_c.setter
    def preco_c(self, preco_c):
        self._preco_c = preco_c
         
    @preco_b.setter
    def preco_b(self, preco_b):
        self._preco_b = preco_b
        
    def str2datetime(self,datestr):
        
        datestr = datestr.replace("/", ";")
        datestr = datestr.replace("-", ";")
        datestr = datestr.replace(":", ";")
        datestr = datestr.replace(" ", ";")
        
        
        
        diahorastr =list(map(int, datestr.split(";")))
        
        
        date = datetime.datetime(diahorastr[0], diahorastr[1], diahorastr[2])
        if len(diahorastr)>3:
            date=date.replace(hour = diahorastr[3])
        if len(diahorastr)>4:
            date=date.replace(minute=  diahorastr[4])
        if len(diahorastr)>5:
            date=date.replace(second = diahorastr[5])
            date.replace
        return date
 

if __name__ == "__main__":    
    
  
    teste = Class_evento(10,'2021/05/16 10:20:30','p2','consumiveis',3,4)
    teste.write()
    print(teste)
      
    