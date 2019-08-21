from Fila import Fila
from tkinter import *
from functools import partial
from Usuario import Usuario
from tkinter import messagebox
class TelaCadastro(object):

    def __init__(self,user,siape):
            
#====================== função que limita o que pode ser digitado nas Entry ============================================
#======================================================================================================================
#======================================================================================================================
        def limitar_TamanhoSiape_Senha(tipo,entrada):
            '''função limita a entrada que é digitada nos entrys da tela'''
            if tipo =='user':

                if len(entrada) > 7:
                    '''Siape é limitado a ter len > 7'''
                    return False
                elif len(entrada)==0:
                    return True

                elif entrada[-1] not in '1234567890':
                    '''impossibilita  entrada de algo que não seja numero'''
                    return False
            elif tipo =='pesquisaUser':
                if entrada == 'Digite Siape...':
                    return True
                elif len(entrada) > 7:
                    '''Siape é limitado a ter len > 7'''
                    return False
                elif len(entrada) == 0:
                    return True
                elif entrada[-1] not in '1234567890':
                    '''impossibilita  entrada de algo que não seja numero'''
                    return False
                return True
            elif tipo == 'senha':
                if len(entrada) > 7:
                    '''Senha é limitada a ter len > 7'''
                    return False
                elif len(entrada)==0:
                    return True
                elif entrada[-1] == ',':
                    '''impossibilita  entrada de virgula'''
                    return False
            elif tipo == 'nome':
                if len(entrada) >30:
                    '''Nome é limitado a ter len > 30'''
                    return False
                elif len(entrada) == 0:
                    return True
                elif entrada[-1] in '1234567890-+=-*@#$%¨&()}]{",[!_><:;?/|]' or entrada[-1] in "'":
                    '''Impossibilita a entrada de alguns caracteres'''
                    return False
            elif tipo == 'tell':
                if len(entrada) >11:
                    '''telefone é limitado a ter len > 11'''
                    return False
                elif len(entrada) == 0:
                    return True
                elif entrada[-1] not in '1234567890':
                    '''Somente numeros podem ser digitados'''
                    return False

            elif tipo =='email':
                if len(entrada)==0:
                    return True
                elif entrada[-1] in ' ' or  entrada[-1] in ',':
                    '''impossibilita digitar virgula'''
                    return False







            return True
#======================================================================================================================

#============================FUNÇÂO DE BUSCA DE USUÁRIOS UTILIZANDO SIAPE COMO CHAVE ==================================
#======================================================================================================================
#======================================================================================================================
        def apagar(event):
            '''apaga entrada de pequisa assim q o entry for acionado por <Button-1>'''
            self.entradapesquisavar.set('')
        def pesquisarSiape():
            '''instancia uma fila'''
            self.usuarios = Fila()
            '''chama metodo fila usuarios'''
            self.usuarios.filaUsuarios()


            self.siape = self.entradapesquisavar.get()
            temppesquisa = False
            for siapes in self.usuarios.dados:
                '''verifica o siape digitano na fila criada'''
                if siapes.verificarUsuario(self.siape):
                    '''se ele estiver cadastrado'''
                    self.btAlterar.configure(state=NORMAL)
                    self.entradausuario.configure(state=DISABLED)
                    self.checkStatus.place(x=200,y=self.y/4-58)
                    #verifica o status do usuario
                    if siapes.status == 'Ativo':
                        self.statusvar.set('Inativar Usuário')
                        self.checkStatus['fg'] = 'red'
                        self.tempstatus = 'Ativo'
                    elif siapes.status == 'Inativo':
                        self.statusvar.set('Ativar Usuário')
                        self.checkStatus['fg'] = '#006400'
                        self.tempstatus = 'Inativo'

                    temppesquisa=True
                    self.tell.set(siapes.tell)

                    '''set campos com os dados encontrados'''
                    self.nomevar.set(siapes.nome)
                    self.emailvar.set(siapes.email)
                    self.siapevar.set(siapes.login)
                    self.senhavar.set(siapes.senha)
                    self.checkStatus.deselect()
                    '''set tipo do usuario encontrado'''
                    if str(siapes.tipo) == 'prof':
                        SelecionarTipo('prof')
                    elif str(siapes.tipo) =='tec':
                        SelecionarTipo('tec')
                    self.entradapesquisavar.set('')
            if temppesquisa ==False:
                '''se nenhum usuario tiver sido encontrado'''
                messagebox.showinfo('AVISO', 'USUÁRIO NÃO ENCONTRADO')
                self.tell.set('')
               
                self.nomevar.set('')
                self.emailvar.set('')
                self.siapevar.set('')
                self.senhavar.set('')
                self.entradausuario.configure(state=NORMAL)
                
                self.btAlterar.configure(state=DISABLED)
                self.checkStatus.place(x=self.x + 1000, y=self.y + 1000)

