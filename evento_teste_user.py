#-*- coding: utf-8 -*-

"""

"""
from classes.tipos import Tipos
from classes.class_evento import Class_evento
from classes.eventos import Eventos


from forms.openuser import OpenUser

from forms.Form_evento import Form_evento
from forms.FormCompraevento import FormCompraevento
from forms.customer_type_form_Table import Customer_type_form_Table


import tkinter as tk
from tkinter import *




class UserForm(Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry('400x100+100+100')
        self.title('Events Management')
        self.SelectedDiaHora = tk.StringVar()
        self.read_data('data/')
        self.create_menu()
        self.create_frames()
        self.create_buttons()
        self.SelectedDiaHora.set(self.Class_evento.current().dia)
        self.mainloop()   
    
    
    def create_menu(self):

       my_menu = Menu(self)
       self.config(menu = my_menu)
       menu = Menu(my_menu)
       my_menu.add_cascade(label='Menu', menu=menu)
       menu.add_command(label='quit', command = self.app_end)

          
    def read_data(self,filePath):
        Tipos.read(filePath)
        self.Tipos = Tipos
       
        Class_evento.read(filePath)
        self.Class_evento = Class_evento

    def create_frames(self):
        
        self.frame_2 = LabelFrame(self)
        self.frame_2.grid(row=0,column=0,padx=10,pady=10)   
        
    def create_buttons(self):

        
        self.btn_p = Button(self.frame_2, text='Purchases', command=self.open_form_edit_evento)
        self.btn_p.grid(row=0, column=1, padx = 10, pady = 10)
        
        self.btn_p = Button(self.frame_2, text='Show Calendar', command=self.open_form_evento)
        self.btn_p.grid(row=0, column=2, padx = 10, pady = 10)
        
        self.btn_s = Button(self.frame_2, text='Type Events', command=self.open_form_show)
        self.btn_s.grid(row=0, column=0, padx = 10, pady = 10)

        self.btn_q = Button(self, text='Exit', command=self.app_end)
        self.btn_q.grid(row=0, column=2, padx = 10, pady = 10)


       
    def app_end(self):

        self.destroy()


    def open_form_evento(self):
        fshow = Form_evento(self,self.SelectedDiaHora,filePath='data/') 
    
    def open_form_show(self):
        showme = Customer_type_form_Table(self,filePath='data/') 
        
    def open_form_edit_evento(self):
        Fedir = FormCompraevento(self,filePath='data/') 


if __name__ == '__main__':
    ap = UserForm()
    