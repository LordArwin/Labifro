from datetime import date
from functools import partial
from tkinter import*
from tkinter import ttk, messagebox
from Agendamento import Agendamento
from Fila import Fila

from Laboratorio import Laboratorio
class TelaControleChave(object):
    def __init__(self,nome,siape,desativa = 1):

#========================================================================================
##################FUNÇÃO PARA VOLTAR PRA TELA INICIAL ###################################
        def back():
            from Tela_Inicial import Tela_Inicial
            self.telaEntrega.destroy()
            volta = Tela_Inicial(nome,siape)
        def logout():
            from TelaLogin import TelaLogin
            self.telaEntrega.destroy()
            TelaLogin()
#=======================================================================================
#######################FUNÇÃO DE MUDANÇA NO STATUS DO AGENDAMENTO#######################

        def mudaStatus(texto):

            if texto == 'checkcoluna1':
                if self.checkcoluna1var.get() == 'Em andamento':
                    self.servidorconf1h.set(siape)
                    temp = Agendamento(self.laboratorio1a.get(),self.chave1b.get(),self.turno1c.get(),self.data1d.get(),self.temposAula1f.get(),self.turma1e.get(),self.entradapesquisavar.get(),self.checkcoluna1var.get(),self.servidorconf1h.get())
                    temp.controleChave()

                    self.checkcoluna1var.set('Concluído')
                    self.checkcancel1.place(x=1000,y=1000)

                elif self.checkcoluna1var.get() == 'Concluído':
                    self.servidordev1i.set(siape)
                    temp = Agendamento(self.laboratorio1a.get(), self.chave1b.get(), self.turno1c.get(), self.data1d.get(),self.temposAula1f.get(), self.turma1e.get(), self.entradapesquisavar.get(),self.checkcoluna1var.get(),self.servidorconf1h.get(),self.servidordev1i.get())
                    temp.controleChave()
                    self.checkcoluna1.place(x=1000,y=1000)
                    self.laboratorio1a.set('')
                    self.chave1b.set('')
                    self.turno1c.set('')
                    self.data1d.set('')
                    self.turma1e.set('')
                    self.temposAula1f.set('')
                    self.siapeprofessor1g.set('')
                    self.servidorconf1h.set('')
                    self.servidordev1i.set('')

            if texto == 'checkcoluna3':
                if self.checkcoluna3var.get() == 'Em andamento':
                    self.servidorconf3h.set(siape)
                    temp = Agendamento(self.laboratorio3a.get(),self.chave3b.get(),self.turno3c.get(),self.data3d.get(),self.temposAula3f.get(),self.turma3e.get(),self.entradapesquisavar.get(),self.checkcoluna3var.get(),self.servidorconf3h.get())
                    temp.controleChave()

                    self.checkcoluna3var.set('Concluído')
                    self.checkcancel3.place(x=3000,y=1000)

                elif self.checkcoluna3var.get() == 'Concluído':
                    self.servidordev3i.set(siape)
                    temp = Agendamento(self.laboratorio3a.get(), self.chave3b.get(), self.turno3c.get(), self.data3d.get(),self.temposAula3f.get(), self.turma3e.get(), self.entradapesquisavar.get(),self.checkcoluna3var.get(),self.servidorconf3h.get(),self.servidordev3i.get())
                    temp.controleChave()
                    self.checkcoluna3.place(x=3000,y=3000)
                    self.laboratorio3a.set('')
                    self.chave3b.set('')
                    self.turno3c.set('')
                    self.data3d.set('')
                    self.turma3e.set('')
                    self.temposAula3f.set('')
                    self.siapeprofessor3g.set('')
                    self.servidorconf3h.set('')
                    self.servidordev3i.set('')
            if texto == 'checkcoluna4':
                if self.checkcoluna4var.get() == 'Em andamento':
                    self.servidorconf4h.set(siape)
                    temp = Agendamento(self.laboratorio4a.get(),self.chave4b.get(),self.turno4c.get(),self.data4d.get(),self.temposAula4f.get(),self.turma4e.get(),self.entradapesquisavar.get(),self.checkcoluna4var.get(),self.servidorconf4h.get())
                    temp.controleChave()

                    self.checkcoluna4var.set('Concluído')
                    self.checkcancel4.place(x=4000,y=4000)

                elif self.checkcoluna4var.get() == 'Concluído':
                    self.servidordev4i.set(siape)
                    temp = Agendamento(self.laboratorio4a.get(), self.chave4b.get(), self.turno4c.get(), self.data4d.get(),self.temposAula4f.get(), self.turma4e.get(), self.entradapesquisavar.get(),self.checkcoluna4var.get(),self.servidorconf4h.get(),self.servidordev4i.get())
                    temp.controleChave()
                    self.checkcoluna4.place(x=4000,y=4000)
                    self.laboratorio4a.set('')
                    self.chave4b.set('')
                    self.turno4c.set('')
                    self.data4d.set('')
                    self.turma4e.set('')
                    self.temposAula4f.set('')
                    self.siapeprofessor4g.set('')
                    self.servidorconf4h.set('')
                    self.servidordev4i.set('')
            if texto == 'checkcoluna6':
                if self.checkcoluna6var.get() == 'Em andamento':
                    self.servidorconf6h.set(siape)
                    temp = Agendamento(self.laboratorio6a.get(),self.chave6b.get(),self.turno6c.get(),self.data6d.get(),self.temposAula6f.get(),self.turma6e.get(),self.entradapesquisavar.get(),self.checkcoluna6var.get(),self.servidorconf6h.get())
                    temp.controleChave()

                    self.checkcoluna6var.set('Concluído')
                    self.checkcancel6.place(x=6000,y=6000)

                elif self.checkcoluna6var.get() == 'Concluído':
                    self.servidordev6i.set(siape)
                    temp = Agendamento(self.laboratorio6a.get(), self.chave6b.get(), self.turno6c.get(), self.data6d.get(),self.temposAula6f.get(), self.turma6e.get(), self.entradapesquisavar.get(),self.checkcoluna6var.get(),self.servidorconf6h.get(),self.servidordev6i.get())
                    temp.controleChave()
                    self.checkcoluna6.place(x=6000,y=6000)
                    self.laboratorio6a.set('')
                    self.chave6b.set('')
                    self.turno6c.set('')
                    self.data6d.set('')
                    self.turma6e.set('')
                    self.temposAula6f.set('')
                    self.siapeprofessor6g.set('')
                    self.servidorconf6h.set('')
                    self.servidordev6i.set('')
            if texto == 'checkcoluna2':
                if self.checkcoluna2var.get() == 'Em andamento':
                    self.servidorconf2h.set(siape)
                    temp = Agendamento(self.laboratorio2a.get(),self.chave2b.get(),self.turno2c.get(),self.data2d.get(),self.temposAula2f.get(),self.turma2e.get(),self.entradapesquisavar.get(),self.checkcoluna2var.get(),self.servidorconf2h.get())
                    temp.controleChave()

                    self.checkcoluna2var.set('Concluído')
                    self.checkcancel2.place(x=2000,y=2000)

                elif self.checkcoluna2var.get() == 'Concluído':
                    self.servidordev2i.set(siape)
                    temp = Agendamento(self.laboratorio2a.get(), self.chave2b.get(), self.turno2c.get(), self.data2d.get(),self.temposAula2f.get(), self.turma2e.get(), self.entradapesquisavar.get(),self.checkcoluna2var.get(),self.servidorconf2h.get(),self.servidordev2i.get())
                    temp.controleChave()
                    self.checkcoluna2.place(x=2000,y=2000)
                    self.laboratorio2a.set('')
                    self.chave2b.set('')
                    self.turno2c.set('')
                    self.data2d.set('')
                    self.turma2e.set('')
                    self.temposAula2f.set('')
                    self.siapeprofessor2g.set('')
                    self.servidorconf2h.set('')
                    self.servidordev2i.set('')
                    self.checkcoluna2.place(x=2000,y=2000)
            if texto == 'checkcoluna5':
                if self.checkcoluna5var.get() == 'Em andamento':
                    self.servidorconf5h.set(siape)
                    temp = Agendamento(self.laboratorio5a.get(),self.chave5b.get(),self.turno5c.get(),self.data5d.get(),self.temposAula5f.get(),self.turma5e.get(),self.entradapesquisavar.get(),self.checkcoluna5var.get(),self.servidorconf5h.get())
                    temp.controleChave()

                    self.checkcoluna5var.set('Concluído')
                    self.checkcancel5.place(x=5000,y=5000)

                elif self.checkcoluna5var.get() == 'Concluído':
                    self.servidordev5i.set(siape)
                    temp = Agendamento(self.laboratorio5a.get(), self.chave5b.get(), self.turno5c.get(), self.data5d.get(),self.temposAula5f.get(), self.turma5e.get(), self.entradapesquisavar.get(),self.checkcoluna5var.get(),self.servidorconf5h.get(),self.servidordev5i.get())
                    temp.controleChave()
                    self.checkcoluna5.place(x=5000,y=5000)
                    self.laboratorio5a.set('')
                    self.chave5b.set('')
                    self.turno5c.set('')
                    self.data5d.set('')
                    self.turma5e.set('')
                    self.temposAula5f.set('')
                    self.siapeprofessor5g.set('')
                    self.servidorconf5h.set('')
                    self.servidordev5i.set('')
                    self.checkcoluna5.place(x=5000,y=5000)
            else:
                if texto == "cancelacoluna1":
                    self.checkcoluna1var.set('Concluído')
                    self.checkcancel1.place(x=1000, y=1000)
                    mudaStatus('checkcoluna1')

                if texto == "cancelacoluna2":
                    self.checkcoluna2var.set('Concluído')
                    self.checkcancel2.place(x=1000, y=1000)
                    mudaStatus('checkcoluna2')

                if texto == "cancelacoluna3":
                    self.checkcoluna3var.set('Concluído')
                    self.checkcancel3.place(x=1000, y=1000)
                    mudaStatus('checkcoluna3')

                if texto == "cancelacoluna4":
                    self.checkcoluna4var.set('Concluído')
                    self.checkcancel4.place(x=1000, y=1000)
                    mudaStatus('checkcoluna4')

                if texto == "cancelacoluna5":
                    self.checkcoluna5var.set('Concluído')
                    self.checkcancel5.place(x=1000, y=1000)
                    mudaStatus('checkcoluna5')
                if texto == "cancelacoluna6":
                    self.checkcoluna6var.set('Concluído')
                    self.checkcancel6.place(x=1000, y=1000)
                    mudaStatus('checkcoluna6')