#======================================================================================================================

#=============FUNÇÕES DE MODIFICAÇÃO DO BANCO .TXT, FUNÇOES DE ALTERAR/INATIVAR E CADASTRAR DADOS======================
#======================================================================================================================
#======================================================================================================================


#======================================================================================================================

#===========================FUNÇÂO DE VALIDAÇÃO DOS DADOS INSERIDOS PELO USUÁRIO======================================
#======================================================================================================================
#======================================================================================================================
                    
    
        def validarDadosInseridos(parametroButton):
            '''instancia uma fila'''
            self.usuarios = Fila()
            '''chama metodo filaUsuarios'''
            self.usuarios.filaUsuarios()
            login = self.entradausuario .get()
            senha = self.entradasenha.get()
            templog=','
            tempsen=','
            '''verifica se estava no modo de alteraçao'''
            if self.entradausuario['state'] == DISABLED and parametroButton =='cad':
                '''emite erro e esvazia campos'''
                self.entradausuario.configure(state=NORMAL)
                self.tell.set('')
                self.nomevar.set('')
                self.emailvar.set('')
                self.siapevar.set('')
                self.senhavar.set('')
                messagebox.showwarning('AVISO', 'USUÁRIO NÃO PODE SER CADASTRADO NOVAMENTE, VOLTANDO PARA O MODO DE CADASTRO')
                self.btAlterar.configure(state=DISABLED)
                self.statusvar.set('')
                self.checkStatus.deselect()
                self.checkStatus.place(x=self.x+1000,y = self.y+1000)
            else:
                '''se não continua verificaçao'''
                if len(self.entradausuario.get())<7 :
                    '''verifica se campo siape está correto'''
                    messagebox.showwarning('ERRO', '*CAMPO DE SIAPE DEVE POSSUIR 7 CARACTERES')
                elif len(self.entradasenha.get())<4:
                    '''verifica se campo senha está correto'''
                    messagebox.showwarning('ERRO', '*CAMPO DE SENHA COM NO MINIMO 4 CARACTERES')
                elif len(self.entradaNomeAdm.get())<5:
                    '''verifica se campo nome está correto'''
                    messagebox.showwarning('ERRO', '*INSIRA O NOME COMPLETO')
                elif len(self.entradaTelAdm.get())<11:
                    '''verifica se campo telefone está correto'''
                    messagebox.showwarning('ERRO', '*NUMERO DE TELEFONE INCOMPLETO')
                elif self.tipo == None:
                    '''verifica se um tipo foi escolhido'''
                    messagebox.showwarning('ERRO', '*ESCOLHA UM TIPO DE USUÁRIO')
                elif'@' in self.entradaEmailAdm.get()or '@' not in self.entradaEmailAdm.get():
                    '''verifica a validade do campo e-mail'''
                    if '@' not in self.entradaEmailAdm.get():

                        messagebox.showwarning('ERRO', '*E-MAIL INVALIDO')
                    else:
                        stri =self.entradaEmailAdm.get()
                        string = stri.split('@')
                        stritemp = string[1]
                        stritemp2 =string[0]
                        if '..' in stri:
                            messagebox.showwarning('ERRO', '*E-MAIL INVALIDO')
                        elif len((string)) != 2:
                            messagebox.showwarning('ERRO', '*E-MAIL INVALIDO')
                        elif len(string[0]) == 0 or len(string[1]) == 0:
                            messagebox.showwarning('ERRO', '*E-MAIL INVALIDO')
                        elif len(stritemp) == 0:
                            messagebox.showwarning('ERRO', '*E-MAIL INVALIDO')
                        elif '.' not in stritemp:
                            messagebox.showwarning('ERRO', '*E-MAIL INVALIDO')
                        elif stritemp2[-1]=='.':
                            messagebox.showwarning('ERRO', '*E-MAIL INVALIDO')
                        elif stritemp[0] == '.':
                            messagebox.showwarning('ERRO', '*E-MAIL INVALIDO')
                        elif stritemp[-1] == '.':
                            messagebox.showwarning('ERRO', '*E-MAIL INVALIDO')

                        else:
                            for usuario in self.usuarios.dados:
                                '''percorre a lista de usuarios'''
                                if usuario.verificarUsuario(login) and parametroButton == 'cad':
                                    '''se o usuario já existir emite mensagem de erro'''
                                    templog = login
                                    tempsen = senha

                                    messagebox.showwarning('ATENÇÃO', 'USUÁRIO JÁ EXISTE')
                            if  templog ==',' and tempsen == ','and parametroButton == 'alt':
                                "se nao existir e o parametro do botao for alterar"
                                messagebox.showinfo('AVISO', 'DADOS ALTERADOS COM SUCESSO')

                                '''instancia Usuario'''
                                self.alteraUser = Usuario(self.tipo, self.entradausuario.get(),self.entradasenha.get(), self.entradaNomeAdm.get(),self.entradaEmailAdm.get(), self.entradaTelAdm.get(),self.tempstatus)
                                '''Chama metodo alterarDados'''
                                self.alteraUser.alterarDados()
                                self.checkStatus.deselect()
                                self.tell.set('')
                                self.nomevar.set('')
                                self.emailvar.set('')
                                self.siapevar.set('')
                                self.senhavar.set('')
                                self.entradausuario.configure(state=NORMAL)
                                self.btAlterar.configure(state=DISABLED)
                                self.checkStatus.place(x=self.x + 1000, y=self.y + 1000)
                            elif templog ==',' and tempsen == ','and parametroButton == 'cad':
                                '''Se nao existir e o parametro for cadastrar'''
                                '''instancia Usuario'''
                                self.cadastrarUser = Usuario(self.tipo, self.entradausuario.get(),self.entradasenha.get(), self.entradaNomeAdm.get(),self.entradaEmailAdm.get(), self.entradaTelAdm.get(),'Ativo')
                                """chama metodo registrarUsuario"""
                                self.cadastrarUser.registrarUsuario()

                                messagebox.showinfo('AVISO', 'USUÁRIO CADASTRADO COM SUCESSO')
                                self.tell.set('')
                                self.nomevar.set('')
                                self.emailvar.set('')
                                self.siapevar.set('')
                                self.senhavar.set('')
