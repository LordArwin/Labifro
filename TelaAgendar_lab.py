from tkinter import *
from tkinter import ttk, messagebox
from Usuario import Usuario
from datetime import date
from Laboratorio import Laboratorio
from Agendamento import Agendamento
from Fila import Fila
class TelaAgendar_lab(object):
    def __init__(self,user,siape):
        '''Classe de Fronteira para interação do usuario ao cadastrar Agendamento'''
# ==========================================================================================================================================================
# ===================== FUNÇÃO QUE LIMITA OQ PODE SER DIGITADO NA ENTRY ======================================================================================
# =======================================================================================================================================================
        def limitarEntry(entrada):
            if entrada=='Digite Siape...':
                return True
            elif len(entrada) > 7:
                return False
            elif len(entrada) == 0:
                return True
            elif entrada[-1] not in '1234567890':
                return False
            return True
# =================================================== FUNÇÃO BACK PARA VOLTAR A TELA INICIAL ===============================================================
# ==========================================================================================================================================================

        def back():
            from Tela_Inicial import Tela_Inicial
            self.janAgendar.destroy()
            volta = Tela_Inicial(user,siape)

# ==========================================================================================================================================================
        def pesquisa_siape():
                '''Funçao de pesquisa do siape'''
                self.usuarios = Fila()
                '''instancia Fila e chama metodo filaUsuarios'''
                self.usuarios.filaUsuarios()
                self.siape = self.entradapesquisa.get()
                temppesquisa = False
                for siapes in self.usuarios.dados:
                    '''Chama metodo verificarUsuario'''
                    if siapes.verificarUsuario(self.siape):
                        if siapes.status == 'Ativo':
                            '''caso usuario existir e for ativo pesquisa é concluida'''
                            self.entradavar.set(siapes.nome+','+siapes.login)
                            temppesquisa=True
                            self.pesquisavar.set('')
                if temppesquisa ==False:
                    '''caso erro na veriicação do usuario, emite mensagem de erro'''
                    messagebox.showinfo('AVISO', 'USUÁRIO NÃO ENCONTRADO')
                    self.entradavar.set('')