#=======================================================================================
#########################FUNÇÃO QUE LIMITA ENTRY DE SIAPE PESQUISA######################
        def apagar(event):
            self.entradapesquisavar.set('')
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
        def apagarDadosTabela():
            self.checkcancel1.place(x=1000, y=1000)
            self.checkcoluna1.place(x=1000, y=1000)
            self.checkcancel2.place(x=1000, y=1000)
            self.checkcoluna2.place(x=1000, y=1000)
            self.checkcancel3.place(x=1000, y=1000)
            self.checkcoluna3.place(x=1000, y=1000)
            self.checkcancel4.place(x=1000, y=1000)
            self.checkcoluna4.place(x=1000, y=1000)
            self.checkcancel5.place(x=1000, y=1000)
            self.checkcoluna5.place(x=1000, y=1000)
            self.checkcancel6.place(x=1000, y=1000)
            self.checkcoluna6.place(x=1000, y=1000)
            # SET VARIAVEIS DA PRIMEIRA COLUNA
            self.laboratorio1a.set('')
            self.laboratorio2a.set('')
            self.laboratorio3a.set('')
            self.laboratorio4a.set('')
            self.laboratorio5a.set('')
            self.laboratorio6a.set('')
            # SET VARIAVEIS DA SEGUNDA COLUNA CHAVES COMO ESPAÇO VAZIO
            self.chave1b.set('')
            self.chave2b.set('')
            self.chave3b.set('')
            self.chave4b.set('')
            self.chave5b.set('')
            self.chave6b.set('')
            # SET VARIAVEIS DA TERCEIRA COLUNA TURNO COMO ESPAÇO VAZIO
            self.turno1c.set('')
            self.turno2c.set('')
            self.turno3c.set('')
            self.turno4c.set('')
            self.turno5c.set('')
            self.turno6c.set('')
            # SET VARIAVEIS DA QUARTA COLUNA DATA COMO ESPAÇO VAZIO
            self.data1d.set('')
            self.data2d.set('')
            self.data3d.set('')
            self.data4d.set('')
            self.data5d.set('')
            self.data6d.set('')
            #  SET VARIAVEIS DA QUINTA COLUNA TURMA COMO ESPAÇO VAZIO
            self.turma1e.set('')
            self.turma2e.set('')
            self.turma3e.set('')
            self.turma4e.set('')
            self.turma5e.set('')
            self.turma6e.set('')
            # SET VARIAVEIS DA SEXTA COLUNA TEMPOS DE AULA COMO ESPAÇO VAZIO
            self.temposAula1f.set('')
            self.temposAula2f.set('')
            self.temposAula3f.set('')
            self.temposAula4f.set('')
            self.temposAula5f.set('')
            self.temposAula6f.set('')
            # SET VARIAVEIS DA SÉTIMA COLUNA SIAPES DOS PROFESSORES COMO ESPAÇO VAZIO
            self.siapeprofessor1g.set('')
            self.siapeprofessor2g.set('')
            self.siapeprofessor3g.set('')
            self.siapeprofessor4g.set('')
            self.siapeprofessor5g.set('')
            self.siapeprofessor6g.set('')
            # SET VARIAVEIS DA OITAVA COLUNA SIAPES DO SERVIDOR CONF.RET COMO VAZIO

            self.servidorconf1h.set('')
            self.servidorconf2h.set('')
            self.servidorconf3h.set('')
            self.servidorconf4h.set('')
            self.servidorconf5h.set('')
            self.servidorconf6h.set('')

            # SET VARIAVES DA NONA COLUNA SIAPES DO SERVIDOR CONF.DEV COMO VAZIO
            self.servidordev1i.set('')
            self.servidordev2i.set('')
            self.servidordev3i.set('')
            self.servidordev4i.set('')
            self.servidordev5i.set('')
            self.servidordev6i.set('')


    # ==================================
#=======================================================================================
######################## FUNÇÃO DE PREENCHIMENTO #######################################
        def autoPreenchimento(event):
            self.chavecombo.set('')
            self.turnocombo.set('')


            self.laboratorios = Fila()
            self.laboratorios.filaLaboratorios()
            
            tipo = []
            for labs in self.laboratorios.dados:
                if labs.tipoLab == self.tipolab.get():
                    tipo.append(labs.numeroChave)
            self.chavecombo['values'] = (tipo)
            self.turnocombo['values'] = ('Matutino','Vespertino','Noturno')
# ==================================
#=======================================================================================
######################## FUNÇÃO DE CARREGAR DATA #######################################
        def carregarData(event):
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

            self.data['values']=(listaDias)