#======================================================================================================================
#===================================FUNÇÂO DE SELEÇÃO DO CHECKBOX PROF OU TEC==========================================
#======================================================================================================================
#======================================================================================================================
        def SelecionarTipo(tipo):
            if tipo == 'prof':
                self.checkbuttonProf.select()
                self.checkbuttonTec.deselect()
                self.tipo = tipo
            elif tipo == 'tec':
                self.checkbuttonTec.select()
                self.checkbuttonProf.deselect()
                self.tipo = tipo
        def coletarStatus(event):
            '''Coleta Status atual do usuario Buscado'''
            if self.statusvar.get() == 'Inativar Usuário':
                if self.tempstatus == 'Inativo':
                    self.tempstatus = 'Ativo'
                else:
                    self.tempstatus = 'Inativo'

            if self.statusvar.get() == 'Ativar Usuário':
                if self.tempstatus == 'Ativo':
                    self.tempstatus = 'Inativo'
                else:
                    self.tempstatus = 'Ativo'

#======================================================================================================================

#===================================FUNÇÂO DE BACK, VOLTA PARA A TELA INICIAL==========================================
#======================================================================================================================
#======================================================================================================================
        def back():
            from Tela_Inicial import Tela_Inicial
            self.window.destroy()
            volta = Tela_Inicial(user,siape)

