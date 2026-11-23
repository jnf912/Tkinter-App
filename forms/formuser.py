# -*- coding: utf-8 -*-
"""

"""
from classes.userlogin import Userlogin
from tkinter import *
from tkinter import ttk
import os
from PIL import ImageTk,Image

class Formuser(Toplevel):
    def __init__(self, root, filePath = './',fileimagesPath = './'):
        super().__init__(root)
        self.user = Userlogin.username
        if self.user == '':
            self.app_end()
        self.fileimagesPath = 'images/'
        x = root.winfo_rootx()
        y = root.winfo_rooty()
        self.fileimagesPath = fileimagesPath
        self.image_height=595
        self.image_width=200
        self.image_list = []
        self.geometry(f'595x200+{x-470}+{y-30}')
        self.title('User login')
        self.filePath = filePath
        self.protocol("WM_DELETE_WINDOW", self.app_end)
        self.group = Userlogin.obj[self.user].group
        
        lstf = list()
        if self.group == 'admin':
            lstf.append('users')    
            f_dic = {'group': lstf, 'user': [self.user]}
        else:
            f_dic = {'user': [self.user] }
        Userlogin.set_filter(f_dic)
        Userlogin.current(self.user)
        self.create_frames()
        self.create_buttons()
        self.create_entries()
        self.config_mode('Show')
        self.disp_obj()
        
        self.mainloop()        
        
    def app_end(self):
		
        self.destroy()
        
    def read_data(self):
        formlogin.read(self.filePath)
        self.formlogin = formlogin
        
    def disp_obj(self):
		
        obj = Userlogin.current()
        self.state_entries('normal')
        self.clean_form()
        self.ent_user.insert(0, obj._user)
        self.ent_group.insert(0,obj._group)
        self.ent_budget.insert(0, obj._budget)
        self.ent_c_purchased.insert(0, obj._c_purchased)
        self.ent_b_purchased.insert(0, obj._b_purchased)
        self.state_entries('readonly')
        
    
    
    def create_obj(self):
		
        strobj = self.ent_user.get() + ';' + self.ent_group.get() + ';' + Userlogin.set_password(self.ent_password.get()) + ';' + self.ent_budget.get() + ';' + self.ent_b_purchased.get() + ';' + self.ent_c_purchased.get()
        Userlogin.from_string(strobj)
        
    
    def update_obj(self):
		
        obj = Userlogin.current()
        self.state_entries('normal')
        obj._user = self.ent_user.get()
        obj._group = self.ent_group.get()
        obj._password = Userlogin.set_password(self.ent_password.get())
        obj._budget = self.ent_budget.get()
        obj._c_purchased = self.ent_c_purchased.get()
        obj._b_purchased = self.ent_b_purchased.get()
        self.state_entries('readonly')
        
    def clean_form(self):
		
        self.ent_user.delete(0, 'end')
        self.ent_group.delete(0,'end')
        self.ent_password.delete(0,'end')
        self.ent_budget.delete(0,'end')
        self.ent_c_purchased.delete(0,'end')
        self.ent_b_purchased.delete(0,'end')
        self.ent_user.focus_set()
        
    def first(self):
		
        Userlogin.first()
        self.disp_obj()
    
    def back(self):
		
        Userlogin.previous()
        self.disp_obj()
    
    def nextrec(self):
		
        Userlogin.nextrec()
        self.disp_obj()
    
    def last(self):
		
        Userlogin.last()
        self.disp_obj()
    
    def edit(self):
		
        self.mode = 'Edit'
        self.config_mode('Edit')
        self.state_entries('normal')
        self.ent_user['state'] = 'readonly'
    
    def delete(self):
		
        resp = messagebox.askyesno(title='delete record', message='Are you sure?')
        if resp:
            Userlogin.remove(Userlogin.current()._user)
            Userlogin.write(self.filePath)
            Userlogin.previous()
            self.disp_obj()
    
    def insert(self):
		
        self.mode = 'Insert'
        self.state_entries('normal')
        self.clean_form()
        self.config_mode('Edit')
    
    def save(self):
		
        if self.mode == 'Insert':
            self.create_obj()
            Userlogin.last()
        elif self.mode == 'Edit':
            self.update_obj()
            
        self.config_mode('Show')
        self.state_entries('readonly')
        self.disp_obj()
        Userlogin.write(self.filePath)
    
    def cancel(self):
		
        self.disp_obj()
        self.config_mode('Show')
        self.state_entries('readonly')
    
    def config_mode(self, mode):
        
        if mode == "Show":
            state = 'disabled'
            if self.group == 'admin':
                state = 'normal'
                
            self.btn_first['state'] = "normal"
            self.btn_back['state'] = "normal"
            self.btn_next['state'] = "normal"
            self.btn_last['state'] = "normal"
            
            self.btn_delete['state'] = state
            self.btn_insert['state'] = state
            self.btn_edit['state'] = "normal"
            self.btn_save['state'] = "disabled"
            self.btn_cancel['state'] = "disabled"
            
            self.btn_exit['state'] = "normal"

        elif mode == "Edit":
            
            self.btn_first['state'] = "disabled"
            self.btn_back['state'] = "disabled"
            self.btn_next['state'] = "disabled"
            self.btn_last['state'] = "disabled"
            
            self.btn_edit['state'] = "disabled"
            self.btn_delete['state'] = "disabled"
            self.btn_insert['state'] = "disabled"
            self.btn_save['state'] = "normal"
            self.btn_cancel['state'] = "normal"
            
            self.btn_exit['state'] = "disabled"
            
    def state_entries(self, state):
        
        if state == 'readonly':
            self.ent_user['state'] = state
            self.ent_group['state'] = state
            self.ent_password['state'] = state
            self.ent_budget['state'] = state
            self.ent_c_purchased['state'] = state
            self.ent_b_purchased['state'] = state
        else:
            if self.group == 'admin':
                self.ent_user['state'] = state
                self.ent_group['state'] = state
                self.ent_budget['state'] = state
                self.ent_c_purchased['state'] = state
                self.ent_b_purchased['state'] = state
            self.ent_password['state'] = state
        
    def create_frames(self):
        
        self.frame_buttons = Frame(self)
        self.frame_buttons.grid(row=0, column=0)
        
        self.frame_move_button = Frame(self.frame_buttons)
        self.frame_move_button.grid(row=0, column=1, padx = 10)
        
        self.frame_edit_button = Frame(self.frame_buttons)
        self.frame_edit_button.grid(row=0, column=0, padx=10)
        self.frame_class = LabelFrame(self, text = 'User')
        self.frame_class.grid(row=2, column=0, padx = 10, pady=10)
    
    def create_buttons(self):
        
        self.btn_first = Button(self.frame_move_button, text='<<', command = self.first)
        self.btn_back = Button(self.frame_move_button, text='<', command = self.back)
        self.btn_next = Button(self.frame_move_button, text='>', command = self.nextrec)
        self.btn_last = Button(self.frame_move_button, text='>>', command = self.last)
        self.btn_first.grid(row=0,column=0)
        self.btn_back.grid(row=0,column=1)
        self.btn_next.grid(row=0,column=2)
        self.btn_last.grid(row=0,column=3)
        
        self.btn_edit = Button(self.frame_edit_button, text='edit', command = self.edit)
        self.btn_delete = Button(self.frame_edit_button, text='delete', command = self.delete)
        self.btn_insert = Button(self.frame_edit_button, text='insert', command = self.insert)
        self.btn_save = Button(self.frame_edit_button, text='save', command = self.save)
        self.btn_cancel = Button(self.frame_edit_button, text='cancel', command = self.cancel)
        self.btn_edit.grid(row=0,column=0)
        self.btn_delete.grid(row=0,column=1)
        self.btn_insert.grid(row=0,column=2)
        self.btn_save.grid(row=0,column=3)
        self.btn_cancel.grid(row=0,column=4)
        
        self.btn_exit = Button(self.frame_buttons,text="Exit",command=self.app_end)
        self.btn_exit.grid(row=0,column=2,padx=10)
    
    def create_entries(self):
        
        lbl_user = Label(self.frame_class, text='User:')
        lbl_user.grid(row=0,column=0, padx=10,pady=10)
        self.ent_user = Entry(self.frame_class)
        self.ent_user.grid(row=0,column=1, padx=10,pady=10)
        
        lbl_group = Label(self.frame_class, text='Group:')
        lbl_group.grid(row=0,column=2, padx=10,pady=10)
        self.ent_group = Entry(self.frame_class)
        self.ent_group.grid(row=0,column=3, padx=10,pady=10)
        
        lbl_password = Label(self.frame_class, text='Password:')
        lbl_password.grid(row=1,column=0, padx=10,pady=10)
        self.ent_password = Entry(self.frame_class, show = '*')
        self.ent_password.grid(row=1,column=1, padx=10,pady=10)
        
        lbl_budget = Label(self.frame_class, text='Budget:')
        lbl_budget.grid(row=1,column=2, padx=10,pady=10)
        self.ent_budget = Entry(self.frame_class)
        self.ent_budget.grid(row=1,column=3, padx=10,pady=10)
        
        lbl_b_purchased = Label(self.frame_class, text='Tickets purchased:')
        lbl_b_purchased.grid(row=2,column=0, padx=10,pady=10)
        self.ent_b_purchased = Entry(self.frame_class)
        self.ent_b_purchased.grid(row=2,column=1, padx=10,pady=10)
        
        lbl_c_purchased = Label(self.frame_class, text='Consumables purchased:')
        lbl_c_purchased.grid(row=2,column=2, padx=10,pady=10)
        self.ent_c_purchased = Entry(self.frame_class)
        self.ent_c_purchased.grid(row=2,column=3, padx=10,pady=10)
        
        def Creat_newobj_from_Entry(self):
            return self.Userlogin(self.ent_user.get(),self.ent_group.get(),
                                     self.ent_password.get(), self.ent_budget.get(), self.ent_c_purchased.get(), self.ent_b_purchased.get())
    
        def upadate_my_object(self,objet):
            objet.user = self.ent_code.get()
            objet.group = self.ent_group.get()
            objet.password = Userlogin.set_password(self.ent_password.get())
            objet.budget = self.ent_budget.get()
            objet.c_purchased = self.ent_c_purchased.get()
            objet.b_purchased = self.ent_b_purchased.get()
            


            

        
if __name__ == '__main__':
    root = Tk()
    ap = Formuser(root, 'data/')
    ap.mainloop()