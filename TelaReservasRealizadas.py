from datetime import date
from functools import partial
from tkinter import *
from Planilha import Planilha

class TelaReservasRealizadas(object):
    def __init__(self, user, siape):
        '''Classe fronteira para a interação do usuario e a geração de planilhas'''
        self.telareservas = Tk()
        self.telareservas.title('Labifro')
        screen_width = 1024
        screen_height = 768
        self.telareservas.geometry('{}x{}+0+0'.format(screen_width,screen_height))
        self.telareservas['bg'] = '#5F9EA0'
        self.telareservas.iconbitmap('icons_images/iconewindow.ico')
        self.frametela = Frame(self.telareservas,width=screen_width/2+200,height=screen_height/2+130,bg='#5F9EA0')


        def back():
            '''função que volta pra tela inicial'''
            from Tela_Inicial import Tela_Inicial
            self.telareservas.destroy()
            volta = Tela_Inicial(user,siape)
        def gerar(mes):
            '''função que gera planilha'''
            '''instancia Planilha'''
            gera = Planilha(mes,self.hj.year)
            '''Chama metodo gerarPlanilha'''
            gera.gerarPlanilha()



        self.frametop = Frame(self.telareservas,height=100,width = screen_width-100,bg = '#708090')
        self.frametop.pack()
        self.frametela.pack()
        self.listaMeses = ('Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro','Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')
        self.hj = date.today()


        self.photo = PhotoImage(file='icons_images/iconecad.png')
        self.photo = self.photo.subsample(1, 1)
        self.labelimg = Label(self.frametop, image=self.photo)
        self.labelimg['bg'] = '#708090'
        self.labelimg.place(x=self.frametop['width']/2-300, y=15)
        self.labelReservas = Label(self.frametop, text='Reservas de Laboratórios', font=('Times', 30))
        self.labelReservas['bg'] = '#708090'
        self.labelReservas.place(x=screen_width/2-250, y=25)
        self.logomeio = PhotoImage(file = 'icons_images/iconered.png')
        self.logomeiolabel = Label(self.frametela,image=self.logomeio,bg='#5F9EA0')
        self.logomeiolabel.place(x=400,y=80)
        self.labelExplicativo = Label(self.frametela,text = 'Download de planilhas na pasta Planilhas, com as informações\n relacionadas a os agendamentos de determinado mês.',bg ='#5F9EA0' )
        self.labelExplicativo.place(x=315,y=250)
        self.PhotoDownload = PhotoImage(file='icons_images/download.png')
        self.btDownloadReservasProx = Button(self.frametela,height=60,width=150,image=self.PhotoDownload,relief = GROOVE,bg ='#5F9EA0',font=('Times', 13),activebackground= '#00FF7F')
        self.btDownloadReservasProx['command'] = partial(gerar,self.hj.month+1)
        self.btDownloadReservasProx.place(x=0,y=100)
        self.labelDownProximoMes = Label(self.frametela,text = ('Reservas de {}'.format(self.listaMeses[self.hj.month])),bg ='#5F9EA0' )
        self.labelDownProximoMes.place(x=0,y=75)
        self.btDownloadReservasAtual = Button(self.frametela,height=60,width=150,image=self.PhotoDownload,relief = GROOVE,bg ='#5F9EA0',font=('Times', 13),activebackground= '#00FF7F' )
        self.btDownloadReservasAtual.place(x=0,y=200)
        self.btDownloadReservasAtual['command'] = partial(gerar, self.hj.month)
        self.labelDownAtual = Label(self.frametela, text=('Reservas de {}'.format(self.listaMeses[self.hj.month-1])), bg='#5F9EA0')
        self.labelDownAtual.place(x=0, y=175)
        self.btDownloadReservasAnt = Button(self.frametela, height=60, width=150, image=self.PhotoDownload,relief=GROOVE, bg='#5F9EA0', font=('Times', 13),activebackground='#00FF7F')
        self.btDownloadReservasAnt.place(x=0, y=300)
        self.btDownloadReservasAnt['command'] = partial(gerar, self.hj.month-1)
        self.labelDownAnterior = Label(self.frametela, text=('Reservas de {}'.format(self.listaMeses[self.hj.month - 2])),bg='#5F9EA0')
        self.labelDownAnterior.place(x=0, y=275)
        self.imgback = PhotoImage(file='icons_images/back.png')
        self.back = Button(self.frametop, image=self.imgback, height=30, width=30, relief=FLAT,activebackground='#00FF7F')
        self.back.place(x=10, y=50)
        self.back['command'] = back
        self.back['bg'] = '#5F9EA0'
        self.back['relief']=FLAT
        self.back['cursor'] = 'exchange'
        self.telareservas.mainloop()