#======================================================================================================================

#================================INICIO DA CONTRUÇÃO GRAFICA DA TELA CADASTRO==========================================
#======================================================================================================================
#======================================================================================================================

        self.window = Tk()
        self.tipo = None
        self.tempstatus = None
        vcmd = self.window.register(func=limitar_TamanhoSiape_Senha)
        screen_width = 1024
        screen_height = 768
        self.window.title('Labifro')
        self.window.geometry('{}x{}+0+0'.format(screen_width,screen_height))


        self.frameTela = Frame(self.window)
        self.frameTela['bg'] = '#5F9EA0'
        self.frameconteiner = Frame(height = screen_height/2+150,width=screen_width/2,bg='#5F9EA0')
        self.y = self.frameconteiner['height']
        self.x= self.frameconteiner['width']
        self.frameTela.place(x=10,y=10,height = 680,width=1260)
        self.frametop = Frame(self.window, height=100, width=screen_width - 100, bg='#708090')
        self.frametop.pack()

        self.photo = PhotoImage(file='icons_images/iconecad.png')
        self.photo = self.photo.subsample(1, 1)
        self.labelimg = Label(self.frametop, image=self.photo)
        self.labelimg['bg'] = '#708090'
        self.labelimg.place(x=self.frametop['width'] / 2 - 300, y=15)
        self.labelcad = Label(self.frametop, text='Cadastro de Usuário', font=('Times', 30))
        self.labelcad['bg'] = '#708090'
        self.labelcad.place(x=screen_width / 2 - 250, y=25)
        ###########ADM##########################
        self.tell=StringVar()
        self.nomevar =StringVar()
        self.emailvar = StringVar()
        self.siapevar = StringVar()
        self.senhavar=StringVar()
        self.entradapesquisavar = StringVar()
        self.entradapesquisavar.set('Digite Siape...')
        self.statusvar = StringVar()



#################################'''NEWS'''###################################################
        self.entradapesquisa = Entry(self.frameconteiner,relief = FLAT,validate= 'key',textvariable=self.entradapesquisavar , validatecommand=(vcmd,'pesquisaUser','%P'))
        self.entradapesquisa.place(x=0,y= self.y/4-50)
        self.imgbtlupa = PhotoImage(file='icons_images/lup.png')
        self.btlupa = Button(self.frameconteiner,image = self.imgbtlupa, height=15, width=15,relief = GROOVE,command= pesquisarSiape).place(x=120,y=self.y/4-51)
        self.entradapesquisa.bind('<Button-1>',apagar)