#================================================================================================
##################### FUNÇÃO QUE VALIDA DADOS INSERIDOS PARA PESQUISA############################
        def validarPesquisa():
            apagarDadosTabela()

            #ABRE TXT ONDE ESTÃO OS DADOS E INSTÂNCIA OBJETOS DA CLASSE AGENDAMENTO PARA DENTRO DE UMA FILA
            #self.agendamentos = []
            self.fila_agendamentos = Fila()
            self.fila_agendamentos.filaAgendamentos()
            if self.tipolab.get()!='' and self.chavecombo.get()!='' and self.data.get()!='' and self.entradapesquisa.get()!='' and self.turnocombo.get():
                for agendamentos in self.fila_agendamentos.dados:
                    if agendamentos.verificarAgendamento(self.tipolab.get(),self.chavecombo.get(),self.data.get(),self.entradapesquisavar.get(),self.turnocombo.get()):
                        #INSERE OBJETOS DA CLASSE AGENDAMENTO NA FILA
                        self.dadosagendamentos.adicionar(agendamentos)
                        
                encontrados = self.dadosagendamentos.lenFila()
                if encontrados==0:
                    messagebox.showwarning('ATENÇÃO', 'NENHUM AGENDAMENTO FOI ENCONTRADO')
                if encontrados==1:
                    #PREENCHE OS LABELS COM AS INFORMAÇOES DO AGENDAMENTO
                    #COLUNA 1
                    self.laboratorio1a.set(self.dadosagendamentos.dados[0].laboratorio)
                    self.chave1b.set(self.dadosagendamentos.dados[0].sala)
                    self.turno1c.set(self.dadosagendamentos.dados[0].turno)
                    self.turma1e.set(self.dadosagendamentos.dados[0].turma)
                    self.temposAula1f.set(self.dadosagendamentos.dados[0].tempos)
                    self.data1d.set(self.dadosagendamentos.dados[0].data)
                    self.siapeprofessor1g.set(self.dadosagendamentos.dados[0].professor)
                    self.servidorconf1h.set(self.dadosagendamentos.dados[0].confirmaEntrega)
                    self.servidordev1i.set(self.dadosagendamentos.dados[0].confirmaDevolucao)
                    #MUDA O ESTADO DO BOTÃO DE STATUS
                    if self.dadosagendamentos.dados[0].status == 'Pendente':
                        self.checkcoluna1var.set('Em andamento')
                        self.checkcoluna1.place(x=0, y=0)
                        self.checkcancel1var.set('Cancelar Agendamento')
                        self.checkcancel1.place(x=0, y=25)
                    elif self.dadosagendamentos.dados[0].status == 'Em andamento':
                        self.checkcoluna1var.set('Concluído')
                        self.checkcoluna1.place(x=0, y=0)
                    # RETIRA O PRIMEIRO OBJETO DA FILA
                    self.dadosagendamentos.remover()

                elif encontrados==2:
                    # PREENCHE OS LABELS COM AS INFORMAÇOES DO AGENDAMENTO
                    # COLUNA 1
                    self.laboratorio1a.set(self.dadosagendamentos.dados[0].laboratorio)
                    self.chave1b.set(self.dadosagendamentos.dados[0].sala)
                    self.turno1c.set(self.dadosagendamentos.dados[0].turno)
                    self.turma1e.set(self.dadosagendamentos.dados[0].turma)
                    self.temposAula1f.set(self.dadosagendamentos.dados[0].tempos)
                    self.data1d.set(self.dadosagendamentos.dados[0].data)
                    self.siapeprofessor1g.set(self.dadosagendamentos.dados[0].professor)
                    self.servidorconf1h.set(self.dadosagendamentos.dados[0].confirmaEntrega)
                    self.servidordev1i.set(self.dadosagendamentos.dados[0].confirmaDevolucao)
                    # MUDA O ESTADO DO BOTÃO DE STATUS
                    if self.dadosagendamentos.dados[0].status == 'Pendente':
                        self.checkcoluna1var.set('Em andamento')
                        self.checkcoluna1.place(x=0, y=0)
                        self.checkcancel1var.set('Cancelar Agendamento')
                        self.checkcancel1.place(x=0, y=25)
                    elif self.dadosagendamentos.dados[0].status == 'Em andamento':
                        self.checkcoluna1var.set('Concluído')
                        self.checkcoluna1.place(x=0, y=0)
                    # RETIRA O PRIMEIRO OBJETO DA FILA
                    self.dadosagendamentos.remover()
                    #COLUNA 2
                    self.laboratorio2a.set(self.dadosagendamentos.dados[0].laboratorio)
                    self.chave2b.set(self.dadosagendamentos.dados[0].sala)
                    self.turno2c.set(self.dadosagendamentos.dados[0].turno)
                    self.turma2e.set(self.dadosagendamentos.dados[0].turma)
                    self.temposAula2f.set(self.dadosagendamentos.dados[0].tempos)
                    self.data2d.set(self.dadosagendamentos.dados[0].data)
                    self.siapeprofessor2g.set(self.dadosagendamentos.dados[0].professor)
                    self.servidorconf2h.set(self.dadosagendamentos.dados[0].confirmaEntrega)
                    self.servidordev2i.set(self.dadosagendamentos.dados[0].confirmaDevolucao)
                    # MUDA O ESTADO DO BOTÃO DE STATUS
                    if self.dadosagendamentos.dados[0].status == 'Pendente':
                        self.checkcoluna2var.set('Em andamento')
                        self.checkcoluna2.place(x=0, y=0)
                        self.checkcancel2var.set('Cancelar Agendamento')
                        self.checkcancel2.place(x=0, y=25)
                    elif self.dadosagendamentos.dados[0].status == 'Em andamento':
                        self.checkcoluna2var.set('Concluído')
                        self.checkcoluna2.place(x=0, y=0)
                    # RETIRA O PRIMEIRO OBJETO DA FILA
                    self.dadosagendamentos.remover()
                elif encontrados==3:
                    # PREENCHE OS LABELS COM AS INFORMAÇOES DO AGENDAMENTO
                    # COLUNA 1
                    self.laboratorio1a.set(self.dadosagendamentos.dados[0].laboratorio)
                    self.chave1b.set(self.dadosagendamentos.dados[0].sala)
                    self.turno1c.set(self.dadosagendamentos.dados[0].turno)
                    self.turma1e.set(self.dadosagendamentos.dados[0].turma)
                    self.temposAula1f.set(self.dadosagendamentos.dados[0].tempos)
                    self.data1d.set(self.dadosagendamentos.dados[0].data)
                    self.siapeprofessor1g.set(self.dadosagendamentos.dados[0].professor)
                    self.servidorconf1h.set(self.dadosagendamentos.dados[0].confirmaEntrega)
                    self.servidordev1i.set(self.dadosagendamentos.dados[0].confirmaDevolucao)
                    # MUDA O ESTADO DO BOTÃO DE STATUS
                    if self.dadosagendamentos.dados[0].status == 'Pendente':
                        self.checkcoluna1var.set('Em andamento')
                        self.checkcoluna1.place(x=0, y=0)
                        self.checkcancel1var.set('Cancelar Agendamento')
                        self.checkcancel1.place(x=0, y=25)
                    elif self.dadosagendamentos.dados[0].status == 'Em andamento':
                        self.checkcoluna1var.set('Concluído')
                        self.checkcoluna1.place(x=0, y=0)

                    # RETIRA O PRIMEIRO OBJETO DA FILA
                    self.dadosagendamentos.remover()
                    #COLUNA 2
                    self.laboratorio2a.set(self.dadosagendamentos.dados[0].laboratorio)
                    self.chave2b.set(self.dadosagendamentos.dados[0].sala)
                    self.turno2c.set(self.dadosagendamentos.dados[0].turno)
                    self.turma2e.set(self.dadosagendamentos.dados[0].turma)
                    self.temposAula2f.set(self.dadosagendamentos.dados[0].tempos)
                    self.data2d.set(self.dadosagendamentos.dados[0].data)
                    self.siapeprofessor2g.set(self.dadosagendamentos.dados[0].professor)
                    self.servidorconf2h.set(self.dadosagendamentos.dados[0].confirmaEntrega)
                    self.servidordev2i.set(self.dadosagendamentos.dados[0].confirmaDevolucao)
                    # MUDA O ESTADO DO BOTÃO DE STATUS
                    if self.dadosagendamentos.dados[0].status == 'Pendente':
                        self.checkcoluna2var.set('Em andamento')
                        self.checkcoluna2.place(x=0, y=0)
                        self.checkcancel2var.set('Cancelar Agendamento')
                        self.checkcancel2.place(x=0, y=25)
                    elif self.dadosagendamentos.dados[0].status == 'Em andamento':
                        self.checkcoluna2var.set('Concluído')
                        self.checkcoluna2.place(x=0, y=0)
                    # RETIRA O PRIMEIRO OBJETO DA FILA
                    self.dadosagendamentos.remover()
                    #COLUNA 3
                    self.laboratorio3a.set(self.dadosagendamentos.dados[0].laboratorio)
                    self.chave3b.set(self.dadosagendamentos.dados[0].sala)
                    self.turno3c.set(self.dadosagendamentos.dados[0].turno)
                    self.turma3e.set(self.dadosagendamentos.dados[0].turma)
                    self.temposAula3f.set(self.dadosagendamentos.dados[0].tempos)
                    self.data3d.set(self.dadosagendamentos.dados[0].data)
                    self.siapeprofessor3g.set(self.dadosagendamentos.dados[0].professor)
                    self.servidorconf3h.set(self.dadosagendamentos.dados[0].confirmaEntrega)
                    self.servidordev3i.set(self.dadosagendamentos.dados[0].confirmaDevolucao)
                    # MUDA O ESTADO DO BOTÃO DE STATUS
                    if self.dadosagendamentos.dados[0].status == 'Pendente':
                        self.checkcoluna3var.set('Em andamento')
                        self.checkcoluna3.place(x=0, y=0)
                        self.checkcancel3var.set('Cancelar Agendamento')
                        self.checkcancel3.place(x=0, y=25)
                    elif self.dadosagendamentos.dados[0].status == 'Em andamento':
                        self.checkcoluna3var.set('Concluído')
                        self.checkcoluna3.place(x=0, y=0)
                    # RETIRA O PRIMEIRO OBJETO DA FILA
                    self.dadosagendamentos.remover()
                elif encontrados==4:
                    # PREENCHE OS LABELS COM AS INFORMAÇOES DO AGENDAMENTO
                    # COLUNA 1
                    self.laboratorio1a.set(self.dadosagendamentos.dados[0].laboratorio)
                    self.chave1b.set(self.dadosagendamentos.dados[0].sala)
                    self.turno1c.set(self.dadosagendamentos.dados[0].turno)
                    self.turma1e.set(self.dadosagendamentos.dados[0].turma)
                    self.temposAula1f.set(self.dadosagendamentos.dados[0].tempos)
                    self.data1d.set(self.dadosagendamentos.dados[0].data)
                    self.siapeprofessor1g.set(self.dadosagendamentos.dados[0].professor)
                    self.servidorconf1h.set(self.dadosagendamentos.dados[0].confirmaEntrega)
                    self.servidordev1i.set(self.dadosagendamentos.dados[0].confirmaDevolucao)
                    # MUDA O ESTADO DO BOTÃO DE STATUS
                    if self.dadosagendamentos.dados[0].status == 'Pendente':
                        self.checkcoluna1var.set('Em andamento')
                        self.checkcoluna1.place(x=0, y=0)
                        self.checkcancel1var.set('Cancelar Agendamento')
                        self.checkcancel1.place(x=0, y=25)
                    elif self.dadosagendamentos.dados[0].status == 'Em andamento':
                        self.checkcoluna1var.set('Concluído')
                        self.checkcoluna1.place(x=0, y=0)
                    # RETIRA O PRIMEIRO OBJETO DA FILA
                    self.dadosagendamentos.remover()
                    #COLUNA 2
                    self.laboratorio2a.set(self.dadosagendamentos.dados[0].laboratorio)
                    self.chave2b.set(self.dadosagendamentos.dados[0].sala)
                    self.turno2c.set(self.dadosagendamentos.dados[0].turno)
                    self.turma2e.set(self.dadosagendamentos.dados[0].turma)
                    self.temposAula2f.set(self.dadosagendamentos.dados[0].tempos)
                    self.data2d.set(self.dadosagendamentos.dados[0].data)
                    self.siapeprofessor2g.set(self.dadosagendamentos.dados[0].professor)
                    self.servidorconf2h.set(self.dadosagendamentos.dados[0].confirmaEntrega)
                    self.servidordev2i.set(self.dadosagendamentos.dados[0].confirmaDevolucao)
                    # MUDA O ESTADO DO BOTÃO DE STATUS
                    if self.dadosagendamentos.dados[0].status == 'Pendente':
                        self.checkcoluna2var.set('Em andamento')
                        self.checkcoluna2.place(x=0, y=0)
                        self.checkcancel2var.set('Cancelar Agendamento')
                        self.checkcancel2.place(x=0, y=25)
                    elif self.dadosagendamentos.dados[0].status == 'Em andamento':
                        self.checkcoluna2var.set('Concluído')
                        self.checkcoluna2.place(x=0, y=0)
                    # RETIRA O PRIMEIRO OBJETO DA FILA
                    self.dadosagendamentos.remover()
                    #COLUNA 3
                    self.laboratorio3a.set(self.dadosagendamentos.dados[0].laboratorio)
                    self.chave3b.set(self.dadosagendamentos.dados[0].sala)
                    self.turno3c.set(self.dadosagendamentos.dados[0].turno)
                    self.turma3e.set(self.dadosagendamentos.dados[0].turma)
                    self.temposAula3f.set(self.dadosagendamentos.dados[0].tempos)
                    self.data3d.set(self.dadosagendamentos.dados[0].data)
                    self.siapeprofessor3g.set(self.dadosagendamentos.dados[0].professor)
                    self.servidorconf3h.set(self.dadosagendamentos.dados[0].confirmaEntrega)
                    self.servidordev3i.set(self.dadosagendamentos.dados[0].confirmaDevolucao)
                    # MUDA O ESTADO DO BOTÃO DE STATUS
                    if self.dadosagendamentos.dados[0].status == 'Pendente':
                        self.checkcoluna3var.set('Em andamento')
                        self.checkcoluna3.place(x=0, y=0)
                        self.checkcancel3var.set('Cancelar Agendamento')
                        self.checkcancel3.place(x=0, y=25)
                    elif self.dadosagendamentos.dados[0].status == 'Em andamento':
                        self.checkcoluna3var.set('Concluído')
                        self.checkcoluna3.place(x=0, y=0)
                    # RETIRA O PRIMEIRO OBJETO DA FILA
                    self.dadosagendamentos.remover()
                    #COLUNA 4
                    self.laboratorio4a.set(self.dadosagendamentos.dados[0].laboratorio)
                    self.chave4b.set(self.dadosagendamentos.dados[0].sala)
                    self.turno4c.set(self.dadosagendamentos.dados[0].turno)
                    self.turma4e.set(self.dadosagendamentos.dados[0].turma)
                    self.temposAula4f.set(self.dadosagendamentos.dados[0].tempos)
                    self.data4d.set(self.dadosagendamentos.dados[0].data)
                    self.siapeprofessor4g.set(self.dadosagendamentos.dados[0].professor)
                    self.servidorconf4h.set(self.dadosagendamentos.dados[0].confirmaEntrega)
                    self.servidordev4i.set(self.dadosagendamentos.dados[0].confirmaDevolucao)
                    # MUDA O ESTADO DO BOTÃO DE STATUS
                    if self.dadosagendamentos.dados[0].status == 'Pendente':
                        self.checkcoluna4var.set('Em andamento')
                        self.checkcoluna4.place(x=0, y=0)
                        self.checkcancel4var.set('Cancelar Agendamento')
                        self.checkcancel4.place(x=0, y=25)
                    elif self.dadosagendamentos.dados[0].status == 'Em andamento':
                        self.checkcoluna4var.set('Concluído')
                        self.checkcoluna4.place(x=0, y=0)
                    # RETIRA O PRIMEIRO OBJETO DA FILA
                    self.dadosagendamentos.remover()
                elif encontrados==5:
                    # PREENCHE OS LABELS COM AS INFORMAÇOES DO AGENDAMENTO
                    # COLUNA 1
                    self.laboratorio1a.set(self.dadosagendamentos.dados[0].laboratorio)
                    self.chave1b.set(self.dadosagendamentos.dados[0].sala)
                    self.turno1c.set(self.dadosagendamentos.dados[0].turno)
                    self.turma1e.set(self.dadosagendamentos.dados[0].turma)
                    self.temposAula1f.set(self.dadosagendamentos.dados[0].tempos)
                    self.data1d.set(self.dadosagendamentos.dados[0].data)
                    self.siapeprofessor1g.set(self.dadosagendamentos.dados[0].professor)
                    self.servidorconf1h.set(self.dadosagendamentos.dados[0].confirmaEntrega)
                    self.servidordev1i.set(self.dadosagendamentos.dados[0].confirmaDevolucao)
                    # MUDA O ESTADO DO BOTÃO DE STATUS
                    if self.dadosagendamentos.dados[0].status == 'Pendente':
                        self.checkcoluna1var.set('Em andamento')
                        self.checkcoluna1.place(x=0, y=0)
                        self.checkcancel1var.set('Cancelar Agendamento')
                        self.checkcancel1.place(x=0, y=25)
                    elif self.dadosagendamentos.dados[0].status == 'Em andamento':
                        self.checkcoluna1var.set('Concluído')
                        self.checkcoluna1.place(x=0, y=0)
                    # RETIRA O PRIMEIRO OBJETO DA FILA
                    self.dadosagendamentos.remover()
                    #COLUNA 2
                    self.laboratorio2a.set(self.dadosagendamentos.dados[0].laboratorio)
                    self.chave2b.set(self.dadosagendamentos.dados[0].sala)
                    self.turno2c.set(self.dadosagendamentos.dados[0].turno)
                    self.turma2e.set(self.dadosagendamentos.dados[0].turma)
                    self.temposAula2f.set(self.dadosagendamentos.dados[0].tempos)
                    self.data2d.set(self.dadosagendamentos.dados[0].data)
                    self.siapeprofessor2g.set(self.dadosagendamentos.dados[0].professor)
                    self.servidorconf2h.set(self.dadosagendamentos.dados[0].confirmaEntrega)
                    self.servidordev2i.set(self.dadosagendamentos.dados[0].confirmaDevolucao)
                    # MUDA O ESTADO DO BOTÃO DE STATUS
                    if self.dadosagendamentos.dados[0].status == 'Pendente':
                        self.checkcoluna2var.set('Em andamento')
                        self.checkcoluna2.place(x=0, y=0)
                        self.checkcancel2var.set('Cancelar Agendamento')
                        self.checkcancel2.place(x=0, y=25)
                    elif self.dadosagendamentos.dados[0].status == 'Em andamento':
                        self.checkcoluna2var.set('Concluído')
                        self.checkcoluna2.place(x=0, y=0)
                    # RETIRA O PRIMEIRO OBJETO DA FILA
                    self.dadosagendamentos.remover()
                    #COLUNA 3
                    self.laboratorio3a.set(self.dadosagendamentos.dados[0].laboratorio)
                    self.chave3b.set(self.dadosagendamentos.dados[0].sala)
                    self.turno3c.set(self.dadosagendamentos.dados[0].turno)
                    self.turma3e.set(self.dadosagendamentos.dados[0].turma)
                    self.temposAula3f.set(self.dadosagendamentos.dados[0].tempos)
                    self.data3d.set(self.dadosagendamentos.dados[0].data)
                    self.siapeprofessor3g.set(self.dadosagendamentos.dados[0].professor)
                    self.servidorconf3h.set(self.dadosagendamentos.dados[0].confirmaEntrega)
                    self.servidordev3i.set(self.dadosagendamentos.dados[0].confirmaDevolucao)
                    # MUDA O ESTADO DO BOTÃO DE STATUS
                    if self.dadosagendamentos.dados[0].status == 'Pendente':
                        self.checkcoluna3var.set('Em andamento')
                        self.checkcoluna3.place(x=0, y=0)
                        self.checkcancel3var.set('Cancelar Agendamento')
                        self.checkcancel3.place(x=0, y=25)
                    elif self.dadosagendamentos.dados[0].status == 'Em andamento':
                        self.checkcoluna3var.set('Concluído')
                        self.checkcoluna3.place(x=0, y=0)
                    # RETIRA O PRIMEIRO OBJETO DA FILA
                    self.dadosagendamentos.remover()
                    #COLUNA 4
                    self.laboratorio4a.set(self.dadosagendamentos.dados[0].laboratorio)
                    self.chave4b.set(self.dadosagendamentos.dados[0].sala)
                    self.turno4c.set(self.dadosagendamentos.dados[0].turno)
                    self.turma4e.set(self.dadosagendamentos.dados[0].turma)
                    self.temposAula4f.set(self.dadosagendamentos.dados[0].tempos)
                    self.data4d.set(self.dadosagendamentos.dados[0].data)
                    self.siapeprofessor4g.set(self.dadosagendamentos.dados[0].professor)
                    self.servidorconf4h.set(self.dadosagendamentos.dados[0].confirmaEntrega)
                    self.servidordev4i.set(self.dadosagendamentos.dados[0].confirmaDevolucao)
                    # MUDA O ESTADO DO BOTÃO DE STATUS
                    if self.dadosagendamentos.dados[0].status == 'Pendente':
                        self.checkcoluna4var.set('Em andamento')
                        self.checkcoluna4.place(x=0, y=0)
                        self.checkcancel4var.set('Cancelar Agendamento')
                        self.checkcancel4.place(x=0, y=25)
                    elif self.dadosagendamentos.dados[0].status == 'Em andamento':
                        self.checkcoluna4var.set('Concluído')
                        self.checkcoluna4.place(x=0, y=0)
                    #RETIRA O PRIMEIRO OBJETO DA FILA
                    self.dadosagendamentos.remover()
                    # COLUNA 5
                    self.laboratorio5a.set(self.dadosagendamentos.dados[0].laboratorio)
                    self.chave5b.set(self.dadosagendamentos.dados[0].sala)
                    self.turno5c.set(self.dadosagendamentos.dados[0].turno)
                    self.turma5e.set(self.dadosagendamentos.dados[0].turma)
                    self.temposAula5f.set(self.dadosagendamentos.dados[0].tempos)
                    self.data5d.set(self.dadosagendamentos.dados[0].data)
                    self.siapeprofessor5g.set(self.dadosagendamentos.dados[0].professor)
                    self.servidorconf5h.set(self.dadosagendamentos.dados[0].confirmaEntrega)
                    self.servidordev5i.set(self.dadosagendamentos.dados[0].confirmaDevolucao)
                    # MUDA O ESTADO DO BOTÃO DE STATUS
                    if self.dadosagendamentos.dados[0].status == 'Pendente':
                        self.checkcoluna5var.set('Em andamento')
                        self.checkcoluna5.place(x=0, y=0)
                        self.checkcancel5var.set('Cancelar Agendamento')
                        self.checkcancel5.place(x=0, y=25)
                    elif self.dadosagendamentos.dados[0].status == 'Em andamento':
                        self.checkcoluna5var.set('Concluído')
                        self.checkcoluna5.place(x=0, y=0)
                    # RETIRA O PRIMEIRO OBJETO DA FILA
                    self.dadosagendamentos.remover()
                elif encontrados==6:
                    # PREENCHE OS LABELS COM AS INFORMAÇOES DO AGENDAMENTO
                    # COLUNA 1
                    self.laboratorio1a.set(self.dadosagendamentos.dados[0].laboratorio)
                    self.chave1b.set(self.dadosagendamentos.dados[0].sala)
                    self.turno1c.set(self.dadosagendamentos.dados[0].turno)
                    self.turma1e.set(self.dadosagendamentos.dados[0].turma)
                    self.temposAula1f.set(self.dadosagendamentos.dados[0].tempos)
                    self.data1d.set(self.dadosagendamentos.dados[0].data)
                    self.siapeprofessor1g.set(self.dadosagendamentos.dados[0].professor)
                    self.servidorconf1h.set(self.dadosagendamentos.dados[0].confirmaEntrega)
                    self.servidordev1i.set(self.dadosagendamentos.dados[0].confirmaDevolucao)
                    # MUDA O ESTADO DO BOTÃO DE STATUS
                    if self.dadosagendamentos.dados[0].status == 'Pendente':
                        self.checkcoluna1var.set('Em andamento')
                        self.checkcoluna1.place(x=0, y=0)
                        self.checkcancel1var.set('Cancelar Agendamento')
                        self.checkcancel1.place(x=0, y=25)
                    elif self.dadosagendamentos.dados[0].status == 'Em andamento':
                        self.checkcoluna1var.set('Concluído')
                        self.checkcoluna1.place(x=0, y=0)
                    # RETIRA O PRIMEIRO OBJETO DA FILA
                    self.dadosagendamentos.remover()
                    #COLUNA 2
                    self.laboratorio2a.set(self.dadosagendamentos.dados[0].laboratorio)
                    self.chave2b.set(self.dadosagendamentos.dados[0].sala)
                    self.turno2c.set(self.dadosagendamentos.dados[0].turno)
                    self.turma2e.set(self.dadosagendamentos.dados[0].turma)
                    self.temposAula2f.set(self.dadosagendamentos.dados[0].tempos)
                    self.data2d.set(self.dadosagendamentos.dados[0].data)
                    self.siapeprofessor2g.set(self.dadosagendamentos.dados[0].professor)
                    self.servidorconf2h.set(self.dadosagendamentos.dados[0].confirmaEntrega)
                    self.servidordev2i.set(self.dadosagendamentos.dados[0].confirmaDevolucao)
                    # MUDA O ESTADO DO BOTÃO DE STATUS
                    if self.dadosagendamentos.dados[0].status == 'Pendente':
                        self.checkcoluna2var.set('Em andamento')
                        self.checkcoluna2.place(x=0, y=0)
                        self.checkcancel2var.set('Cancelar Agendamento')
                        self.checkcancel2.place(x=0, y=25)
                    elif self.dadosagendamentos.dados[0].status == 'Em andamento':
                        self.checkcoluna2var.set('Concluído')
                        self.checkcoluna2.place(x=0, y=0)
                    # RETIRA O PRIMEIRO OBJETO DA FILA
                    self.dadosagendamentos.remover()
                    #COLUNA 3
                    self.laboratorio3a.set(self.dadosagendamentos.dados[0].laboratorio)
                    self.chave3b.set(self.dadosagendamentos.dados[0].sala)
                    self.turno3c.set(self.dadosagendamentos.dados[0].turno)
                    self.turma3e.set(self.dadosagendamentos.dados[0].turma)
                    self.temposAula3f.set(self.dadosagendamentos.dados[0].tempos)
                    self.data3d.set(self.dadosagendamentos.dados[0].data)
                    self.siapeprofessor3g.set(self.dadosagendamentos.dados[0].professor)
                    self.servidorconf3h.set(self.dadosagendamentos.dados[0].confirmaEntrega)
                    self.servidordev3i.set(self.dadosagendamentos.dados[0].confirmaDevolucao)
                    # MUDA O ESTADO DO BOTÃO DE STATUS
                    if self.dadosagendamentos.dados[0].status == 'Pendente':
                        self.checkcoluna3var.set('Em andamento')
                        self.checkcoluna3.place(x=0, y=0)
                        self.checkcancel3var.set('Cancelar Agendamento')
                        self.checkcancel3.place(x=0, y=25)
                    elif self.dadosagendamentos.dados[0].status == 'Em andamento':
                        self.checkcoluna3var.set('Concluído')
                        self.checkcoluna3.place(x=0, y=0)
                    # RETIRA O PRIMEIRO OBJETO DA FILA
                    self.dadosagendamentos.remover()
                    #COLUNA 4
                    self.laboratorio4a.set(self.dadosagendamentos.dados[0].laboratorio)
                    self.chave4b.set(self.dadosagendamentos.dados[0].sala)
                    self.turno4c.set(self.dadosagendamentos.dados[0].turno)
                    self.turma4e.set(self.dadosagendamentos.dados[0].turma)
                    self.temposAula4f.set(self.dadosagendamentos.dados[0].tempos)
                    self.data4d.set(self.dadosagendamentos.dados[0].data)
                    self.siapeprofessor4g.set(self.dadosagendamentos.dados[0].professor)
                    self.servidorconf4h.set(self.dadosagendamentos.dados[0].confirmaEntrega)
                    self.servidordev4i.set(self.dadosagendamentos.dados[0].confirmaDevolucao)
                    # MUDA O ESTADO DO BOTÃO DE STATUS
                    if self.dadosagendamentos.dados[0].status == 'Pendente':
                        self.checkcoluna4var.set('Em andamento')
                        self.checkcoluna4.place(x=0, y=0)
                        self.checkcancel4var.set('Cancelar Agendamento')
                        self.checkcancel4.place(x=0, y=25)
                    elif self.dadosagendamentos.dados[0].status == 'Em andamento':
                        self.checkcoluna4var.set('Concluído')
                        self.checkcoluna4.place(x=0, y=0)
                    # RETIRA O PRIMEIRO OBJETO DA FILA
                    self.dadosagendamentos.remover()
                    # COLUNA 5
                    self.laboratorio5a.set(self.dadosagendamentos.dados[0].laboratorio)
                    self.chave5b.set(self.dadosagendamentos.dados[0].sala)
                    self.turno5c.set(self.dadosagendamentos.dados[0].turno)
                    self.turma5e.set(self.dadosagendamentos.dados[0].turma)
                    self.temposAula5f.set(self.dadosagendamentos.dados[0].tempos)
                    self.data5d.set(self.dadosagendamentos.dados[0].data)
                    self.siapeprofessor5g.set(self.dadosagendamentos.dados[0].professor)
                    self.servidorconf5h.set(self.dadosagendamentos.dados[0].confirmaEntrega)
                    self.servidordev5i.set(self.dadosagendamentos.dados[0].confirmaDevolucao)
                    # MUDA O ESTADO DO BOTÃO DE STATUS
                    if self.dadosagendamentos.dados[0].status == 'Pendente':
                        self.checkcoluna5var.set('Em andamento')
                        self.checkcoluna5.place(x=0, y=0)
                        self.checkcancel5var.set('Cancelar Agendamento')
                        self.checkcancel5.place(x=0, y=25)
                    elif self.dadosagendamentos.dados[0].status == 'Em andamento':
                        self.checkcoluna5var.set('Concluído')
                        self.checkcoluna5.place(x=0, y=0)
                    # RETIRA O PRIMEIRO OBJETO DA FILA
                    self.dadosagendamentos.remover()
                    #COLUNA 6
                    self.laboratorio6a.set(self.dadosagendamentos.dados[0].laboratorio)
                    self.chave6b.set(self.dadosagendamentos.dados[0].sala)
                    self.turno6c.set(self.dadosagendamentos.dados[0].turno)
                    self.turma6e.set(self.dadosagendamentos.dados[0].turma)
                    self.temposAula6f.set(self.dadosagendamentos.dados[0].tempos)
                    self.data6d.set(self.dadosagendamentos.dados[0].data)
                    self.siapeprofessor6g.set(self.dadosagendamentos.dados[0].professor)
                    self.servidorconf6h.set(self.dadosagendamentos.dados[0].confirmaEntrega)
                    self.servidordev6i.set(self.dadosagendamentos.dados[0].confirmaDevolucao)
                    # MUDA O ESTADO DO BOTÃO DE STATUS
                    if self.dadosagendamentos.dados[0].status == 'Pendente':
                        self.checkcoluna6var.set('Em andamento')
                        self.checkcoluna6.place(x=0, y=0)
                        self.checkcancel6var.set('Cancelar Agendamento')
                        self.checkcancel6.place(x=0, y=25)
                    elif self.dadosagendamentos.dados[0].status == 'Em andamento':
                        self.checkcoluna6var.set('Concluído')
                        self.checkcoluna6.place(x=0, y=0)
                    # RETIRA O PRIMEIRO OBJETO DA FILA
                    self.dadosagendamentos.remover()


            else:
                messagebox.showwarning('ATENÇÃO','PREENCHA OS CAMPOS CORRETAMENTE ')





        self.telaEntrega = Tk()
        screen_width = 1024
        screen_height = 768
        vcmd = self.telaEntrega.register(func=limitarEntry)
        self.telaEntrega.title('Labifro')
        self.telaEntrega.geometry('{}x{}+0+0'.format(screen_width, screen_height))
        self.telaEntrega.iconbitmap('icons_images/iconewindow.ico')
        self.telaEntrega['bg'] = '#5F9EA0'
        self.frametop = Frame(self.telaEntrega, height=100, width=screen_width - 80, bg='#708090')
        self.frametop.pack()
        self.imgback = PhotoImage(file='icons_images/back.png')
        self.back = Button(self.frametop, image=self.imgback, height=30, width=30,relief = FLAT,activebackground= '#00FF7F')
        self.back.place(x=10, y=50)
        self.back['command'] = back
        self.back['bg']='#5F9EA0'
        self.back['cursor'] = 'exchange'
        self.framemid = Frame(self.telaEntrega, width=screen_width - 80, height=screen_height / 2 + 500,bg='#5F9EA0')
        self.framemid.pack()
