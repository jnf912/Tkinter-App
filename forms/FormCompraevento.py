# -*- coding: utf-8 -*-
"""

"""



import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import datetime
from datetime import timedelta


from forms.Form_evento import Form_evento
from forms.formuser import Formuser

# ipmort class to form
from classes.class_evento import Class_evento

from classes.tipos import Tipos

from classes.userlogin import Userlogin




class FormCompraevento(Toplevel):
    def __init__(self, myroot, filePath = './'):
        super().__init__(myroot)
        self.myroot = myroot
        self.consumiveis_iniciais = -1
       
        self.filePath = filePath
        self.selecteddateTime = tk.StringVar()
        
        
        self.read_data()
        
        self.conf_windows() 
        self.create_frames()
        self.create_buttons()
        self.create_entries()
          
        
        
    
       
      
        self.config_mode("Show")
        
        self.showObject("C")
        
        

        self.mainloop()
    
    def app_end(self):

        self.destroy()
        
    
    def read_data(self):
        Tipos.read(self.filePath)
        self.Tipos = Tipos

        
        Class_evento.read(self.filePath)
        self.Class_evento = Class_evento
        
        
    
    def conf_windows(self):
        self.statusText=''
        
        
        self.title('Tickets/Consumables Purchases')
        
        
        
    def create_frames(self):
          
        self.frame_main = Frame(self)
        self.frame_main.grid(row=0,column=0)
    
       
        self.frame_buttons = Frame(self.frame_main)
        self.frame_buttons.grid(row=0,column=0)
        
         
        self.frame_move_button = Frame(self.frame_buttons)
        self.frame_move_button.grid(row=0,column=0, padx=10)
        
        
        
         
        self.frame_class = LabelFrame(self,text ='Class evento')
        self.frame_class.grid(row=2,column=0,padx=10,pady=10)
        
        self.create_status(self)
        
    def create_buttons(self):
      
        self.create_navigation_buttons()
        
        self.create_edit_buttons()
        
    def create_status(self,frame):
        
        
        
        self.frame_status = Label(frame,bd=1,relief=SUNKEN)
        self.frame_status.grid(row=22,column=0,sticky=W+E)
        
        self.lb_status = Label(self.frame_status,text= "Status" , bd=1,relief=SUNKEN)
        self.lb_status.grid(row=0, column=0,  pady=10, sticky=W+E)
        
        
    
    def create_navigation_buttons(self):
         
        self.button_first = Button(self.frame_move_button,text="<<",  command= lambda: self.showObject('F'))
        self.button_back = Button(self.frame_move_button,text="<",  command= lambda: self.showObject('P'))
        self.button_next = Button(self.frame_move_button,text=">",command= lambda: self.showObject('N'))
        self.button_last = Button(self.frame_move_button,text=">>",command= lambda: self.showObject('L'))
        
        self.button_first.grid(row=0,column=0)
        self.button_back.grid(row=0,column=1)
        self.button_next.grid(row=0,column=3)
        self.button_last.grid(row=0,column=4)
        
        
         
        self.button_exit = Button(self.frame_buttons,text="Exit",command=self.app_end)
        self.button_exit.grid(row=0,column=5,padx=10)
        
    def create_edit_buttons(self):
        
        self.button_comprar = Button(self.frame_class,height=2, width=20,text="Buy",command= lambda: self.button_comprar_click())
        self.button_comprar.grid(row=4,column=4, padx=10, pady=10)
        self.button_reservar = Button(self.frame_class, height=2, width=20, text="Book", command= lambda: self.button_reservar_click())
        self.button_reservar.grid(row=3,column=4, padx=10, pady=10)
        
    def create_entries(self):
        
        
        
        self.lb_code = Label(self.frame_class,text = 'Code :')
        self.en_code = Entry(self.frame_class)
        
        
        self.lb_diahora = Label(self.frame_class,text = 'Day & Hour :')
        self.en_diahora = Entry(self.frame_class,textvariable=self.selecteddateTime)
        
        self.lb_consumiveis = Label(self.frame_class,text = 'Consumables :')
        self.consumiveis_var = StringVar()
        self.en_consumiveis = Entry(self.frame_class, textvariable=self.consumiveis_var)
        
        self.lb_bilhetes_comprar = Label(self.frame_class,text = 'Tickets to buy :')
        self.bilhetes_comprar_var = StringVar()
        self.en_bilhetes_comprar = Entry(self.frame_class, textvariable=self.bilhetes_comprar_var)
        
        self.lb_consumiveis_comprar = Label(self.frame_class,text = 'Consumables to buy :')
        self.consumiveis_comprar_var = StringVar()
        self.en_consumiveis_comprar = Entry(self.frame_class, textvariable=self.consumiveis_comprar_var)
            
        self.lb_preco_b = Label(self.frame_class,text = 'Price of Tickets :')
        self.en_preco_b = Entry(self.frame_class)
        
        self.lb_preco_c = Label(self.frame_class,text = 'Price of Consumables :')
        self.en_preco_c = Entry(self.frame_class)
        
        
        self.lb_code.grid(row=0, column=0, padx=10, pady=10)
        self.en_code.grid(row=0, column=1, padx=10, pady=10)
     
        self.lb_diahora.grid(row=0, column=2, padx=10, pady=10)
        self.en_diahora.grid(row=0, column=3, padx=10, pady=10)
        
        self.lb_consumiveis.grid(row=1, column=0, padx=10, pady=10)
        self.en_consumiveis.grid(row=1, column=1, padx=10, pady=10)
        
        self.lb_bilhetes_comprar.grid(row=3, column=2, padx=10, pady=10)
        self.en_bilhetes_comprar.grid(row=3, column=3, padx=10, pady=10)
        
        self.lb_consumiveis_comprar.grid(row=4, column=2, padx=10, pady=10)
        self.en_consumiveis_comprar.grid(row=4, column=3, padx=10, pady=10)
         
        self.lb_preco_b.grid(row=3, column=0, padx=10, pady=10)
        self.en_preco_b.grid(row=3, column=1, padx=10, pady=10)
         
        self.lb_preco_c.grid(row=4, column=0, padx=10, pady=10)
        self.en_preco_c.grid(row=4, column=1, padx=10, pady=10)
         
         
        l1 = tk.Label(self.frame_buttons,  textvariable=self.selecteddateTime )
        l1.grid(row=3,column=0) 
        

        
        

        
        self.createCombosTipo()
        
        
    
    def createCombosTipo(self):
        
        self.lb_codTipo = Label(self.frame_class,text = 'Type of event :') 
        self.lb_codTipo.grid(row=2, column=0, padx=10, pady=10)
        self.lb_Tipo = Label(self.frame_class,text = 'Capacity :')
        self.lb_Tipo.grid(row=2, column=2, padx=10, pady=10)

        
        listToCombo = self.Tipos.lst
        self.selectedValue = StringVar()
        self.Combo_Tipo_cod = ttk.Combobox(self.frame_class,textvariable = self.selectedValue)
        self.Combo_Tipo_cod['values'] = listToCombo
        self.Combo_Tipo_cod.bind('<<ComboboxSelected>>', self.SelectedCombo_Tipo_cod)
        self.Combo_Tipo_cod.current(0)
        
        listToCombo = self.Tipos.getatlist('nomeTipo')
        self.Combo_Tipo_name = ttk.Combobox(self.frame_class)
        self.Combo_Tipo_name['values'] = listToCombo
        self.Combo_Tipo_name.bind('<<ComboboxSelected>>', self.SelectedCombo_Tipo_name)
        self.Combo_Tipo_name.current(0)
    
        self.Combo_Tipo_cod.grid(row=2,column=1,sticky = W)
        self.Combo_Tipo_name.grid(row=2,column=3,sticky = W)
 
        
    def SelectedCombo_Tipo_cod(self,event):
        self.Combo_Tipo_name.current( self.Combo_Tipo_cod.current())
        self.SelectedCombo_Tipo()
        
    def SelectedCombo_Tipo_name(self,event):
        self.Combo_Tipo_cod.current( self.Combo_Tipo_name.current())
        self.SelectedCombo_Tipo()
       
    
    def SelectedCombo_Tipo(self):
        self.visible_object.tipo = self.Combo_Tipo_cod.get()
        self.showObject("C")
        
        
        
    
    def Creat_newobj_from_Entry(self):
        return self.Class_evento(self.en_code.get(),self.selecteddateTime.get(),#self.en_diahora.get(),
                                 self.Combo_Tipo_cod.get(), self.en_consumiveis.get(), self.en_preco_c.get(), self.en_preco_b.get())


    
    def upadate_my_object(self,objet):
        objet.code = self.en_code.get()
        objet.diahora = self.selecteddateTime.get()
        
        objet.tipo = self.Combo_Tipo_cod.get()
        
        objet.consumiveis = self.en_consumiveis.get()
        objet.preco_c = self.en_preco_c.get()
        objet.preco_b = self.en_preco_b.get()
      
    
    def cleanForm(self):
        
        children_widgets = self.frame_class.winfo_children()
        for child_widget in children_widgets:
            if child_widget.winfo_class() == 'Entry':
                child_widget.delete(0,END)
    
    def update_utilizador(self, gasto, b_comprou, c_comprou):
		
        user0 = Userlogin.username
        
        diferença = float(Userlogin.obj[user0].budget) - float(gasto)
        Userlogin.obj[user0].budget = str(diferença)
        Userlogin.obj[user0].b_purchased = str(int(Userlogin.obj[user0].b_purchased) + int(b_comprou))
        Userlogin.obj[user0].c_purchased = str(int(Userlogin.obj[user0].c_purchased) + int(c_comprou))
        
    def pode_comprar(self, gasto, b_comprou, c_comprou):
        user0 = Userlogin.username
        
        diferença = float(Userlogin.obj[user0].budget) - float(gasto)
        if diferença >= 0:
            return True
        else:
            return False
    
            
    def button_reservar_click(self):
        user = Userlogin.username
    
        
        if int(self.en_consumiveis_comprar.get()) != 0:
            restantes = int(self.en_consumiveis.get()) - int(self.en_consumiveis_comprar.get())
            if restantes >= 0:
                self.consumiveis_var.set(restantes)
                messagebox.showinfo('Booked', 'Use "Buy" to complete your transactions.')
            else:
                messagebox.showerror('Error', 'You cannot buy more consumables than the ones available.')
        
    
    def button_comprar_click(self):
        
        self.upadate_my_object(self.visible_object)
        
        gastou = (int(self.en_bilhetes_comprar.get()) * float(self.en_preco_b.get())) + (int(self.en_consumiveis_comprar.get()) * float(self.en_preco_c.get()))
        
        self.update_utilizador(gastou, self.en_bilhetes_comprar.get(), self.en_consumiveis_comprar.get())
        
        if self.pode_comprar(gastou, self.en_bilhetes_comprar.get(), self.en_consumiveis_comprar.get()) == True:
            if gastou == 0 or self.en_consumiveis.get() == self.consumiveis_iniciais:
                messagebox.showinfo('Try again', 'You did not book a ticket or a consumable.')
            else:
                Userlogin.write2(self.filePath)
                    
                self.Class_evento.write(self.filePath)
                
                self.visible_object=self.Class_evento.current() 
               
                self.config_mode("Show")
                
                messagebox.showinfo('Purchased', 'Successful transaction.')
            
        else:
            messagebox.showerror('Error', 'Não tem fundos suficientes para realizar a transação')
        
    def button_save_click(self):
        
        if self.visible_object == None:
            
            self.visible_object = self.Creat_newobj_from_Entry()
            self.visible_object=self.Class_evento.last() 
        else:
            
            self.upadate_my_object(self.visible_object)
            
        
        self.Class_evento.write(self.filePath)
        
        self.visible_object=self.Class_evento.current() 
       
        self.config_mode("Show")
        
        
    def str2datetime(self,datestr):
        
        datestr = datestr.replace("/", ";")
        datestr = datestr.replace("-", ";")
        datestr = datestr.replace(":", ";")
        datestr = datestr.replace(" ", ";")
        
        
        diahorastr =list(map(int, datestr.split(";")))
        
        
        date = datetime.datetime(diahorastr[0], diahorastr[1], diahorastr[2])
        
        return date.date()
     
    def button_evento_click(self):
        h1 = Form_evento(self,self.selecteddateTime,filePath='Data/')
 
        
            
    def button_cancel__click(self):
       
        self.visible_object=self.Class_evento.current() 
        self.config_mode("Show")
        self.showObject("P")
        

    
    def config_mode(self,mode):
        
        
        if mode == "Show":
            self.button_first['state'] = "normal"
            self.button_back['state'] = "normal"
            self.button_next['state'] = "normal"
            self.button_last['state'] = "normal"
            
            self.button_exit['state'] = "normal"
            
    
    
    def objectToEntrys(self):
        self.en_code['state'] = "normal"
        
        self.en_code.delete(0,END)
        self.en_code.insert(0, self.visible_object.code)
        
        self.en_code['state'] = "disabled"
        
        self.en_diahora['state'] = ["normal"]
        
        self.en_diahora.delete(0,END)
        self.en_diahora.insert(0, self.visible_object.diahora)
        self.selecteddateTime.set( self.visible_object.diahora)
        
        self.en_diahora['state'] = ["disable"]
        
        self.en_consumiveis['state'] = "normal"
        
        self.en_consumiveis.delete(0,END)
        self.en_consumiveis.insert(0, self.visible_object.consumiveis)
        
        self.en_consumiveis['state'] = "disable"
        
        self.Combo_Tipo_cod['state'] = "normal"
        
        self.Combo_Tipo_cod.set(self.visible_object.tipo)
        
        self.Combo_Tipo_cod['state'] = "disable"
        
        self.Combo_Tipo_name['state'] = "normal"
        
        self.Combo_Tipo_name.set(self.visible_Tipo_obj.nomeTipo)
        
        self.Combo_Tipo_name['state'] = "disable"
        
        self.en_preco_c['state'] = "normal"
        
        self.en_preco_c.delete(0,END)
        self.en_preco_c.insert(0,self.visible_object.preco_c)
        
        self.en_preco_c['state'] = "disable"
        
        self.en_preco_b['state'] = "normal"
        
        self.en_preco_b.delete(0,END)
        self.en_preco_b.insert(0,self.visible_object.preco_b)
        
        self.en_preco_b['state'] = "disable"
        
        self.bilhetes_comprar_var.set(0)
        
        self.consumiveis_comprar_var.set(0)
        
        self.consumiveis_iniciais = self.en_consumiveis.get()
       
    
    def showObject(self,option):
        # C - current
        # F - first
        # P - previous
        # N - next
       
        
        
        option = option.upper()
       
        if option == 'C':
            self.visible_object=self.Class_evento.current()
            
        elif  option == 'F':
            self.visible_object=self.Class_evento.first()
            
        elif  option == 'P':
            self.visible_object=self.Class_evento.previous()
            if self.visible_object == None:
                self.visible_object=self.Class_evento.first()
                
        elif  option == 'N':
            self.visible_object=self.Class_evento.nextrec()
            if self.visible_object == None:
                self.visible_object=self.Class_evento.last()
                
        elif  option == 'L':
            self.visible_object=self.Class_evento.last()
            
        self.visible_Tipo_obj = Tipos.obj[self.visible_object.tipo]
        
        self.objectToEntrys()
        
        
 

   

def teste():
    
    root = Tk()
    f = FormCompraevento(root)
     
   



if __name__ == "__main__":
    teste()