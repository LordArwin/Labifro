from tkinter import *
from tkinter import ttk, messagebox
from Laboratorio import Laboratorio
from Fila import Fila
class TelaCadastro_Lab(object):
    def __init__(self,user,siape):
        self.telacadLab = Tk()
        screen_width = 1024
        screen_height = 768
        self.telacadLab.title('Labifro')
        self.telacadLab.geometry('{}x{}+0+0'.format(screen_width,screen_height))
        self.telacadLab.iconbitmap('icons_images/iconewindow.ico')
        self.telacadLab['bg']='#5F9EA0'

        def limitar_Tamanho(tipo,entrada):
            '''funçao que limita oq pode ser digitado nas entradas'''
            if tipo == 'chave':
                if len(entrada) > 3:
                    return False
                elif len(entrada)==0:
                    return True
                elif entrada[-1] not in '1234567890':
                    return False
            elif tipo =='nome':
                if len(entrada) > 30:
                    return False
                elif len(entrada)==0:
                    return True
                elif entrada[-1] in ',':
                    return False

            return True
        def validarLab():
            '''função que valida laboratorio para saber se ja existe'''
            existe = False
            '''instancia Fila e chama metodo filaLaboratorios'''
            self.labs = Fila()
            self.labs.filaLaboratorios()

            if len(self.n_sala.get()) < 1 or len(self.chave.get()) < 2:
                '''se dados incorretos'''
                messagebox.showwarning('ATENÇÃO','DADOS INCORRETOS, VERIFIQUE SE AS INFORMAÇÕES FORAM PREENCHIDAS CORRETAMENTE')
            else:
                '''se dados corretos'''
                for lab in self.labs.dados:
                    '''chama metodos validarCad'''
                    if lab.validarCad(self.chave.get(),self.tipo_lab.get()):
                        existe = True

                        messagebox.showwarning('ATENÇÃO', 'LABORATÓRIO JÁ EXISTE')
                if existe == False:
                    '''se nao exite'''
                    '''instancia Laboratorio'''
                    cad = Laboratorio(self.tipo_lab.get(),self.n_sala.get(),self.chave.get())
                    '''chama funçao registrarLab'''
                    cad.registrarLab()
                    messagebox.showinfo('AVISO', 'LABORATÓRIO CADASTRADO COM SUCESSO')
                    self.n_salavar.set('')
                    self.n_chavevar.set('')
                    self.tipo_lab.set('')


        def back():
            '''Funçao para voltar a tela inicial'''
            from Tela_Inicial import Tela_Inicial
            self.telacadLab.destroy()
            volta = Tela_Inicial(user,siape)


        self.imgback = PhotoImage(file='icons_images/back.png')

        self.frametop = Frame(self.telacadLab, height=100, width=screen_width - 100, bg='#708090')
        self.frametop.pack()
        self.back = Button(self.frametop, image=self.imgback, height=30, width=30, relief=FLAT,
                           activebackground='#00FF7F')
        self.back.place(x=10, y=50)
        self.back['command'] = back
        self.n_salavar=StringVar()
        self.n_chavevar=StringVar()

        comando = self.telacadLab.register(func=limitar_Tamanho)
        self.photo = PhotoImage(file='icons_images/iconecad.png')
        self.photo = self.photo.subsample(1, 1)
        self.labelimg = Label(self.frametop, image=self.photo)
        self.labelimg['bg'] = '#708090'
        self.labelimg.place(x=self.frametop['width'] / 2 - 300, y=15)
        self.labelcad= Label(self.frametop, text='Cadastro de Laboratório', font=('Times', 30))
        self.labelcad['bg'] = '#708090'
        self.labelcad.place(x=screen_width / 2 - 250, y=25)
        self.framemid= Frame(self.telacadLab,width=screen_width/2,height = screen_height/2+500,bg='#5F9EA0')
        self.framemid.pack()
        self.lab = StringVar()
        self.tipo_lab = ttk.Combobox(self.framemid,state="readonly",textvariable = self.lab)
        self.tipo_lab['values'] = ('Informática', 'Química','Física','Edificações','Biologia','Eletrotécnica')
        self.tipo_lab.current(0)
        self.tipo_lablabel = Label(self.framemid,text = 'Tipo de Laboratório:')
        self.tipo_lablabel['bg']='#5F9EA0'
        self.tipo_lablabel.place(x=0,y=self.framemid['height']/8)
        self.tipo_lab.place(x=120, y=self.framemid['height']/8)
        self.n_sala = Entry(self.framemid,relief=FLAT,width = 30,textvariable=self.n_salavar,validate= 'key', validatecommand=(comando,'nome','%P'))
        self.n_sala.place(x=80, y=self.framemid['height']/8+35)
        self.n_salalabel = Label(self.framemid,text='Nome da Sala:')
        self.n_salalabel.place(x=0,y=self.framemid['height']/8+35)
        self.n_salalabel['bg']='#5F9EA0'
        self.chave = Entry(self.framemid,relief=FLAT,textvariable=self.n_chavevar,validate= 'key', validatecommand=(comando,'chave','%P'))
        self.chave.place(x=50, y=self.framemid['height']/8+70)
        self.chavelabel = Label(self.framemid,text = 'Chave:')
        self.chavelabel['bg']='#5F9EA0'
        self.chavelabel.place(x=0,y=self.framemid['height']/8+70)
        self.imgbt = PhotoImage(file = 'icons_images/Save1.png')
        self.btCadastrar = Button(self.framemid, text = 'Cadastrar',height = 40,width =50,image = self.imgbt,activebackground= '#00FF7F',relief = GROOVE)
        self.btCadastrar['bg']= '#D3D3D3'
        self.back['bg'] = '#5F9EA0'
        self.back['relief']=FLAT
        self.back['cursor'] = 'exchange'

        self. btCadastrar.place(x = 205,y=self.framemid['height']/8+120)
        self.btCadastrar['command']=validarLab

        self.telacadLab.mainloop()