##################################################################################################################
########### VARIAVEIS EM (STRINGVAR) PARA PREECHIMENTO DOS (LABEL(S)) ##################################
##################################################################################################################
        # VARIAVEIS DA PRIMEIRA COLUNA LABORATORIOS
        self.laboratorio1a = StringVar()
        self.laboratorio2a = StringVar()
        self.laboratorio3a = StringVar()
        self.laboratorio4a = StringVar()
        self.laboratorio5a = StringVar()
        self.laboratorio6a = StringVar()
        # VARIAVEIS DA SEGUNDA COLUNA CHAVES
        self.chave1b = StringVar()
        self.chave2b = StringVar()
        self.chave3b = StringVar()
        self.chave4b = StringVar()
        self.chave5b = StringVar()
        self.chave6b = StringVar()
        # VARIAVEIS DA TERCEIRA COLUNA TURNO
        self.turno1c = StringVar()
        self.turno2c = StringVar()
        self.turno3c = StringVar()
        self.turno4c = StringVar()
        self.turno5c = StringVar()
        self.turno6c = StringVar()
        # VARIAVEIS DA QUARTA COLUNA DATA
        self.data1d = StringVar()
        self.data2d = StringVar()
        self.data3d = StringVar()
        self.data4d = StringVar()
        self.data5d = StringVar()
        self.data6d = StringVar()
        # VARIAVEIS DA QUINTA COLUNA TURMA
        self.turma1e = StringVar()
        self.turma2e = StringVar()
        self.turma3e = StringVar()
        self.turma4e = StringVar()
        self.turma5e = StringVar()
        self.turma6e = StringVar()
        # VARIAVEIS DA SEXTA COLUNA TEMPOS DE AULA
        self.temposAula1f = StringVar()
        self.temposAula2f = StringVar()
        self.temposAula3f = StringVar()
        self.temposAula4f = StringVar()
        self.temposAula5f = StringVar()
        self.temposAula6f = StringVar()
        # VARIAVEIS DA SÉTIMA COLUNA SIAPES DOS PROFESSORES
        self.siapeprofessor1g = StringVar()
        self.siapeprofessor2g = StringVar()
        self.siapeprofessor3g = StringVar()
        self.siapeprofessor4g = StringVar()
        self.siapeprofessor5g = StringVar()
        self.siapeprofessor6g = StringVar()
        # VARIAVEIS DA OITAVA COLUNA SIAPES DO SERVIDOR CONF.RET

        self.servidorconf1h = StringVar()
        self.servidorconf2h = StringVar()
        self.servidorconf3h = StringVar()
        self.servidorconf4h = StringVar()
        self.servidorconf5h = StringVar()
        self.servidorconf6h = StringVar()

        # VARIAVES DA NONA COLUNA SIAPES DO SERVIDOR CONF.DEV
        self.servidordev1i = StringVar()
        self.servidordev2i = StringVar()
        self.servidordev3i = StringVar()
        self.servidordev4i = StringVar()
        self.servidordev5i = StringVar()
        self.servidordev6i = StringVar()




        #STRINGVAR PESQUISA
        self.entradapesquisavar = StringVar()
        self.entradapesquisavar.set('Digite Siape...')

        # FILA QUE ARMAZENA OS AGENDAMENTOS ENCONTRADOS
        self.dadosagendamentos = Fila()

