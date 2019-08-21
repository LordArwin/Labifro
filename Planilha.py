from tkinter import messagebox

import xlwt

from Fila import Fila

class Planilha(object):
    def __init__(self,mes,ano):
        self.__mes = mes
        self.__anoReferenciado = ano
        self.listaMeses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro','Dezembro','Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro','Dezembro')

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, valor):
        self.__mes = valor

    @property
    def anoReferenciado(self):
        return self.__anoReferenciado

    @anoReferenciado.setter
    def anoReferenciado(self, valor):
        self.__anoReferenciado = valor

    @property
    def listaMeses(self):
        return self.__listaMeses

    @listaMeses.setter
    def listaMeses(self, valor):
        self.__listaMeses = valor


    def gerarPlanilha(self):
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet(u'Agendamentos')
        worksheet.write(0, 0, u'Laboratorio')
        worksheet.write(0, 1, u'Chave')
        worksheet.write(0, 2, u'Turno')
        worksheet.write(0, 3, u'Data')
        worksheet.write(0, 4, u'Turma')
        worksheet.write(0, 5, u'Tempos')
        worksheet.write(0, 6, u'Professor')
        worksheet.write(0, 7, u'S.C.E.')
        worksheet.write(0, 8, u'S.C.D.')
        worksheet.write(0, 9, u'Status')

        linhas = Fila()
        linhas.filaAgendamentos()
        if int(self.mes)>12:
            self.mes=1
        self.mestemp=self.mes
        if self.mes<10:
            self.mestemp='0{}'.format(self.mes)
        c = 2
        for i in linhas.dados:
            if i.data[3:10] == '{}-{}'.format(self.mestemp,self.anoReferenciado):
                worksheet.write(c, 0, u'{}'.format(i.laboratorio))
                worksheet.write(c, 1, u'{}'.format(i.sala))
                worksheet.write(c, 2, u'{}'.format(i.turno))
                worksheet.write(c, 3, u'{}'.format(i.data))
                worksheet.write(c, 4, u'{}'.format(i.turma))
                worksheet.write(c, 5, u'{}'.format(i.tempos))
                worksheet.write(c, 6, u'{}'.format(i.professor))
                worksheet.write(c, 7, u'{}'.format(i.confirmaEntrega))
                worksheet.write(c, 8, u'{}'.format(i.confirmaDevolucao))
                worksheet.write(c, 9, u'{}'.format(i.status))
                c += 1
        messagebox.showwarning('AVISO','PLANILHA GERADA COM SUCESSO')
        workbook.save('Planilhas/{} {}.xls'.format(self.listaMeses[self.mes-1],self.anoReferenciado))
