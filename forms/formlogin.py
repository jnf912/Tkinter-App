# -*- coding: utf-8 -*-
"""

"""


from tkinter import *

from classes.userlogin import Userlogin
from forms.formuser import Formuser
from forms.openform import OpenForm
from tkinter import messagebox

class FormLogin(Toplevel):
    def __init__(self, root, ncols = 2, filePath = './'):
        super().__init__(root)
        self.protocol("WM_DELETE_WINDOW", self.button_cancel_click)
        root.eval(f'tk::PlaceWindow {str(self)} center')
        self.grab_set()
        self.focus()
        
        self.root = root
        self.filePath = filePath
        self.ncols = 1
        
        self.classObj = Userlogin
        self.classObj.read(self.filePath)
        
        obj = self.classObj.first()
        self.att = self.classObj.att
        
        self.attnames =['Login:','Password:']
        
        self.title('User login')
        
                
           
        self.frame_buttons = Frame(self)
        self.frame_buttons.grid(row=2,column=0)
        
        
        self.frame_edit_button = Frame(self.frame_buttons)
        self.frame_edit_button.grid(row=0,column=0, padx=10)
          
        self.button_login = Button(self.frame_edit_button,text="Login",  command= self.button_login_click)
        self.button_cancel = Button(self.frame_edit_button,text="Cancel",  command= self.button_cancel_click)
        self.button_create = Button(self.frame_edit_button,text="Edit",command= self.button_create_click)
        
        self.button_login.grid(row=0,column=0)
        self.button_cancel.grid(row=0,column=1)
        self.button_create.grid(row=0,column=3)
        self.button_login.bind('<Return>',self.button_login_click)
        self.button_cancel.bind('<Return>',self.button_cancel_click)
        self.button_create.bind('<Return>',self.button_create_click)
        
        
        self.frame_class = LabelFrame(self,text = self.classObj.__name__)
        self.frame_class.grid(row=1,column=0,padx=10,pady=10)
        
        
        self.ent = list()
        r = 0
        c = 0
        for desc in self.attnames:
            lbl = Label(self.frame_class, text=desc)
            lbl.grid(row=r, column=c, padx=10, pady=10)
            c = c + 1
            if desc == 'Password:':
                ent = Entry(self.frame_class, show = '*')
            else:
                ent = Entry(self.frame_class)
            ent.grid(row=r, column=c, padx=10, pady=10)
            self.ent.append(ent)
            if c == 2 * self.ncols - 1:
                r = r + 1
                c = 0
            else:
                c = c + 1

        Userlogin.username = ''
        self.ent[0].focus_set()
        
        self.mainloop()
    
    def cleanForm(self):
        
        for ent in self.ent:
            ent.config(state='normal')
            ent.delete(0, 'end')
    
    def button_login_click(self,event=None):
        
        loginIn = self.ent[0].get()
        passwordIn = str(self.ent[1].get())
        
        if Userlogin.chk_password(loginIn, passwordIn):
            Userlogin.username = loginIn
            self.destroy()
            self.root.destroy()
    
    def button_cancel_click(self,event=None):
       Userlogin.username = ''
       self.destroy()
       self.root.destroy()
    
    def button_create_click(self,event=None):
        loginIn = self.ent[0].get()
        passwordIn = self.ent[1].get()
        if Userlogin.chk_password(loginIn, passwordIn):
            Userlogin.username = loginIn
            flogin = Formuser(self, filePath = 'data/')        
    
     
    

   
   
   
 