# ================================================ FUNÇÃO DE PREENCHIMENTO DOS COMBOBOX ====================================================================
# ==========================================================================================================================================================

        def autoPreenchimento(event):
            self.labsala.set('')
            self.labturno.set('')
            self.tempoAulacombo.set('')
            self.tempoAulacombo['values'] = ('')


            self.laboratorios = Fila()
            self.laboratorios.filaLaboratorios()
            tipo = Fila()
            for labs in self.laboratorios.dados:
                if labs.tipoLab == self.labtipo.get():
                    tipo.adicionar(labs.numeroChave)
            self.labsala['values'] = (tipo.dados)

        def turnoPreenchimento(event):
            self.labturno.set('')
            self.tempoAulacombo.set('')
            self.tempoAulacombo['values'] = ('')
            self.labturno['values'] = ('Matutino', 'Vespertino', 'Noturno')


        def preencherTurmaTempo(event):
            '''preenche o tempo de Aula de acordo com os agendamentos já feitos, sem aparecer os indisponiveis'''
            self.tempoAulacombo.set('')
            self.tempoAulacombo['values'] = ('')
            '''instancia Fila'''
            self.agenda = Fila()
            '''chama metodo filaAgendamentos'''
            self.agenda.filaAgendamentos()
            if self.labturno.get()=='Noturno':
                self.labturmas.set('')
                self.labturmas['values']=('ADS','Física',"Engenharia Civil",'ECA',"M.S.I.Sub",'Outros')

                self.listatempo = []
                for objt in self.agenda.dados:
                    if objt.data == self.dataAgendamento.get() and objt.laboratorio == self.labtipo.get() and self.labsala.get()==objt.sala and objt.status != 'Concluído' and objt.turno == self.labturno.get():
                        self.listatempo.append(objt.tempos)
                self.tempos = ['Todos os Tempos', '1° Tempo', '2° Tempo', '3° Tempo', '4° Tempo', '1° e 2° Tempo','3° e 4° Tempo']
                tempx = []


                for i in range(len(self.tempos)):
                    if self.tempos[i] not in self.listatempo:
                        tempx.append(self.tempos[i])
                if 'Todos os Tempos' in self.listatempo:
                    tempx = ['Indisponivel']
                if '3° e 4° Tempo' in self.listatempo:
                    temp = []
                    for i in range(len(tempx)):

                        if tempx[i] != '3° Tempo' and tempx[i] != '4° Tempo' and tempx[i] != 'Todos os Tempos':
                            temp.append(tempx[i])
                    tempx = temp
                if '1° e 2° Tempo' in self.listatempo:
                    temp = []
                    for i in range(len(tempx)):

                        if tempx[i] != '1° Tempo' and tempx[i] != '2° Tempo' and tempx[i] != 'Todos os Tempos':
                            temp.append(tempx[i])
                    tempx = temp
                if '1° Tempo' in self.listatempo or '2° Tempo' in self.listatempo:
                    temp = []
                    for i in range(len(tempx)):

                        if tempx[i] != '1° e 2° Tempo' and tempx[i] != 'Todos os Tempos':
                            temp.append(tempx[i])
                    tempx = temp
                if '3° Tempo' in self.listatempo or '4° Tempo' in self.listatempo:
                    temp = []
                    for i in range(len(tempx)):

                        if tempx[i] != '3° e 4° Tempo' and tempx[i] != 'Todos os Tempos':
                            temp.append(tempx[i])
                    tempx = temp
                self.tempos = tempx
                if len(self.tempos) == 0:
                    self.tempos = ['Indisponível']
                self.tempoAulacombo['values'] =(self.tempos)



            elif self.labturno.get()=='Vespertino':
                self.labturmas.set('')
                self.labturmas['values'] = ('Tec.Informática', 'Tec.Química', "Tec.Edificações",'Tec.Eletrotécnica',"Engenharia Civil",'ECA','Outros')

                self.listatempo = []
                for objt in self.agenda.dados:
                    if objt.data == self.dataAgendamento.get() and objt.laboratorio == self.labtipo.get() and self.labsala.get() == objt.sala and objt.status != 'Concluído' and objt.turno == self.labturno.get():
                        self.listatempo.append(objt.tempos)
                self.tempos = ['Todos os Tempos', '1° Tempo', '2° Tempo', '3° Tempo', '4° Tempo',  '5° Tempo', '6° Tempo','1° e 2° Tempo',
                               '3° e 4° Tempo','5° e 6° Tempo']
                tempx = []

                for i in range(len(self.tempos)):
                    if self.tempos[i] not in self.listatempo:
                        tempx.append(self.tempos[i])
                if 'Todos os Tempos' in self.listatempo:
                    tempx = ['Indisponível']
                if '3° e 4° Tempo' in self.listatempo:
                    temp = []
                    for i in range(len(tempx)):

                        if tempx[i] != '3° Tempo' and tempx[i] != '4° Tempo' and tempx[i] != 'Todos os Tempos':
                            temp.append(tempx[i])
                    tempx = temp
                if '1° e 2° Tempo' in self.listatempo:
                    temp = []
                    for i in range(len(tempx)):

                        if tempx[i] != '1° Tempo' and tempx[i] != '2° Tempo' and tempx[i] != 'Todos os Tempos':
                            temp.append(tempx[i])
                    tempx = temp
                if '5° e 6° Tempo' in self.listatempo:
                    temp = []
                    for i in range(len(tempx)):

                        if tempx[i] != '5° Tempo' and tempx[i] != '6° Tempo' and tempx[i] != 'Todos os Tempos':
                            temp.append(tempx[i])
                    tempx = temp
                if '5° Tempo' in self.listatempo or '6° Tempo' in self.listatempo:
                    temp = []
                    for i in range(len(tempx)):

                        if tempx[i] != '5° e 6° Tempo' and tempx[i] != 'Todos os Tempos':
                            temp.append(tempx[i])
                    tempx = temp
                if '1° Tempo' in self.listatempo or '2° Tempo' in self.listatempo:
                    temp = []
                    for i in range(len(tempx)):

                        if tempx[i] != '1° e 2° Tempo' and tempx[i] != 'Todos os Tempos':
                            temp.append(tempx[i])
                    tempx = temp
                if '3° Tempo' in self.listatempo or '4° Tempo' in self.listatempo:
                    temp = []
                    for i in range(len(tempx)):

                        if tempx[i] != '3° e 4° Tempo' and tempx[i] != 'Todos os Tempos':
                            temp.append(tempx[i])
                    tempx = temp
                self.tempos = tempx
                if len(self.tempos) == 0:
                    self.tempos = ['Indisponível']
                self.tempoAulacombo['values'] = (self.tempos)
            elif self.labturno.get()=='Matutino':
                self.labturmas.set('')
                self.labturmas['values'] = ('Tec.Informática', 'Tec.Química', "Tec.Edificações", 'Tec.Eletrotécnica','Outros')

                self.listatempo = []
                for objt in self.agenda.dados:
                    if objt.data == self.dataAgendamento.get() and objt.laboratorio == self.labtipo.get() and self.labsala.get() == objt.sala and objt.status != 'Concluído' and objt.turno == self.labturno.get():
                        self.listatempo.append(objt.tempos)
                self.tempos = ['Todos os Tempos', '1° Tempo', '2° Tempo', '3° Tempo', '4° Tempo', '5° Tempo',
                               '6° Tempo', '1° e 2° Tempo',
                               '3° e 4° Tempo', '5° e 6° Tempo']
                tempx = []

                for i in range(len(self.tempos)):
                    if self.tempos[i] not in self.listatempo:
                        tempx.append(self.tempos[i])
                if 'Todos os Tempos' in self.listatempo:
                    tempx = ['Indisponível']
                if '3° e 4° Tempo' in self.listatempo:
                    temp = []
                    for i in range(len(tempx)):

                        if tempx[i] != '3° Tempo' and tempx[i] != '4° Tempo' and tempx[i] != 'Todos os Tempos':
                            temp.append(tempx[i])
                    tempx = temp
                if '1° e 2° Tempo' in self.listatempo:
                    temp = []
                    for i in range(len(tempx)):

                        if tempx[i] != '1° Tempo' and tempx[i] != '2° Tempo' and tempx[i] != 'Todos os Tempos':
                            temp.append(tempx[i])
                    tempx = temp
                if '5° e 6° Tempo' in self.listatempo:
                    temp = []
                    for i in range(len(tempx)):

                        if tempx[i] != '5° Tempo' and tempx[i] != '6° Tempo' and tempx[i] != 'Todos os Tempos':
                            temp.append(tempx[i])
                    tempx = temp
                if '5° Tempo' in self.listatempo or '6° Tempo' in self.listatempo:
                    temp = []
                    for i in range(len(tempx)):

                        if tempx[i] != '5° e 6° Tempo' and tempx[i] != 'Todos os Tempos':
                            temp.append(tempx[i])
                    tempx = temp
                if '1° Tempo' in self.listatempo or '2° Tempo' in self.listatempo:
                    temp = []
                    for i in range(len(tempx)):

                        if tempx[i] != '1° e 2° Tempo' and tempx[i] != 'Todos os Tempos':
                            temp.append(tempx[i])
                    tempx = temp
                if '3° Tempo' in self.listatempo or '4° Tempo' in self.listatempo:
                    temp = []
                    for i in range(len(tempx)):
                        if tempx[i] != '3° e 4° Tempo' and tempx[i] != 'Todos os Tempos':
                            temp.append(tempx[i])
                    tempx = temp
                self.tempos = tempx
                if len(self.tempos) == 0:
                    self.tempos = ['Indisponível']
                self.tempoAulacombo['values'] = (self.tempos)
        def preencherPeriodo(event):
            self.periodocombo.set('')
            if self.labturmas.get()=='ADS':
                self.periodocombo['values']=('1º','2º','3º','4º','5º','6º')
            elif self.labturmas.get()=='Engenharia Civil':
                self.periodocombo['values']=('1º','2º','3º','4º','5º','6º','7º','8º','9º','10º','11º','12º')
            elif self.labturmas.get()=='ECA':
                self.periodocombo['values']=('1º','2º','3º','4º','5º','6º','7º','8º','9º','10º')
            elif self.labturmas.get()=='Física':
                self.periodocombo['values']=('1º','2º','3º','4º','5º','6º','7º','8º')
            elif self.labturmas.get()=='M.S.I.Sub':
                self.periodocombo['values']=('1º','2º','3º')
            elif self.labturmas.get()=='Tec.Informática'or self.labturmas.get()=='Tec.Química'or self.labturmas.get()=='Tec.Eletrotécnica' or self.labturmas.get()=='Tec.Edificações':
                self.periodocombo['values']=('1º','2º','3º','4º')
            elif self.labturmas.get() =='Outros':
                self.periodocombo['values'] = ('-')
        def apagar(event):
            self.pesquisavar.set('')
        def carregarData(event):
            self.labturno.set('')
            self.tempoAulacombo.set('')
            listaDias=[]
            hj = date.today()

            for i in range (30):
                if hj.day<10 and hj.month<10:
                    listaDias.append('0{}-0{}-{}'.format(hj.day, hj.month, hj.year))
                elif hj.day<10 and hj.month>=10:
                    listaDias.append('0{}-{}-{}'.format(hj.day, hj.month, hj.year))
                elif hj.month<10 and hj.day >=10:
                    listaDias.append('{}-0{}-{}'.format(hj.day, hj.month, hj.year))
                else:
                    listaDias.append('{}-{}-{}'.format(hj.day, hj.month, hj.year))

                hj = date.fromordinal(hj.toordinal() + 1)

            self.dataAgendamento['values']=(listaDias)



