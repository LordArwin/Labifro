from Usuario import Usuario
from Laboratorio import Laboratorio
from Agendamento import Agendamento
class Fila():
    def __init__(self):
        self.__dados =[]

    @property
    def dados(self):
        return self.__dados

    @dados.setter
    def dados(self, valor):
        self.__dados = valor

    def filaUsuarios(self):
        linhas = open("DadosUsuarios.txt", 'r').read().splitlines()
        for linha in linhas:
            linha = linha.split(',')
            u = Usuario(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5],linha[6])

            self.dados.append(u)
    def filaLaboratorios(self):
        linhas = open("DadosLaboratorios.txt", 'r').read().splitlines()
        for linha in linhas:
            linha = linha.split(',')
            u = Laboratorio(linha[0], linha[1], linha[2])
            self.dados.append(u)
    def filaAgendamentos(self):
        linhas = open("DadosAgendamento.txt", 'r').read().splitlines()
        for linha in linhas:
            if ',' in linha:
                linha = linha.split(',')
                u = Agendamento(linha[0], linha[1], linha[2], linha[3], linha[4],
                                 linha[5], linha[6], linha[7], linha[8], linha[9])
                self.dados.append(u)
    def adicionar(self,elemento):
        self.dados.append(elemento)
    def remover(self):
        self.dados.pop(0)
    def lenFila(self):
        return len(self.dados)
    def zeraFila(self):
        self.dados =[]