########### (LABEL(S))PARA CADA TUPLA NAS COLUNAS DE AGENDAMENTO ############################
##################################################################################################
        # LABEL DA COLUNA DE ATRIBUTOS
        self.labellaboratorio = Label(self.framemid,text = 'Laboratório',font = ('vendana',12),width =9)
        self.labellaboratorio.place(x=2,y=self.telaEntrega['height']/4+40)
        self.labelChave = Label(self.framemid,text="Chave",width=9,font=('vendana',12))
        self.labelChave.place(x=2,y=self.telaEntrega['height']/4+65)
        self.labelTurno = Label(self.framemid,text="Turno",width=9,font=('vendana',12))
        self.labelTurno.place(x=2,y=self.telaEntrega['height']/4+90)
        self.labelData = Label(self.framemid,text="Data",width=9,font=('vendana',12))
        self.labelData.place(x=2,y=self.telaEntrega['height']/4+115)
        self.labelTurma = Label(self.framemid,text="Turma",width=9,font=('vendana',12))
        self.labelTurma.place(x=2,y=self.telaEntrega['height']/4+140)
        self.labelTempos = Label(self.framemid,text="Tempos",width=9,font=('vendana',12))
        self.labelTempos.place(x=2,y=self.telaEntrega['height']/4+165)
        self.labelProfessor = Label(self.framemid,text="Professor",width=9,font=('vendana',12))
        self.labelProfessor.place(x=2,y=self.telaEntrega['height']/4+190)
        self.labelConfret = Label(self.framemid,text="CONF.RET",width=9,font=('vendana',12))
        self.labelConfret.place(x=2,y=self.telaEntrega['height']/4+215)
        self.labelConfdev = Label(self.framemid,text="CONF.DEV",width=9,font=('vendana',12))
        self.labelConfdev.place(x=2,y=self.telaEntrega['height']/4+240)
        self.labelStatus = Label(self.framemid,text='Status',width=9,font=('vendana',12),height=3)
        self.labelStatus.place(x=2,y=self.telaEntrega['height']/4+265)

        # LABEL DA PRIMEIRA COLUNA LABORATÓRIO
        self.labelLaboratorio1a=Label(self.framemid,textvariable=self.laboratorio1a,width=15,font=('vendana',12))
        self.labelLaboratorio1a.place(x=91,y=self.telaEntrega['height']/4+40)
        self.labelLaboratorio2a=Label(self.framemid,textvariable=self.laboratorio2a,width=15,font=('vendana',12))
        self.labelLaboratorio2a.place(x=233,y=self.telaEntrega['height']/4+40)
        self.labelLaboratorio3a=Label(self.framemid,textvariable=self.laboratorio3a,width=15,font=('vendana',12))
        self.labelLaboratorio3a.place(x=375,y=self.telaEntrega['height']/4+40)
        self.labelLaboratorio4a=Label(self.framemid,textvariable=self.laboratorio4a,width=15,font=('vendana',12))
        self.labelLaboratorio4a.place(x=517,y=self.telaEntrega['height']/4+40)
        self.labelLaboratorio5a=Label(self.framemid,textvariable=self.laboratorio5a,width=15,font=('vendana',12))
        self.labelLaboratorio5a.place(x=659,y=self.telaEntrega['height']/4+40)
        self.labelLaboratorio6a=Label(self.framemid,textvariable=self.laboratorio6a,width=15,font=('vendana',12))
        self.labelLaboratorio6a.place(x=801,y=self.telaEntrega['height']/4+40)
        #LABEL DA SEGUNDA COLUNA CHAVE
        self.labelChave1b=Label(self.framemid,textvariable=self.chave1b,width=15,font=('vendana',12))
        self.labelChave1b.place(x=91,y=self.telaEntrega['height']/4+65)
        self.labelChave2b=Label(self.framemid,textvariable=self.chave2b,width=15,font=('vendana',12))
        self.labelChave2b.place(x=233,y=self.telaEntrega['height']/4+65)
        self.labelChave3b=Label(self.framemid,textvariable=self.chave3b,width=15,font=('vendana',12))
        self.labelChave3b.place(x=375,y=self.telaEntrega['height']/4+65)
        self.labelChave4b=Label(self.framemid,textvariable=self.chave4b,width=15,font=('vendana',12))
        self.labelChave4b.place(x=517,y=self.telaEntrega['height']/4+65)
        self.labelChave5b=Label(self.framemid,textvariable=self.chave5b,width=15,font=('vendana',12))
        self.labelChave5b.place(x=659,y=self.telaEntrega['height']/4+65)
        self.labelChave6b=Label(self.framemid,textvariable=self.chave6b,width=15,font=('vendana',12))
        self.labelChave6b.place(x=801,y=self.telaEntrega['height']/4+65)
        #LABEL DA TERCEIRA COLUNA TURNO
        self.labelTurno1c=Label(self.framemid,textvariable=self.turno1c,width=15,font=('vendana',12))
        self.labelTurno1c.place(x=91,y=self.telaEntrega['height']/4+90)
        self.labelTurno2c=Label(self.framemid,textvariable=self.turno2c,width=15,font=('vendana',12))
        self.labelTurno2c.place(x=233,y=self.telaEntrega['height']/4+90)
        self.labelTurno3c=Label(self.framemid,textvariable=self.turno3c,width=15,font=('vendana',12))
        self.labelTurno3c.place(x=375,y=self.telaEntrega['height']/4+90)
        self.labelTurno4c=Label(self.framemid,textvariable=self.turno4c,width=15,font=('vendana',12))
        self.labelTurno4c.place(x=517,y=self.telaEntrega['height']/4+90)
        self.labelTurno5c=Label(self.framemid,textvariable=self.turno5c,width=15,font=('vendana',12))
        self.labelTurno5c.place(x=659,y=self.telaEntrega['height']/4+90)
        self.labelTurno6c=Label(self.framemid,textvariable=self.turno6c,width=15,font=('vendana',12))
        self.labelTurno6c.place(x=801,y=self.telaEntrega['height']/4+90)
        #LABEL DA QUARTA COLUNA DATA
        self.labelData1d=Label(self.framemid,textvariable=self.data1d,width=15,font=('vendana',12))
        self.labelData1d.place(x=91,y=self.telaEntrega['height']/4+115)
        self.labelData2d=Label(self.framemid,textvariable=self.data2d,width=15,font=('vendana',12))
        self.labelData2d.place(x=233,y=self.telaEntrega['height']/4+115)
        self.labelData3d=Label(self.framemid,textvariable=self.data3d,width=15,font=('vendana',12))
        self.labelData3d.place(x=375,y=self.telaEntrega['height']/4+115)
        self.labelData4d=Label(self.framemid,textvariable=self.data4d,width=15,font=('vendana',12))
        self.labelData4d.place(x=517,y=self.telaEntrega['height']/4+115)
        self.labelData5d=Label(self.framemid,textvariable=self.data5d,width=15,font=('vendana',12))
        self.labelData5d.place(x=659,y=self.telaEntrega['height']/4+115)
        self.labelData6d=Label(self.framemid,textvariable=self.data6d,width=15,font=('vendana',12))
        self.labelData6d.place(x=801,y=self.telaEntrega['height']/4+115)
        #LABEL DA QUINTA COLUNA TURMA
        self.labelTurma1e=Label(self.framemid,textvariable=self.turma1e,width=15,font=('vendana',12))
        self.labelTurma1e.place(x=91,y=self.telaEntrega['height']/4+140)
        self.labelTurma2e=Label(self.framemid,textvariable=self.turma2e,width=15,font=('vendana',12))
        self.labelTurma2e.place(x=233,y=self.telaEntrega['height']/4+140)
        self.labelTurma3e=Label(self.framemid,textvariable=self.turma3e,width=15,font=('vendana',12))
        self.labelTurma3e.place(x=375,y=self.telaEntrega['height']/4+140)
        self.labelTurma4e=Label(self.framemid,textvariable=self.turma4e,width=15,font=('vendana',12))
        self.labelTurma4e.place(x=517,y=self.telaEntrega['height']/4+140)
        self.labelTurma5e=Label(self.framemid,textvariable=self.turma5e,width=15,font=('vendana',12))
        self.labelTurma5e.place(x=659,y=self.telaEntrega['height']/4+140)
        self.labelTurma6e=Label(self.framemid,textvariable=self.turma6e,width=15,font=('vendana',12))
        self.labelTurma6e.place(x=801,y=self.telaEntrega['height']/4+140)
        #LABEL DA SEXTA COLUNA TEMPOS
        self.labelTemposAula1f=Label(self.framemid,textvariable=self.temposAula1f,width=15,font=('vendana',12))
        self.labelTemposAula1f.place(x=91,y=self.telaEntrega['height']/4+165)
        self.labelTemposAula2f=Label(self.framemid,textvariable=self.temposAula2f,width=15,font=('vendana',12))
        self.labelTemposAula2f.place(x=233,y=self.telaEntrega['height']/4+165)
        self.labelTemposAula3f=Label(self.framemid,textvariable=self.temposAula3f,width=15,font=('vendana',12))
        self.labelTemposAula3f.place(x=375,y=self.telaEntrega['height']/4+165)
        self.labelTemposAula4f=Label(self.framemid,textvariable=self.temposAula4f,width=15,font=('vendana',12))
        self.labelTemposAula4f.place(x=517,y=self.telaEntrega['height']/4+165)
        self.labelTemposAula5f=Label(self.framemid,textvariable=self.temposAula5f,width=15,font=('vendana',12))
        self.labelTemposAula5f.place(x=659,y=self.telaEntrega['height']/4+165)
        self.labelTemposAula6f=Label(self.framemid,textvariable=self.temposAula6f,width=15,font=('vendana',12))
        self.labelTemposAula6f.place(x=801,y=self.telaEntrega['height']/4+165)
        #LABEL DA SETIMA COLUNA PROFESSOR
        self.labelProfessor1g=Label(self.framemid,textvariable=self.siapeprofessor1g,width=15,font=('vendana',12))
        self.labelProfessor1g.place(x=91,y=self.telaEntrega['height']/4+190)
        self.labelProfessor2g=Label(self.framemid,textvariable=self.siapeprofessor2g,width=15,font=('vendana',12))
        self.labelProfessor2g.place(x=233,y=self.telaEntrega['height']/4+190)
        self.labelProfessor3g=Label(self.framemid,textvariable=self.siapeprofessor3g,width=15,font=('vendana',12))
        self.labelProfessor3g.place(x=375,y=self.telaEntrega['height']/4+190)
        self.labelProfessor4g=Label(self.framemid,textvariable=self.siapeprofessor4g,width=15,font=('vendana',12))
        self.labelProfessor4g.place(x=517,y=self.telaEntrega['height']/4+190)
        self.labelProfessor5g=Label(self.framemid,textvariable=self.siapeprofessor5g,width=15,font=('vendana',12))
        self.labelProfessor5g.place(x=659,y=self.telaEntrega['height']/4+190)
        self.labelProfessor6g=Label(self.framemid,textvariable=self.siapeprofessor6g,width=15,font=('vendana',12))
        self.labelProfessor6g.place(x=801,y=self.telaEntrega['height']/4+190)
        #LABEL DA OITAVA COLUNA CONFRET
        self.labelConfret1h=Label(self.framemid,width=15,font=('vendana',12),textvariable=self.servidorconf1h)
        self.labelConfret1h.place(x=91,y=self.telaEntrega['height']/4+215)
        self.labelConfret2h=Label(self.framemid,width=15,font=('vendana',12),textvariable=self.servidorconf2h)
        self.labelConfret2h.place(x=233,y=self.telaEntrega['height']/4+215)
        self.labelConfret3h=Label(self.framemid,width=15,font=('vendana',12),textvariable=self.servidorconf3h)
        self.labelConfret3h.place(x=375,y=self.telaEntrega['height']/4+215)
        self.labelConfret4h=Label(self.framemid,width=15,font=('vendana',12),textvariable=self.servidorconf4h)
        self.labelConfret4h.place(x=517,y=self.telaEntrega['height']/4+215)
        self.labelConfret5h=Label(self.framemid,width=15,font=('vendana',12),textvariable=self.servidorconf5h)
        self.labelConfret5h.place(x=659,y=self.telaEntrega['height']/4+215)
        self.labelConfret6h=Label(self.framemid,width=15,font=('vendana',12),textvariable=self.servidorconf6h)
        self.labelConfret6h.place(x=801,y=self.telaEntrega['height']/4+215)
        # LABEL DA NONA COLUNA CONFDEV
        self.labelConfdev1i=Label(self.framemid,textvariable=self.servidordev1i,width=15,font=('vendana',12))
        self.labelConfdev1i.place(x=91,y=self.telaEntrega['height']/4+240)
        self.labelConfdev2i=Label(self.framemid,textvariable=self.servidordev2i,width=15,font=('vendana',12))
        self.labelConfdev2i.place(x=233,y=self.telaEntrega['height']/4+240)
        self.labelConfdev3i=Label(self.framemid,textvariable=self.servidordev3i,width=15,font=('vendana',12))
        self.labelConfdev3i.place(x=375,y=self.telaEntrega['height']/4+240)
        self.labelConfdev4i=Label(self.framemid,textvariable=self.servidordev4i,width=15,font=('vendana',12))
        self.labelConfdev4i.place(x=517,y=self.telaEntrega['height']/4+240)
        self.labelConfdev5i=Label(self.framemid,textvariable=self.servidordev5i,width=15,font=('vendana',12))
        self.labelConfdev5i.place(x=659,y=self.telaEntrega['height']/4+240)
        self.labelConfdev6i=Label(self.framemid,textvariable=self.servidordev6i,width=15,font=('vendana',12))
        self.labelConfdev6i.place(x=801,y=self.telaEntrega['height']/4+240)
        # LABEL DA DÉCIMA COLUNA STATUS
        self.labelStatus1j = Label(self.framemid, width=15,height=3, font=('vendana', 12))
        self.labelStatus1j.place(x=91, y=self.telaEntrega['height'] / 4 + 265)
        self.labelStatus2j = Label(self.framemid, width=15, font=('vendana', 12),height=3)
        self.labelStatus2j.place(x=233, y=self.telaEntrega['height'] / 4 + 265)
        self.labelStatus3j = Label(self.framemid, width=15, font=('vendana', 12),height=3)
        self.labelStatus3j.place(x=375, y=self.telaEntrega['height'] / 4 + 265)
        self.labelStatus4j = Label(self.framemid, width=15, font=('vendana', 12),height=3)
        self.labelStatus4j.place(x=517, y=self.telaEntrega['height'] / 4 + 265)
        self.labelStatus5j = Label(self.framemid, width=15, font=('vendana', 12),height=3)
        self.labelStatus5j.place(x=659, y=self.telaEntrega['height'] / 4 + 265)
        self.labelStatus6j = Label(self.framemid, width=15, font=('vendana', 12),height=3)
        self.labelStatus6j.place(x=801, y=self.telaEntrega['height'] / 4 + 265)