# ==========================================================================================================================================================
# ==========================================================================================================================================================

# =================================================== FUNÇÃO PARA VALIDAR O AGENDAMENTO DO LABORATORIO ===================================================
# ==========================================================================================================================================================
        def validarAgendamento():
            if self.dataAgendamento.get() != ''and self.labtipo.get()!='' and self.labsala.get() !='' and self.tempoAulacombo.get() !='Indisponivel' and self.tempoAulacombo.get() !='' and self.labturno.get() !='' and self.labturmas.get() != '' and self.periodocombo.get()!='' and self.tempoAulacombo.get()!='' and self.entradavar.get()!='':
                '''Se os dados inseridos estiverem corretos'''
                self.prof = self.entradavar.get().split(',')
                '''instancia Agendamento e passa os .get() dos dados como parametro'''
                agenda = Agendamento(self.labtipo.get(),self.labsala.get(),self.labturno.get(),self.dataAgendamento.get(),self.tempoAulacombo.get(),self.periodocombo.get()+self.labturmas.get(),self.prof[1])
                '''Chama metodo cadastrarAgendamento'''
                agenda.cadastrarAgendamento()
                self.labtipo.set('')
                self.labsala.set('')
                self.labsala['values'] =('')
                self.labturno.set('')
                self.labturno['values'] = ('')
                self.labturmas.set('')
                self.labturmas['values'] = ('')
                self.dataAgendamento.set('')
                self.dataAgendamento['values'] = ('')
                self.tempoAulacombo.set('')
                self.tempoAulacombo['values'] =('')
                self.entradavar.set('')
                self.periodocombo.set('')
                self.periodocombo['values']=('')
            else:
                '''se combobox de tempos de aula estiverem em indisponivel'''
                if self.tempoAulacombo.get() =='Indisponível':
                    messagebox.showinfo('AVISO','LABORATÓRIO NÃO ESTÁ DISPONíVEL EM NENHUM TEMPO DE AULA')
                else:
                    messagebox.showinfo('AVISO', 'PREENCHA TODOS OS DADOS CORRETAMENTE')
                self.labtipo.set('')
                self.labsala.set('')
                self.labsala['values'] = ('')
                self.labturno.set('')
                self.labturno['values'] = ('')
                self.labturmas.set('')
                self.labturmas['values'] = ('')
                self.dataAgendamento.set('')
                self.dataAgendamento['values'] = ('')
                self.tempoAulacombo.set('')
                self.tempoAulacombo['values'] = ('')
                self.entradavar.set('')
                self.periodocombo.set('')
                self.periodocombo['values'] = ('')


