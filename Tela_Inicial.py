from tkinter import *
from functools import partial
from TelaCadastro import TelaCadastro
from TelaAgendar_lab import TelaAgendar_lab
from TelaReservasRealizadas import TelaReservasRealizadas
from TelaCadastro_Lab import TelaCadastro_Lab
from TelaControleChave import TelaControleChave


class Tela_Inicial(object):
    def __init__(self,user,siape):
        self.tela_inicio = Tk()
        self.tela_inicio.iconbitmap('icons_images/iconewindow.ico')
        screen_width = 1024
        screen_height = 768
        self.tela_inicio.geometry('{}x{}+0+0'.format(screen_width,screen_height))
        self.tela_inicio.title('Labifro')
        self.fm = Frame(self.tela_inicio,height = screen_height,width=(screen_width/2)+100,bg = '#5F9EA0')
        self.fm.pack()
        self.tela_inicio['bg']='#5F9EA0'
        def Entrar(bt):
            textbt = bt
            self.tela_inicio.destroy()
            if textbt =='Cadastro De Usuário':
                entra = TelaCadastro(user,siape)
            elif textbt == 'Agendar Laboratório':
                entra = TelaAgendar_lab(user,siape)
            elif textbt =='Todas as Reservas':
                entra = TelaReservasRealizadas(user,siape)
            elif textbt =="Cadastrar Laboratório":
                entra = TelaCadastro_Lab(user,siape)
            elif textbt == 'Confirmar Entrega':
                entra = TelaControleChave(user,siape)
            elif textbt == 'voltar pra Login':
                from TelaLogin import TelaLogin
                TelaLogin()


        self.logo = PhotoImage(file='icons_images/iconered.png')
        self.logo = self.logo.subsample(1, 1)
        self.labellogo = Label(self.fm, image=self.logo)
        self.labellogo['bg'] = self.tela_inicio['bg']
        self.labellogo.place(x=(self.fm['width']/2)-65, y=310)
        self.labelInfo = Label(self.fm,text='Sistema de Agendamento de Laboratórios',font = ("Elephant",12))
        self.labelInfo.place(x=(self.fm['width']/2)-165,y=50)

        self.labelInfo['bg'] ='#5F9EA0'

        self.btcadastro_user = Button(self.fm,text ='Cadastrar Usuário', height = 3,width = 20,activebackground= '#5F9EA0',bg ='#006400',fg="white",relief = GROOVE)
        self.btcadastro_user.place(x=0,y=150)



        self.btcadastro_user['command']=partial(Entrar,'Cadastro De Usuário')
        self.btagendar_lab = Button(self.fm,text = 'Agendar Laboratório',height = 3,width = 20,activebackground= '#5F9EA0',bg ='#006400',fg="white",relief = GROOVE)
        self.btagendar_lab.place(x = 0,y = 270)
        self.btagendar_lab['command'] = partial(Entrar,'Agendar Laboratório')
        self.btreservas = Button(self.fm,text = 'Todas as Reservas',height = 3,width = 20,activebackground= '#5F9EA0',bg ='#006400',fg="white",relief = GROOVE)
        self.btreservas.place( x=(self.fm['width']/2)-68,y =210)
        self.btreservas['command']=partial(Entrar,'Todas as Reservas')
        self.btcadLab = Button(self.fm,text="Cadastrar Laboratório",height = 3,width = 20,activebackground= '#5F9EA0',bg ='#006400',fg="white",relief = GROOVE)
        self.btcadLab.place (x=(screen_width/2)-50,y=150)
        self.btcadLab['command']=partial(Entrar,"Cadastrar Laboratório")
        self.btChaveSala = Button(self.fm,text = 'Confirmar Entrega',height = 3,width = 20,activebackground= '#5F9EA0',bg ='#006400',fg="white",relief = GROOVE	)
        self.btChaveSala.place(x=(screen_width/2)-50,y=270)
        self.btChaveSala['command']=partial(Entrar,'Confirmar Entrega')
        self.photologout = PhotoImage(file= 'icons_images/logout1.png')
        self.logout = Button(self.fm,image = self.photologout,height = 35,width=35,relief=FLAT,activebackground= '#5F9EA0')
        self.logout['bg']='#5F9EA0'
        self.logout.place(x=0,y=480)
        self.logout['command']=partial (Entrar,'voltar pra Login')
        self.lbbv = Label(self.fm,text = 'Bem vindo(a), '+user,font = ("Elephant",10),bg='#5F9EA0')
        self.lbbv.place(x=(self.fm['width']/2)+50,y=480)





        self.tela_inicio.mainloop()

