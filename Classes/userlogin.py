# -*- coding: utf-8 -*-
"""

"""

import bcrypt
from tkinter import messagebox
from classes.gclass import Gclass

class Userlogin(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0

    
    att = ['_user','_group','_password','_budget','_b_purchased','_c_purchased']
    username = ''
    
    def __init__(self, user, group, password, budget, b_purchased, c_purchased):
        super().__init__()
        
        self._user = user
        self._group = group
        self._password = password
        self._budget = budget
        self._b_purchased = b_purchased
        self._c_purchased = c_purchased
        
        Userlogin.obj[user] = self
        
        Userlogin.lst.append(user)

    
    @property
    def user(self):
        return self._user
    
    @property
    def group(self):
        return self._group
    
    @group.setter
    def group(self, group):
        self._group = group
        
    @property
    def budget(self):
        return self._budget
    
    @property
    def b_purchased(self):
        return self._b_purchased
    
    @property
    def c_purchased(self):
        return self._c_purchased
    
    @budget.setter
    def budget(self, budget):
        self._budget = budget
    
    @b_purchased.setter
    def b_purchased(self, b_purchased):
        self._b_purchased = b_purchased
    
    @c_purchased.setter
    def c_purchased(self, c_purchased):
        self._c_purchased = c_purchased
    
    
    @classmethod
    def chk_password(self, user, password):
        if user in Userlogin.obj:
            obj = Userlogin.obj[user]
            valid = bcrypt.checkpw(password.encode(), obj._password.encode())
            if not valid:
                messagebox.showerror('Error', 'Wrong password')
            return valid
        else:
            messagebox.showinfo('Error', 'No existent user')
            return False
    @classmethod
    def set_password(self, password):
        passencrypted = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return passencrypted.decode()
    
    @classmethod
    def write2(cls, path):
        fh = open(path + 'Userlogin' + '.csv', 'w')
        strprint = ""
        for att in Userlogin.att:
            if att[0] == '_':
                strprint += att[1:] + ';'
            else:
                strprint += att + ';'
        fh.write(strprint[:-1] + '\n')
        for p in Userlogin.obj.values():
            fh.write(p.__str__() + '\n')
        fh.close()