##############LABEL INFORMATIVO SOBRE ATRIBUTOS DA TABELA##################
        self.explicadevret=Label(self.framemid,bg='#5F9EA0',font=('vendana',8),text='**(CONF.RET)Campo que mostra SIAPE do servidor que confirmou retirada da chave.\n**(CONF.DEV)Campo que mostra SIAPE do servidor que confirmou devolução da chave.').place(x=507, y=self.telaEntrega['height'] / 4 + 340)

        #StringVars checks Culunas
        #COLUNA 1
        self.checkcoluna1var = StringVar()
        self.checkcancel1var = StringVar()
        #COLUNA 2
        self.checkcoluna2var = StringVar()
        self.checkcancel2var = StringVar()
        #COLUNA 3
        self.checkcoluna3var = StringVar()
        self.checkcancel3var = StringVar()
        #COLUNA 4
        self.checkcoluna4var = StringVar()
        self.checkcancel4var = StringVar()
        #COLUNA 5
        self.checkcoluna5var = StringVar()
        self.checkcancel5var = StringVar()
        #COLUNA 6
        self.checkcoluna6var = StringVar()
        self.checkcancel6var = StringVar()

        #BOTOES/COLUNAS PARA CANCELAR OU MUDAR STATUS DE ANDAMENTO DO AGENGAMENTO
        #COLUNA 1
        self.checkcoluna1 = Button(self.labelStatus1j,textvariable=self.checkcoluna1var,width = 18)
        self.checkcoluna1['command'] = partial(mudaStatus, 'checkcoluna1')
        self.checkcancel1 = Button(self.labelStatus1j,textvariable=self.checkcancel1var,width =18)
        self.checkcancel1['command'] = partial(mudaStatus, 'cancelacoluna1')
        #COLUNA 2
        self.checkcoluna2 = Button(self.labelStatus2j,textvariable=self.checkcoluna2var,width = 18)
        self.checkcoluna2['command'] = partial(mudaStatus, 'checkcoluna2')
        self.checkcancel2 = Button(self.labelStatus2j,textvariable=self.checkcancel2var,width =18)
        self.checkcancel2['command'] = partial(mudaStatus, 'cancelacoluna2')
        #COLUNA 3
        self.checkcoluna3 = Button(self.labelStatus3j,textvariable=self.checkcoluna3var,width = 18)
        self.checkcoluna3['command'] = partial(mudaStatus, 'checkcoluna3')
        self.checkcancel3 = Button(self.labelStatus3j,textvariable=self.checkcancel3var,width =18)
        self.checkcancel3['command'] = partial(mudaStatus, 'cancelacoluna3')
        #COLUNA 4
        self.checkcoluna4 = Button(self.labelStatus4j,textvariable=self.checkcoluna4var,width = 18)
        self.checkcoluna4['command'] = partial(mudaStatus, 'checkcoluna4')
        self.checkcancel4 = Button(self.labelStatus4j,textvariable=self.checkcancel4var,width =18)
        self.checkcancel4['command'] = partial(mudaStatus, 'cancelacoluna4')
        #COLUNA 5
        self.checkcoluna5 = Button(self.labelStatus5j,textvariable=self.checkcoluna5var,width = 18)
        self.checkcoluna5['command'] = partial(mudaStatus, 'checkcoluna5')
        self.checkcancel5 = Button(self.labelStatus5j,textvariable=self.checkcancel5var,width =18)
        self.checkcancel5['command'] = partial(mudaStatus, 'cancelacoluna5')
        #COLUNA 6
        self.checkcoluna6 = Button(self.labelStatus6j,textvariable=self.checkcoluna6var,width = 18)
        self.checkcoluna6['command'] = partial(mudaStatus, 'checkcoluna6')
        self.checkcancel6 = Button(self.labelStatus6j,textvariable=self.checkcancel6var,width =18)
        self.checkcancel6['command'] = partial(mudaStatus, 'cancelacoluna6')




        
        

        self.photo = PhotoImage(file='icons_images/iconecad.png')
        self.photo = self.photo.subsample(1, 1)
        self.labelimg = Label(self.frametop, image=self.photo)
        self.labelimg['bg'] = '#708090'
        self.labelimg.place(x=self.frametop['width'] / 2 - 300, y=15)

        self.labelcad = Label(self.frametop, text=' Controle de Chave', font=('Times', 30))
        self.labelcad['bg'] = '#708090'
        self.labelcad.place(x=screen_width / 2 - 250, y=25)

