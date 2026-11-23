# -*- coding: utf-8 -*-
"""

"""


from tkinter import *

class OpenUser(Toplevel):
    def __init__(self, root, classObj, attnames, ncols = 2, filePath = './'):
        super().__init__(root)
        self.root = root
        self.classObj = classObj
        
        
        obj = classObj.first()
        self.att = list(obj.__dict__.keys())
        self.filePath = filePath
        self.attnames =attnames
        
        self.title('Eventos')
        
       
                
          
        self.frame_buttons = Frame(self)
        self.frame_buttons.grid(row=0,column=0)
        
        
        self.frame_move_button = Frame(self.frame_buttons)
        self.frame_move_button.grid(row=0,column=1, padx=10)
         
        self.button_first = Button(self.frame_move_button,text="<<",  command= lambda: self.showObject('F'))
        self.button_back = Button(self.frame_move_button,text="<",  command= lambda: self.showObject('P'))
        self.button_next = Button(self.frame_move_button,text=">",command= lambda: self.showObject('N'))
        self.button_last = Button(self.frame_move_button,text=">>",command= lambda: self.showObject('L'))
       
        self.button_first.grid(row=0,column=0)
        self.button_back.grid(row=0,column=1)
        self.button_next.grid(row=0,column=3)
        self.button_last.grid(row=0,column=4)
        
        
        self.button_exit = Button(self.frame_buttons,text="Exit",command=self.destroy)
        self.button_exit.grid(row=0,column=5,padx=10)
        
        
        self.frame_edit_button = Frame(self.frame_buttons)
        self.frame_edit_button.grid(row=0,column=0, padx=10)
         
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
        
        
        self.frame_class = LabelFrame(self,text = self.classObj.__name__)
        self.frame_class.grid(row=2,column=0,padx=10,pady=10)
        
        
        self.ent = list()
        r = 0
        c = 0
        for desc in attnames:
            lbl = Label(self.frame_class, text=desc)
            lbl.grid(row=r, column=c, padx=10, pady=10)
            c = c + 1
            ent = Entry(self.frame_class)
            ent.grid(row=r, column=c, padx=10, pady=10)
            self.ent.append(ent)
            if c == 2 * ncols - 1:
                r = r + 1
                c = 0
            else:
                c = c + 1

        
        
        
        self.classObj.read(self.filePath)
        
        self.config_mode("Show")
        self.showObject("C")
        
        self.mainloop()

    
    def Creat_newobj_from_Entry(self):
        str_obj = ''
        sep = ''
        for ent in self.ent:
            str_obj = str_obj + sep + ent.get()
            sep = ';'
        return self.classObj.from_string(str_obj)

        
    
    
    def update_my_object(self, objet):
        for idx, ent in enumerate(self.ent):
            setattr(objet, self.att[idx], ent.get())

        
    
    def cleanForm(self):
        # clean all entrys
        for ent in self.ent:
            ent.config(state='normal')
            ent.delete(0, 'end')

        
    
    def button_edit_click(self):
        self.config_mode("Edit")
    
    def button_delete_click(self):
        selobj = 'C'
        resp = messagebox.askyesno(title='delete record', message='Are you sure?')
        if resp:
            self.classObj.remove(self.visible_object.code)
            self.classObj.write(self.filePath)
            selobj = 'P'
        self.config_mode("Show")
        self.showObject(selobj)
    
    def button_insert_click(self):
        self.visible_object = None
        self.config_mode("Edit")
        self.cleanForm()
        
    def button_save_click(self):
        if self.visible_object == None:
            
            self.visible_object = self.Creat_newobj_from_Entry()
            self.visible_object=self.classObj.last() 
        else:
            
            self.update_my_object(self.visible_object)
        
        self.classObj.write(self.filePath)
        self.visible_object=self.classObj.current() 
        self.config_mode("Show")
     
    def button_cancel__click(self):
        self.visible_object=self.classObj.current() 
        self.config_mode("Show")
        self.showObject("C")

    
    def config_mode(self, mode):
        
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
            self.en
            
            self.button_exit['state'] = "normal"
            for ent in self.ent:
                ent.config(state='readonly')

            
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
            
            self.button_exit['state'] = "disabled"
            for ent in self.ent:
                ent.config(state='normal')
            
        

    
    
    def objectToEntrys(self):
        for idx, ent in enumerate(self.ent):
            ent.config(state='normal')
            ent.delete(0, 'end')
            ent.insert(0, getattr(self.visible_object, self.att[idx]))
            ent.config(state='readonly')

        
        
    def showObject(self, option):
        # C - current
        # F - first
        # P - previous
        # N - next
       
        option = option.upper()
       
        if option == 'C':
            self.visible_object=self.classObj.current()
            
        elif  option == 'F':
            self.visible_object=self.classObj.first()
            
        elif  option == 'P':
            self.visible_object=self.classObj.previous()
            if self.visible_object == None:
                self.visible_object=self.classObj.first()
                
        elif  option == 'N':
            self.visible_object=self.classObj.nextrec()
            if self.visible_object == None:
                self.visible_object=self.classObj.last()
                
        elif  option == 'L':
            self.visible_object=self.classObj.last()

        self.objectToEntrys()    
 