# =================================================== COSNTRUÇÃO DA TELA PRINCIPAL =========================================================================
# ==========================================================================================================================================================
        self.janAgendar = Tk()
        vcmd = self.janAgendar.register(func=limitarEntry)
        self.janAgendar['bg']='#5F9EA0'
        screen_width = 1024
        screen_height = 768
        self.janAgendar.title('Labifro')
        self.janAgendar.geometry('{}x{}+0+0'.format(screen_width, screen_height))
        self.frameTela = Frame(self.janAgendar)
        self.janAgendar.iconbitmap('icons_images/iconewindow.ico')
        self.frameTela['bg'] = '#5F9EA0'
        self.frameTela.place(x=10, y=10, height=680, width=1260)
        self.frametop = Frame(self.janAgendar, height=100, width=screen_width - 100, bg='#708090')
        self.frametop.pack()
        self.photo = PhotoImage(file='icons_images/iconecad.png')
        self.photo = self.photo.subsample(1, 1)
        self.labelimg = Label(self.frametop, image=self.photo)
        self.labelimg['bg'] = '#708090'
        self.labelimg.place(x=self.frametop['width'] / 2 - 300, y=15)
        self.labelcad = Label(self.frametop, text='Agendar Laboratório', font=('Times', 30))
        self.labelcad['bg'] = '#708090'
        self.labelcad.place(x=screen_width / 2 - 250, y=25)
        self.frameconteiner = Frame(height=screen_height / 2 + 150, width=screen_width / 2,bg='#5F9EA0')
        self.y = self.frameconteiner['height']
        self.x = self.frameconteiner['width']
        self.frameconteiner.pack()
        self.imgback = PhotoImage(file='icons_images/back.png')


        self.back = Button(self.frametop, image=self.imgback, height=30, width=30, relief=FLAT, activebackground='#00FF7F')
        self.back.place(x=10, y=50)
        self.back['command'] = back
        self.back['bg'] = '#5F9EA0'
        self.back['relief'] = FLAT
        self.back['cursor'] = 'exchange'
