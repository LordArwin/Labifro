from tkinter import *

from Tela_Inicial import Tela_Inicial
from tkinter import messagebox
from TelaControleChave import TelaControleChave
from Fila import Fila
class TelaLogin(object):
    def __init__(self):
        '''Classe da tela login tela responsavel pelo login do usuario recebendo as entradas para validar se usuario existe'''
        self.janela = Tk()
        self.janela.title('Labifro')
        screen_width = self.janela.winfo_screenwidth()
        screen_height = self.janela.winfo_screenheight()
        self.janela.iconbitmap('icons_images/iconewindow.ico')
        self.janela.geometry('297x265+{}+{}'.format(int(screen_width/3+70),int(screen_height/4)))
        self.janela['bg'] = '#708090'
        self.framejanela = Frame(self.janela,height=250 , width = 275)
        self.framejanela.place(x=10,y=5)
        self.framejanela['bg']='#5F9EA0'

    ################FUNÇÃO QUE LIMITA O ENTRY LOGIN########################
        def entryLogin(entrada):
            if len (entrada) > 7:
                return False
            elif len(entrada)==0:
                return True
            elif entrada [-1]not in'1234567890':
                return False
            return True

        comando = self.janela.register(func=entryLogin)




        def validarLogin():
            '''funçao que valida usuario'''
            '''instancia Fila'''
            self.usuarios = Fila()
            '''chama metodo filaUsuarios'''
            self.usuarios.filaUsuarios()

            login = self.entradaLogin.get()
            senha = self.entradaSenha.get()
            templogin = ','
            tempsenha=','

            for usuario in self.usuarios.dados:
                if usuario.validarLogon(login, senha):
                    '''chama metodo validar login'''
                    templogin = usuario.login
                    tempsenha = usuario.senha
                    tempnome = usuario.nome
                    if usuario.tipo == 'tec':
                        '''se for tipo tecnico de lab'''

                        self.janela.destroy()
                        Tela_Inicial(tempnome,templogin)
                    if usuario.tipo =='prof':
                        '''se for professor'''
                        self.janela.destroy()
                        TelaControleChave(tempnome, templogin,0)
            if templogin==',' and tempsenha ==',':
                '''caso não for validado o usuario'''
                messagebox.showwarning('ATENÇÃO','USUÁRIO OU SENHA INVALIDOS')

        self.janela.resizable(False, False)
        self.labelLogin = Label(self.janela, text='Login')
        self.labelLogin['bg'] = '#5F9EA0'
        self.labelLogin.place(x=30, y=90)
        self.labelSenha = Label(self.janela, text='Senha')
        self.labelSenha.place(x=30, y=140)
        self.labelSenha['bg'] = '#5F9EA0'
        self.entradaLogin = Entry(self.janela, width=25,relief = FLAT,validate='key',validatecommand=(comando,'%P'))
        self.entradaLogin.focus()
        self.entradaLogin.place(x=80, y=90)
        self.entradaLogin.bind("<KeyPress>", lambda e: self.entradaSenha.focus() if e.char == '\r' else None)
        self.entradaSenha = Entry(self.janela, show='*', width=25,relief = FLAT)
        self.entradaSenha.focus()      
        self.entradaSenha.place(x=80, y=140)
        self.entradaSenha.bind("<KeyPress>", lambda e: validarLogin() if e.char == '\r' else None)
        photo = PhotoImage(file='icons_images/iconelogin.png')
        photo=photo.subsample(1,1)
        self.labelPNG = Label(self.janela, image=photo)
        self.labelPNG['bg']='#5F9EA0'
        self.labelPNG.place(x=120,y=15)


        self.bt = PhotoImage(file = 'icons_images/entrar.png')
        self.botaoEntrar = Button(self.janela,image= self.bt,text='ENTRAR',width=70,height = 30,command=validarLogin,activebackground= '#20B2AA',bg='#006400',relief = GROOVE)
        self.botaoEntrar.place(x=125,y=190)
        self.botaoEntrar.bind("<KeyPress>", lambda e: validarLogin if e.char == '\r' else None)
        self.janela.mainloop()