########COMBOBOXES LABORATORIO, CHAVE E TURNO################
        self.tipolab = ttk.Combobox(self.framemid,state='readonly')
        self.tipolab['values'] = ('Informática', 'Química', 'Física', 'Edificações', 'Biologia', 'Eletrotécnica')
        self.tipolab.bind('<<ComboboxSelected>>',autoPreenchimento)
        self.tipolab.place(x=0, y=self.frametop['height']/4-10)
        self.chavecombo = ttk.Combobox(self.framemid,state ='readonly',width = 7)
        self.chavecombo.place(x=145, y=self.frametop['height']/4-10)
        self.turnocombo = ttk.Combobox(self.framemid,state = 'readonly',width = 12)
        self.turnocombo.place(x=215,y=self.frametop['height']/4-10)
        self.data = ttk.Combobox(self.framemid,state = 'readonly')
        self.data.bind('<Button-1>',carregarData)
        self.data.place(x=315,y=self.frametop['height']/4-10)
        

        ################PESQUISA WIDGETS########################
        self.entradapesquisa = Entry(self.framemid,textvariable = self.entradapesquisavar, relief=FLAT, validate='key' ,validatecommand=(vcmd,'%P'))
        self.entradapesquisa.place(x=465,y=self.frametop['height']/4-9)
        if desativa == 1:
            self.entradapesquisa.bind('<Button-1>',apagar)
        self.imgbtlupa = PhotoImage(file='icons_images/lup.png')
        self.btlupa = Button(self.framemid, image=self.imgbtlupa, height=15, width=15, relief=GROOVE,command = validarPesquisa).place(x=595,y=self.frametop['height']/4-10)
        if desativa==0:
            self.back['command']= logout
            self.entradapesquisavar.set(siape)
            self.entradapesquisa['state'] = DISABLED
        self.telaEntrega.mainloop()