# ==========================================================================================================================================================
# =========================================================WIDGETS==========================================================================================
# ==========================================================================================================================================================
        self.labeltipo = Label(self.frameconteiner, text = "Tipo de Laboratório",bg='#5F9EA0')
        self.labeltipo.place(x=60,y=self.y/4-20)
        self.labtipo = ttk.Combobox(self.frameconteiner, state="readonly")
        self.labtipo['values'] = ('Informática', 'Química', 'Física', 'Edificações', 'Biologia', 'Eletrotécnica')
        self.labelsala = Label(self.frameconteiner,text = 'Chave',bg='#5F9EA0')
        self.labsala = ttk.Combobox(self.frameconteiner, state="readonly",width=5)
        self.labtipo.bind('<<ComboboxSelected>>', autoPreenchimento)
        self.labsala.bind('<<ComboboxSelected>>', turnoPreenchimento)
        self.labelsala.place(x=195,y=self.y/4-20)
        self.labelturno = Label(self.frameconteiner,text = 'Turno',bg='#5F9EA0')
        self.labturno = ttk.Combobox(self.frameconteiner,state='readonly')

        self.labturno.place(x=250,y=self.y/4)
        self.labelturno.place(x=290,y=self.y/4-20)
        self.labturno.bind('<<ComboboxSelected>>',preencherTurmaTempo)

        self.labtipo.place(x=40,y=self.y/4)
        self.labsala.place(x=190,y=self.y/4)
#########################################################
        self.entradavar = StringVar()
        self.pesquisavar =StringVar()
        self.pesquisavar.set('Digite Siape...')
        self.entradapesquisa = Entry(self.frameconteiner,textvariable=self.pesquisavar,relief = FLAT,validate='key', validatecommand=(vcmd,'%P'))
        self.entradapesquisa.place(x=40,y= self.y/4+100)
        self.entradapesquisa.bind('<Button-1>',apagar)
        self.imgbtlupa = PhotoImage(file='icons_images/lup.png')
        self.btlupa = Button(self.frameconteiner,image = self.imgbtlupa, height=15, width=15,relief = GROOVE,command= pesquisa_siape).place(x=145,y=self.y/4+99)
        self.entradadsb = Entry(self.frameconteiner,textvariable =self.entradavar,state = DISABLED,width = 38).place(x=170,y=self.y/4+100)
        self.labelturma = Label(self.frameconteiner,text='Cursos',bg='#5F9EA0')
        self.labelturma.place(x=90,y=self.y/4+30)
        self.labturmas = ttk.Combobox(self.frameconteiner,state='readonly')
        self.labturmas.bind('<<ComboboxSelected>>',preencherPeriodo)
        self.labturmas.place(x=40,y=self.y/4+50)
        self.labelperiodo = Label(self.frameconteiner,text='Turma',bg='#5F9EA0')
        self.periodocombo = ttk.Combobox(self.frameconteiner,state='readonly',width = 5)
        self.labelperiodo.place(x=192,y=self.y/4+30)
        self.periodocombo.place(x=190,y=self.y/4+50)
        self.labeltempoAula = Label(self.frameconteiner,text = 'Tempos de aula',bg='#5F9EA0')
        self.labeltempoAula.place(x=270,y=self.y/4+30)
        self.tempoAulacombo = ttk.Combobox(self.frameconteiner,state='readonly')
        self.tempoAulacombo.place(x=250,y=self.y/4+50)
        self.datalabel = Label(self.frameconteiner,text='Reservar para o dia',bg='#5F9EA0')
        self.datalabel.place(x=40,y=self.y/4-60)
        self.dataAgendamento = ttk.Combobox(self.frameconteiner,state='readonly')
        self.dataAgendamento.place(x=40,y=self.y/4-43)
        self.dataAgendamento.bind('<Button-1>',carregarData)


        self.imgbt = PhotoImage(file='icons_images/Save1.png')
        self.btAgendar = Button(self.frameconteiner, text='Cadastrar', height=46, width=60, image=self.imgbt,activebackground='#00FF7F', relief=GROOVE,bg='#D3D3D3',command = validarAgendamento)
        self.btAgendar.place(x=325,y=self.y/2+60)



        self.janAgendar.mainloop()
