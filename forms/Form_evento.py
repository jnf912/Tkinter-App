# -*- coding: utf-8 -*-
"""

"""
import datetime
from datetime import timedelta

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo






from  classes.class_evento import Class_evento as classMainObj

class Form_evento(Toplevel):
    def __init__(self,myroot,selectedDiaHora,  filePath = './', f_dic = {}):
        super().__init__(myroot)
        
        self.myroot = myroot
        self.f_dic = f_dic
        
        self.selectedDiaHora = selectedDiaHora
        self.filePath = filePath
        
        self.read_data()
        
        self.config_windows() 
        self.Create_frames()
        self.Create_Navigation_buttons()
        
        
        
        self.config_evento()
        self.Create_Treeview()

         
        self.statusText=''
        
 
        
        self.fillTree()
        self.my_tree.focus(0)
        self.my_tree.selection_set(0)
        
        
        
        
        
        self.mainloop()
        
    def read_data(self):
        classMainObj.read(self.filePath)
        self.classMainObj = classMainObj
        
        if len(self.f_dic) == 0:
            self.classMainObj.set_filter
        else:
            self.classMainObj.set_filter(self.f_dic)
            
        
        
    def config_evento(self):
        
        self.HoraIni = 8
        self.HoraFim = 21
        
        
        dia = self.str2datetime(self.selectedDiaHora.get()).date()
        self.dia = dia
        
    
        
        self.diaInicial = dia+timedelta(days=-int(dia.strftime("%w")))
        self.diaFinal = self.diaInicial+timedelta(days=+6)
        
        self.colunas=('d','2','3','4','5','6','s')
        
        
 
    def config_windows(self):
        
        self.title('Calendar')
        
        
    def closewindows(self):
        self.destroy()
        
    def Create_frames(self):
          
        self.frame_main = Frame(self)
        self.frame_main.grid(row=0,column=0)
    
          
        self.frame_buttons = Frame(self.frame_main)
        self.frame_buttons.grid(row=0,column=0)
        
         
        self.frame_move_button = Frame(self.frame_buttons)
        self.frame_move_button.grid(row=0,column=1, padx=10)
        
        
        self.frame_edit_button = Frame(self.frame_buttons)
        self.frame_edit_button.grid(row=0,column=0, padx=10)
        
         
        self.frame_class = LabelFrame(self,text ='class event')
        self.frame_class.grid(row=2,column=0,padx=10,pady=10)
        
        
        self.frame_Treeview = LabelFrame(self,text ='Calendar')
        self.frame_Treeview.grid(row=4,column=0,padx=10,pady=10)
        
        self.Create_status(self)
        
    
    def Create_status(self,frame):
        
        
        
        self.frame_status = Label(frame,bd=1,relief=SUNKEN)
        self.frame_status.grid(row=22,column=0,sticky=W+E)
        
        self.lb_status = Label(self.frame_status,text= "Status" , bd=1,relief=SUNKEN)
        self.lb_status.grid(row=0, column=0,  pady=10, sticky=W+E)
        
        
    
    def Create_Navigation_buttons(self):
          
        self.button_back = Button(self.frame_move_button,text="<",  command= lambda: self.ShowWeek('P'))
        self.button_next = Button(self.frame_move_button,text=">",command= lambda: self.ShowWeek('N'))
         
        self.button_back.grid(row=0,column=1)
        self.button_next.grid(row=0,column=3)
        
        self.button_exit = Button(self.frame_buttons,text="Exit",command=self.closewindows)
        self.button_exit.grid(row=0,column=5,padx=10)
        
  
    
    
    def Create_Columns(self,tree):
       
        tree['columns'] = self.colunas
        tree.column('#0',width = 100 , stretch = NO)
        tree.heading('#0')
        for i in range(len(self.colunas)):
            tree.column(self.colunas[i],width = 100,anchor='center')
            dias = self.diaInicial+timedelta(days=i)
            tree.heading(self.colunas[i],anchor=CENTER,text = str(dias) )
        
        
        
       
    
    def Create_Treeview(self):
        
        mystyle = ttk.Style()
        mystyle.theme_use("clam")
        
        mystyle.configure("Treeview", 
                        #background='red',
                        #foreground = 'black',
                        rowheight = 25)
        
        

        
        mystyle.map("Treeview",  background=[('selected','green')])
        
        
        
        scrollbar_V = Scrollbar(self.frame_Treeview)
        scrollbar_V.pack(side = RIGHT , fill = Y)
        
        
        scrollbar_H = Scrollbar(self.frame_Treeview,orient = 'horizontal')
        scrollbar_H.pack(side = BOTTOM , fill = X)    
        
        self.my_tree = ttk.Treeview(self.frame_Treeview , 
                                    yscrollcommand = scrollbar_V.set,
                                    xscrollcommand = scrollbar_H.set, 
                                    selectmode = "browse",
                                    style="mystyle.Treeview")
        self.my_tree.pack()
        
        
        scrollbar_V.config(command= self.my_tree.yview)
        scrollbar_H.config(command= self.my_tree.xview)
        
        self.Create_Columns(self.my_tree)
        
       
        
        self.my_tree.bind("<Double-1>", self.select_line)
 
        
    def select_line(self,event):
         
        selected_row_number = self.my_tree.focus()
        l=int(selected_row_number)
        
        col = self.my_tree.identify_column(event.x)
        col = col.split('#')
        c = int(col[len(col)-1])-1

        self.selectedDiaHora.set( str(self.diaInicial+timedelta(days=c))  + " " + str(self.HoraIni + int(selected_row_number )) + ":00")
        
  
        
    def str2datetime(self,datestr):
        
        datestr = datestr.replace("/", ";")
        datestr = datestr.replace("-", ";")
        datestr = datestr.replace(":", ";")
        datestr = datestr.replace(" ", ";")
        
        
        try:
            
            diahorastr =list(map(int, datestr.split(";")))
            
             
            date = datetime.datetime(diahorastr[0], diahorastr[1], diahorastr[2])
            if len(diahorastr)>3:
                date=date.replace(hour = diahorastr[3])
            if len(diahorastr)>4:
                date=date.replace(minute=  diahorastr[4])
            if len(diahorastr)>5:
                date=date.replace(second = diahorastr[5])
        except:
            date = datetime.datetime.now()
            
        return date
    

    
    
    def fillTree(self):
        
        for record in self.my_tree.get_children():
            self.my_tree.delete(record)
        
        self.semanaObj = [[None] * 7 for i in range(24)]
        self.semanaTree = [[''] * 7 for i in range(24)]
       
        for k in classMainObj.lst:
            evento = classMainObj.obj[k]
            if evento.diahora.date() >= self.diaInicial and evento.diahora.date() <= self.diaFinal:
                #print(evento)
                c=int(evento.diahora.strftime("%w"))
                l=int(evento.diahora.strftime("%H"))
                self.semanaTree[l][c] = self.text_to_evento(evento) 
                self.semanaObj[l][c] = classMainObj.obj[k]
      
       
                
        line = 0
        
        for k in range(self.HoraIni,self.HoraFim+1):
            valores = self.semanaTree[k]
            
            self.my_tree.insert(parent='', index ='end',iid=line ,text=str(k) + ' H', values = valores )
            
            line +=1
         
        
        for i in range(len(self.colunas)):
            
            dias = self.diaInicial+timedelta(days=i)
            self.my_tree.heading(self.colunas[i],anchor=CENTER,text = str(dias) )
          
        
        
    def text_to_evento(self,evento):
        texto = f'{evento.code}-{evento.tipo}'
        return texto
    
        
    
    def cleanForm(self):
        
        children_widgets = self.frame_class.winfo_children()
        for child_widget in children_widgets:
            if child_widget.winfo_class() == 'Entry':
                child_widget.delete(0,END)
                
  
    
          
    def ShowWeek(self,option):
       
        # P - previous
        # N - next
        
        
        option = option.upper()
       
       
        if  option == 'P':
            self.diaInicial = self.diaInicial+timedelta(days=-7)
            self.diaFinal = self.diaInicial+timedelta(days=+6)
                
        elif  option == 'N':
           self.diaInicial = self.diaInicial+timedelta(days=+7)
           self.diaFinal = self.diaInicial+timedelta(days=+6)
                
        self.fillTree()