# -*- coding: utf-8 -*-
"""

"""




import tkinter as tk
from tkinter import *
from tkinter import ttk
import datetime
from datetime import timedelta
from forms.Form_evento import Form_evento
from classes.class_evento import Class_evento
from classes.tipos import Tipos




class FormEditevento(Toplevel):
    def __init__(self, myroot, filePath = './'):
        super().__init__(myroot)
        self.myroot = myroot
       
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
        self.Class_evento = Class_evento
        
        
    
    def conf_windows(self):
        
        self.statusText=''
        self.title('Events booking')
        
        
        
    def create_frames(self):
          
        self.frame_main = Frame(self)
        self.frame_main.grid(row=0,column=0)
    
         
        self.frame_buttons = Frame(self.frame_main)
        self.frame_buttons.grid(row=0,column=0)
        
         
        self.frame_move_button = Frame(self.frame_buttons)
        self.frame_move_button.grid(row=0,column=1, padx=10)
        
        
        self.frame_edit_button = Frame(self.frame_buttons)
        self.frame_edit_button.grid(row=0,column=0, padx=10)
        
         
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
        
        
        self.button_edit = Button(self.frame_edit_button,text="Edit",  command= lambda: self.button_edit_click())
        self.button_delete = Button(self.frame_edit_button,text="Delete",  command= lambda: self.button_delete_click())
        self.button_insert = Button(self.frame_edit_button,text="Insert",command= lambda: self.button_insert_click())
        self.button_save = Button(self.frame_edit_button,text="Save",command= lambda: self.button_save_click())
        self.button_cancel = Button(self.frame_edit_button,text="Cancel",command= lambda: self.button_cancel__click())
        
        self.button_edit.grid(row=0,column=0)
        self.button_delete.grid(row=0,column=1)
        self.button_insert.grid(row=0,column=3)
        self.button_save.grid(row=0,column=4)
        self.button_cancel.grid(row=0,column=5)    
        
        self.evento_Show = Button(self.frame_edit_button,text="Calendar",  command= lambda: self.button_evento_click())
        self.evento_Show.grid(row=0,column=7)

        
    
    def create_entries(self):
        
        
        
        self.lb_code = Label(self.frame_class,text = 'Code :')
        self.en_code = Entry(self.frame_class)
        
        
        self.lb_diahora = Label(self.frame_class,text = 'Day & Hour :')
        self.en_diahora = Entry(self.frame_class,textvariable=self.selecteddateTime)
        
        self.lb_consumiveis = Label(self.frame_class,text = 'Consumables :')
        self.en_consumiveis = Entry(self.frame_class)
        
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
         
        self.lb_preco_b.grid(row=3, column=0, padx=10, pady=10)
        self.en_preco_b.grid(row=3, column=1, padx=10, pady=10)
         
        self.lb_preco_c.grid(row=3, column=2, padx=10, pady=10)
        self.en_preco_c.grid(row=3, column=3, padx=10, pady=10)
         
         
        
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
        self.Combo_Tipo_name.current(self.Combo_Tipo_cod.current())
        self.SelectedCombo_Tipo()
        
    def SelectedCombo_Tipo_name(self,event):
        self.Combo_Tipo_cod.current(self.Combo_Tipo_name.current())
        self.SelectedCombo_Tipo()
       
    
    def SelectedCombo_Tipo(self):
        self.visible_object.tipo = self.Combo_Tipo_cod.get()
        self.showObject("C")
        

    def Creat_newobj_from_Entry(self):
        return self.Class_evento(self.en_code.get(),self.selecteddateTime.get(),#self.en_diahora.get(),
                                 self.Combo_Tipo_cod.get(), self.en_consumiveis.get(), self.en_preco_b.get(), self.en_preco_c.get())


    
    def upadate_my_object(self,objet):
        objet.code = self.en_code.get()
        objet.diahora = self.selecteddateTime.get()
        objet.tipo = self.Combo_Tipo_cod.get()
        objet.consumiveis = self.en_consumiveis.get()
        objet.preco_b = self.en_preco_b.get()
        objet.preco_c = self.en_preco_c.get()
    
    def cleanForm(self):
        
        children_widgets = self.frame_class.winfo_children()
        for child_widget in children_widgets:
            if child_widget.winfo_class() == 'Entry':
                child_widget.delete(0,END)
                
            
        
    
    def button_edit_click(self):
        self.config_mode("Edit")
    
    def button_delete_click(self):
        
        self.Class_evento.remove(self.visible_object.code)
        self.config_mode("Show")
        self.showObject("P")
    
    def button_insert_click(self):
        
        self.visible_object = None
        self.config_mode("Edit")
        self.cleanForm()
        self.selecteddateTime.set(datetime.datetime.now().date())
        
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
            
            self.button_edit['state'] = "normal"
            self.button_delete['state'] = "normal"
            self.button_insert['state'] = "normal"
            self.button_save['state'] = "disabled"
            self.button_cancel['state'] = "disabled"
            self.evento_Show['state'] = "disabled"
            
            self.button_exit['state'] = "normal"
            
        elif mode == "Edit":
            self.button_first['state'] = "disabled"
            self.button_back['state'] = "disabled"
            self.button_next['state'] = "disabled"
            self.button_last['state'] = "disabled"
            
            self.button_edit['state'] = "disabled"
            self.button_delete['state'] = "disabled"
            self.button_insert['state'] = "disabled"
            self.button_save['state'] = "normal"
            self.button_cancel['state'] = "normal"
            self.evento_Show['state'] = "normal"
            
            self.button_exit['state'] = "disabled"           
           

    
    
    def objectToEntrys(self):
        self.en_code.delete(0,END)
        self.en_code.insert(0, self.visible_object.code)
        
        
        self.selecteddateTime.set( self.visible_object.diahora)
        
        self.en_consumiveis.delete(0,END)
        self.en_consumiveis.insert(0, self.visible_object.consumiveis)
        
        self.en_preco_b.delete(0,END)
        self.en_preco_b.insert(0, self.visible_object.preco_b)
        
        self.en_preco_c.delete(0,END)
        self.en_preco_c.insert(0, self.visible_object.preco_c)

        
        self.Combo_Tipo_cod.set(self.visible_object.tipo)
        self.Combo_Tipo_name.set(self.visible_Tipo_obj.nomeTipo)
        
    
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
    f = FormEditevento(root)
     
   



if __name__ == "__main__":
    teste()