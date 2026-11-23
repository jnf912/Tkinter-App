# -*- coding: utf-8 -*-

"""

"""

from tkinter import *
from tkinter import ttk


from classes.eventos import Eventos as classMainObj



class Customer_type_form_Table(Toplevel):
    def __init__(self,myroot, filePath = './', editmode = 0):
        super().__init__(myroot)
        self.myroot = myroot
        self.filePath = filePath
        self.editmode = editmode
        self.statusText=''
        self.Conf_windows_title() 
        self.read_data()
        self.Create_frames()
        self.Create_Navigation_buttons()
        self.Create_Edit_buttons()
        self.Create_Treeview()
        self.Create_entys()
        self.config_mode("Show")
        self.fillTree()
        self.my_tree.focus(0)
        self.my_tree.selection_set(0)
        
        self.mainloop()
        
        
    def Conf_windows_title(self):
        
        self.title('Type Events')
        
    
    def read_data(self):
        classMainObj.read(self.filePath)
        self.classMainObj = classMainObj
        
        
        
    def Create_frames(self):
           
        self.frame_main = Frame(self)
        self.frame_main.grid(row=0,column=0)
    
           
        self.frame_buttons = Frame(self.frame_main)
        self.frame_buttons.grid(row=0,column=0)
        
        
        self.frame_move_button = Frame(self.frame_buttons)
        self.frame_move_button.grid(row=0,column=1, padx=10)
        
        
        self.frame_edit_button = Frame(self.frame_buttons)
        self.frame_edit_button.grid(row=0,column=0, padx=10)
        
        
        self.frame_class = LabelFrame(self,text ='class data')
        self.frame_class.grid(row=2,column=0,padx=10,pady=10)
        
        
        self.frame_Treeview = LabelFrame(self,text ='Data Table')
        self.frame_Treeview.grid(row=4,column=0,padx=10,pady=10)
        
        self.Create_status(self)
        
    
    def Create_status(self,frame):

        
        self.frame_status = Label(frame,bd=1,relief=SUNKEN)
        self.frame_status.grid(row=22,column=0,sticky=W+E)
        
        self.lb_status = Label(self.frame_status,text= "Status" , bd=1,relief=SUNKEN)
        self.lb_status.grid(row=0, column=0,  pady=10, sticky=W+E)
        
        
    
    def Create_Navigation_buttons(self):
          
        self.button_first = Button(self.frame_move_button,text="<<",  command= lambda: self.SelectTreeLine('F'))
        self.button_back = Button(self.frame_move_button,text="<",  command= lambda: self.SelectTreeLine('P'))
        self.button_next = Button(self.frame_move_button,text=">",command= lambda: self.SelectTreeLine('N'))
        self.button_last = Button(self.frame_move_button,text=">>",command= lambda: self.SelectTreeLine('L'))
        
        self.button_first.grid(row=0,column=0)
        self.button_back.grid(row=0,column=1)
        self.button_next.grid(row=0,column=3)
        self.button_last.grid(row=0,column=4)
        
        
        
        self.button_exit = Button(self.frame_buttons,text="Exit",command=self.destroy)
        self.button_exit.grid(row=0,column=5,padx=10)
        
    def Create_Edit_buttons(self):
        
          
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
      
    
    
    def Create_Columns(self,tree):
        # Fields to Treeview
        tree['columns'] = ('code','capacidade','patrocionador')
        tree.column('#0',width = 0 , stretch = NO)
        tree.column("code")
        tree.column("capacidade")
        tree.column("patrocionador")
        
        
        tree.heading('#0')
        tree.heading("code",text = 'Event Type')
        tree.heading("capacidade", text = 'Capacity')
        tree.heading("patrocionador", text= 'Sponsor')
        
    
    def Create_Treeview(self):
        
        scrollbar_V = Scrollbar(self.frame_Treeview)
        scrollbar_V.pack(side = RIGHT , fill = Y)
        
        
        scrollbar_H = Scrollbar(self.frame_Treeview,orient = 'horizontal')
        scrollbar_H.pack(side = BOTTOM , fill = X)    
        
        self.my_tree = ttk.Treeview(self.frame_Treeview ,yscrollcommand = scrollbar_V.set,xscrollcommand = scrollbar_H.set, selectmode = "browse")
        self.my_tree.pack()
        
        
        scrollbar_V.config(command= self.my_tree.yview)
        scrollbar_H.config(command= self.my_tree.xview)
        
        self.Create_Columns(self.my_tree)
        
       
        
        self.my_tree.bind("<Double-1>", self.select_line)
    
  
        
        
    def select_line(event):
        print("select line")
        self.button_edit_click()
    
    
    
    def fillTree(self):
        
        for record in self.my_tree.get_children():
            self.my_tree.delete(record)
       
    
        line = 0
        for k in range(len(self.classMainObj.lst)):
            code = self.classMainObj.lst[k]
            obj = self.classMainObj.obj[code]
            self.my_tree.insert(parent='', index ='end',iid=line ,text='', values = (obj.code, obj.capacidade, obj.patrocionador) )
            line +=1
            
    def Create_entys(self):
        
        
        
        self.lb_code = Label(self.frame_class,text = 'Code :')
        self.en_code = Entry(self.frame_class)
        
        self.lb_capacidade = Label(self.frame_class,text = 'Capacidade :')
        self.en_capacidade = Entry(self.frame_class)
        
        self.lb_patrocionador = Label(self.frame_class,text = 'Patrocionador :')
        self.en_patrocionador = Entry(self.frame_class)
        
        
        
        
        self.lb_code.grid(row=0, column=0, padx=10, pady=10)
        self.en_code.grid(row=0, column=1, padx=10, pady=10)
     
        self.lb_capacidade.grid(row=0, column=2, padx=10, pady=10)
        self.en_capacidade.grid(row=0, column=3, padx=10, pady=10)
        
        self.lb_patrocionador.grid(row=0, column=4, padx=10, pady=10)
        self.en_patrocionador.grid(row=0, column=5, padx=10, pady=10)
        
        
    
    
    
    
    def Creat_newobj_from_Entry(self):
        return self.classMainObj(self.en_code.get(),self.en_capacidade.get(),self.en_patrocionador.get())
    
    
    
    def upadate_my_object(self,objet):
        objet.code = self.en_code.get()
        objet.capacidade = self.en_capacidade.get()
        objet.patrocionador = self.en_patrocionador.get()
        
        
        
        
        
    
    def cleanForm(self):
        
        children_widgets = self.frame_class.winfo_children()
        for child_widget in children_widgets:
            if child_widget.winfo_class() == 'Entry':
                child_widget.delete(0,END)
                
            
        
    
    def button_edit_click(self):
        self.config_mode("Edit")
        self.selected_to_entrys()
    
    def button_delete_click(self):
        selected_row_number = my_tree.focus()
        values = my_tree.item(selected_row_number, 'values')
        self.visible_object = self.classMainObj.obj[values[0]]
        self.classMainObj.remove(self.visible_object.code)
        self.config_mode("Show")
        self.fillTree()
    
    def button_insert_click(self):
        
        self.visible_object = None
        self.config_mode("Edit")
       
        
    def button_save_click(self):
        
        if self.visible_object == None:
            
            self.visible_object = self.Creat_newobj_from_Entry()
            self.visible_object=self.classMainObj.last() 
        else:
            
            self.upadate_my_object(self.visible_object)
            
        
        self.classMainObj.write(self.filePath)
        
        self.fillTree() 
       
        self.config_mode("Show")
        self.cleanForm()
     
        
    def button_cancel__click(self):
       
        self.visible_object=self.classMainObj.current() 
        self.config_mode("Show")
        
        self.cleanForm()
        
    def hideEntryFields(self):
        self.frame_class.grid_remove()
    def showEntryFields(self):
        self.frame_class.grid()

    
    def config_mode(self,mode):
        
        if mode == "Show":
            self.button_first['state'] = "normal"
            self.button_back['state'] = "normal"
            self.button_next['state'] = "normal"
            self.button_last['state'] = "normal"
            
            if self.editmode == 1:
                self.btn_mode("normal")
            else:
                self.btn_mode("disabled")
            
            self.button_save['state'] = "disabled"
            self.button_cancel['state'] = "disabled"
            
            self.button_exit['state'] = "normal"
            
            self.hideEntryFields()
            
        elif mode == "Edit":
            self.button_first['state'] = "disabled"
            self.button_back['state'] = "disabled"
            self.button_next['state'] = "disabled"
            self.button_last['state'] = "disabled"
            
            
            self.btn_mode("disabled")
            self.button_save['state'] = "normal"
            self.button_cancel['state'] = "normal"
            
            self.button_exit['state'] = "disabled"           
           
            self.showEntryFields()
            
    def btn_mode(self, state):
        self.button_edit['state'] = state
        self.button_delete['state'] = state
        self.button_insert['state'] = state
    
    
    def objectToEntrys(self):
        self.en_code.delete(0,END)
        self.en_code.insert(0, self.visible_object.code)
        
        self.en_capacidade.delete(0,END)
        self.en_capacidade.insert(0, self.visible_object.capacidade)
        
        self.en_patrocionador.delete(0,END)
        self.en_patrocionador.insert(0, self.visible_object.patrocionador)
        
    def selected_to_entrys(self):
        
        selected_row_number = self.my_tree.focus()
        values = self.my_tree.item(selected_row_number, 'values')
        self.visible_object = classMainObj.obj[values[0]]
        
        
        self.objectToEntrys()    
        
    def SelectTreeLine(self,option):
        # C - current
        # F - first
        # P - previous
        # N - next
        
        
        option = option.upper()
       
       
        if  option == 'F':
            self.my_tree.selection_set(0)
            
        elif  option == 'P':
            nextP = int(self.my_tree.focus())-1
            
            if nextP < 0:
                nextP = 0
            self.my_tree.focus(nextP)
            self.my_tree.selection_set(nextP)
                
        elif  option == 'N':
            nextP = int(self.my_tree.focus())+1
            rows_count = len(self.my_tree.get_children()) -1
            if nextP > rows_count :
                nextP = rows_count 
            self.my_tree.focus(nextP)
            self.my_tree.selection_set(nextP)
                
        elif  option == 'L':
            rows_count = len(self.my_tree.get_children()) -1
            
            self.my_tree.focus(rows_count)
            self.my_tree.selection_set(rows_count)
            
    

   

def teste():
    

    f = Type_customer_form_Table()
     
   



if __name__ == "__main__":
    teste()