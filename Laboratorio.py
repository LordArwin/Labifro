class Laboratorio:
    def __init__(self,tipoLab,nomeSala,numeroChave):
        self.__tipoLab=tipoLab
        self.__nomeSala = nomeSala
        self.__numeroChave = numeroChave

    @property
    def tipoLab(self):
        return self.__tipoLab

    @tipoLab.setter
    def tipoLab(self, valor):
        self.__tipoLab = valor

    @property
    def numeroChave(self):
        return self.__numeroChave

    @numeroChave.setter
    def numeroChave(self, valor):
        self.__numeroChave = valor

    @property
    def nomeSala(self):
        return self.__nomeSala

    @nomeSala.setter
    def nomeSala(self, valor):
        self.__nomeSala = valor

    def validarCad(self,numeroChave,tipo):
        return numeroChave == self.numeroChave and tipo == self.tipoLab
    def registrarLab(self):
        linhas = open("DadosLaboratorios.txt", 'a')
        templab = self.tipoLab + "," + self.nomeSala + "," + self.numeroChave
        linhas.write(templab + '\n')

        linhas.close()