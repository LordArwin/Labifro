from tkinter import messagebox


class Agendamento():
    def __init__(self,lab,sala,turno,data,tempos,turma,prof,status = 'Pendente',confiret = '-',confidev ='-'):
        '''Classe de Agendamentos responsavel por registrar, modificar e ordenar agendamentos na base de dados'''
        self.__data = data
        self.__turno = turno
        self.__tempos = tempos
        self.__sala = sala
        self.__laboratorio = lab
        self.__turma = turma
        self.__professor = prof
        self.__status = status
        self.__confirmaEntrega = confiret
        self.__confirmaDevolucao = confidev

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, valor):
        self.__status = valor

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, valor):
        self.__data = valor

    @property
    def turno(self):
        return self.__turno

    @turno.setter
    def turno(self, valor):
        self.__turno = valor

    @property
    def tempos(self):
        return self.__tempos

    @tempos.setter
    def tempos(self, valor):
        self.__tempos = valor

    @property
    def sala(self):
        return self.__sala

    @sala.setter
    def sala(self, valor):
        self.__sala = valor

    @property
    def laboratorio(self):
        return self.__laboratorio

    @laboratorio.setter
    def laboratorio(self, valor):
        self.__laboratorio = valor

    @property
    def turma(self):
        return self.__turma

    @turma.setter
    def turma(self, valor):
        self.__turma = valor


    @property
    def professor(self):
        return self.__professor

    @professor.setter
    def professor(self, valor):
        self.__professor = valor

    @property
    def iddata(self):
        return self.__iddata

    @iddata.setter
    def iddata(self, valor):
        self.__iddata = valor

    @property
    def confirmaEntrega(self):
        return self.__confirmaEntrega

    @confirmaEntrega.setter
    def confirmaEntrega(self, valor):
        self.__confirmaEntrega = valor

    @property
    def confirmaDevolucao(self):
        return self.__confirmaDevolucao

    @confirmaDevolucao.setter
    def confirmaDevolucao(self, valor):
        self.__confirmaDevolucao = valor

    def insertion_sort(self,vetor, tipo):
        '''Metodo de ordenação insertion sort que ordena os agendamentos por data'''
        if tipo == 'mes':
            atual = 1
            while atual < len(vetor):
                numatual = int(vetor[atual][3][3:5]) + int(vetor[atual][3][6:10])

                tempatual = vetor[atual]
                troca = False
                anterior = atual - 1
                while anterior >= 0 and int(vetor[anterior][3][3:5]) + int(vetor[anterior][3][6:10]) > numatual:
                    vetor[anterior + 1] = vetor[anterior]
                    anterior -= 1
                    troca = True
                if troca == True:
                    vetor[anterior + 1] = tempatual
                atual += 1
        elif tipo == 'dia':
            atual = 1
            while atual < len(vetor):
                numatual = int(vetor[atual][3][3:5]) + int(vetor[atual][3][0:2])

                tempatual = vetor[atual]
                troca = False
                anterior = atual - 1
                while anterior >= 0 and int(vetor[anterior][3][3:5]) + int(vetor[anterior][3][0:2]) > numatual:
                    vetor[anterior + 1] = vetor[anterior]
                    anterior -= 1
                    troca = True
                if troca == True:
                    vetor[anterior + 1] = tempatual
                atual += 1




    def cadastrarAgendamento(self):
        '''Metodo que abre a base de dados e cadastra um agendamento'''
        agenda = open("DadosAgendamento.txt", 'a')
        tempcad =self.laboratorio + ','+self.sala+"," + self.turno + "," + self.data + ',' + self.tempos + ',' + self.turma + ',' + self.professor+','+self.status+','+self.confirmaEntrega+','+self.confirmaDevolucao
        agenda.write(tempcad + '\n')
        agenda.close()
        lista = []
        linhas = open("DadosAgendamento.txt", 'r').read().splitlines()
        for linha in linhas:
            lista.append(linha.split(','))

        """chama metodo insertion_sort e ordena por dia"""
        self.insertion_sort(lista, 'dia')
        '''chama metodo insertion_sort e ordena por mês'''
        self.insertion_sort(lista, 'mes')
        linhas = open("DadosAgendamento.txt", 'w')
        try:
            '''Cadastra os dados ordenados na base de dados'''
            for linha in range(len(lista)):
                new = lista[linha][0] + ',' + lista[linha][1] + ',' + lista[linha][2] + ',' + lista[linha][3] + ',' + \
                      lista[linha][4] + ',' + lista[linha][5] + ',' + lista[linha][6] + ',' + lista[linha][7] + ',' + \
                      lista[linha][8] + ',' + lista[linha][9]
                linhas.write(new + '\n')
        except:
            pass

        messagebox.showinfo('AVISO', 'AGENDAMENTO REALIZADO COM SUCESSO')
    def verificarAgendamento(self,lab,chave,data,siape,turno):
        '''verifica se um agendamento existe'''
        return self.laboratorio == lab and self.sala == chave and self.data == data and self.professor == siape and self.turno == turno and self.status !='Concluído'

    def controleChave(self):
        '''altera o Status do agendamento de acordo com o controle de chaves'''
        linhas = open("DadosAgendamento.txt", 'r').read().splitlines()

        for x in range(len(linhas)):

            if self.laboratorio in linhas[x] and self.sala in linhas[x] and self.data in linhas[x] and self.professor in linhas[x] and self.turno in linhas[x] and self.turma in linhas[x] and self.tempos in linhas[x] and self.status not in linhas[x]:

                novo = open("DadosAgendamento.txt", 'w')
                linhas[x] = self.laboratorio + ','+self.sala+"," + self.turno + "," + self.data + ',' + self.tempos + ',' + self.turma + ',' + self.professor+','+self.status+','+self.confirmaEntrega+','+self.confirmaDevolucao
                novo.write('\n'.join(linhas))