######################################################################

        self.labelNomeAdm =Label(self.frameconteiner,text='Nome',font=('vendana',14))
        self.labelNomeAdm['bg']=self.frameTela['bg']
        self.labelNomeAdm.place(x=135,y = self.y/4 - 23)
        self.labelEmailAdm=Label(self.frameconteiner,text='E-Mail',font=('vendana',14))
        self.labelEmailAdm['bg'] = self.frameTela['bg']
        self.labelEmailAdm.place(x=135,y = self.y/4 + 20)
        self.labelTelAdm = Label(self.frameconteiner, text='Telefone',font=('vendana',14))
        self.labelTelAdm['bg'] = self.frameTela['bg']
        self.labelTelAdm.place(x=129,y=self.y/4+63)
        self.entradaNomeAdm = Entry(self.frameconteiner,width=25,font=('vendana',12),relief = FLAT,validate='key',textvariable=self.nomevar, validatecommand=(vcmd,'nome','%P'))
        self.entradaNomeAdm.place(x= 60, y = self.y / 4+2)
        self.entradaEmailAdm= Entry(self.frameconteiner, width=25, font=('vendana', 12),textvariable=self.emailvar,relief = FLAT,validate='key', validatecommand=(vcmd,'email','%P'))
        self.entradaEmailAdm.place(x=60,y=self.y/4+46)
        self.entradaTelAdm = Entry(self.frameconteiner, width=25, font=('vendana', 12),relief = FLAT,textvariable=self.tell,validate='key', validatecommand=(vcmd,'tell','%P'))
        
        self.labelusuario = Label(self.frameconteiner,text = 'SIAPE',font =('vendana',14))
        self.labelusuario.place(x=135,y=self.y/4+110)
        self.entradaTelAdm.place(x=60,y=self.y/4+88)
        self.labelusuario['bg'] =self.frameTela['bg']
        self.entradausuario = Entry(self.frameconteiner, width=25, font=('vendana', 12),textvariable=self.siapevar,relief=FLAT,validate='key', validatecommand=(vcmd,'user','%P'))
        self.entradausuario.place(x=60,y=self.y/4+136)

        self.labelSenha = Label(self.frameconteiner,text = 'Senha',font =('vendana',14))
        self.labelSenha.place(x=135,y=self.y/4+158)
        self.entradasenha = Entry(self.frameconteiner, width=25, font=('vendana', 12), relief=FLAT,show='*',textvariable=self.senhavar,validate= 'key', validatecommand=(vcmd,'senha','%P'))
        self.labelSenha['bg'] = self.frameTela['bg']
        self.entradasenha.place(x=60,y=self.y/4+182)
        ##################CHECK#########################
        self.checkbuttonProf = Checkbutton(self.frameconteiner,text= 'Professor',font=('Vendana',14),relief=FLAT,bg='#5F9EA0')
        self.checkbuttonProf.place(x=self.x/4-70,y=self.y/4+211)
        self.checkbuttonTec = Checkbutton(self.frameconteiner, text='Tecnico de Lab', font=('Vendana', 14), relief=FLAT,bg='#5F9EA0')
        self.checkbuttonProf['command']=partial(SelecionarTipo,'prof')
        self.checkbuttonTec['command']=partial(SelecionarTipo,'tec')
        self.checkbuttonTec.place(x=self.x/4+120,y=self.y/4+211)



        self.imgback =PhotoImage(file='icons_images/back.png')


        self.back = Button(self.frametop, image=self.imgback, height=30, width=30, relief=FLAT, activebackground='#00FF7F')
        self.back.place(x=10, y=50)
        self.back['command']= back

        self.frameconteiner.pack()

        self.back['bg'] = '#5F9EA0'
        self.back['relief']=FLAT
        self.back['cursor']='exchange'
        ###############################NEWS

        self.imgbtalterar = PhotoImage(file='icons_images/alt.png')
        self.btAlterar = Button(self.frameconteiner,image=self.imgbtalterar,text = 'Alterar',height=46, width=100,bg='#FF8C00',relief = GROOVE,state = DISABLED)
        self.btAlterar.place(x = 60 ,y=self.y/4+260)
        self.btAlterar['command']=partial(validarDadosInseridos,'alt')
        self.checkStatus=Checkbutton(self.frameconteiner,textvariable = self.statusvar,font=('Vendana',14),bg = '#5F9EA0')
        self.checkStatus.bind('<Button-1>',coletarStatus)
        self.imgbt = PhotoImage(file='icons_images/Save1.png')
        self.btCadastrarADM = Button(self.frameconteiner, text='Cadastrar', height=46, width=100, image=self.imgbt,activebackground='#00FF7F', relief=GROOVE)
        self.btCadastrarADM['command']=partial(validarDadosInseridos,'cad')
        self.btCadastrarADM['bg'] = '#D3D3D3'
        self.btCadastrarADM.place(x = 292,y=self.y/4+260)
       



        self.window['bg']='#5F9EA0'
        self.window.iconbitmap('icons_images/iconewindow.ico')
        self.window.mainloop()

