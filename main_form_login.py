# -*- coding: utf-8 -*-
"""

"""

from forms.formuser import Formuser
from forms.formlogin import FormLogin
from forms.openform import OpenForm
from classes.userlogin import Userlogin
# importar a class App
from evento_teste import App
from evento_teste_user import UserForm
from tkinter import *

root = Tk()
root.title('User login')
root.withdraw()

loginf = FormLogin(root,filePath='data/')
root.mainloop()

#alterado para permitir entrar em diferentes forms consoante o tipo de user
user = Userlogin.username

if user != '':
    if Userlogin.obj[user].group == 'admin':
        #caso seja do tipo admin abre o form que estava por omissão neste
        #exemplo
        print('Logged in user:',Userlogin.username)
        #começar app aqui
        ap = App()    
    else:
        ap = UserForm()
   
    # loop até ser fechada pelo utilizador
    ap.mainloop()
else:
    print("Not logged in")
