class Usuario:
    
    def __init__(self, tipo, login, senha, nome, email,telefone,status):
        '''Classe Usuario ue registra altera e valida usuarios possui os atributos, login,senha,nome,tipo,email,telefone,status'''
        self.__login = login
        self.__senha = senha
        self.__nome = nome
        self.__tipo = tipo
        self.__email = email
        self.__tell = telefone
        self.__status = status
    
    @property
    def login(self):
        return self.__login
    
    @login.setter
    def login(self,valor):
        self.__login = valor

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, valor):
        self.__senha = valor

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, valor):
        self.__tipo = valor

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome= valor

    @property
    def tell(self):
        return self.__tell

    @tell.setter
    def tell(self, valor):
        self.__tell = valor

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):
        self.__email = valor

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, valor):
        self.__status = valor

    def validarLogon(self, login, senha):
        '''Metodo que verifica o login do usuario, validando se seus dados estiverem de acordo'''
        return login == self.login and senha == self.senha and self.status == 'Ativo'
    def verificarUsuario(self,login):
        return login == self.__login

    def alterarDados(self):
        '''Metodo que abre a base de dados e altera os dados do usuario selecionado'''
        linhas = open("DadosUsuarios.txt", 'r').read().splitlines()
        for x in range(len(linhas)):
            if self.login in linhas[x]:
                novo = open("DadosUsuarios.txt", 'w')
                linhas[x] = self.tipo + "," + self.login + "," + self.senha + ',' + self.nome + ',' + self.email + ',' + self.tell+','+self.status
                novo.write('\n'.join(linhas))

    def registrarUsuario(self):
        '''Metodo que abre a base de dados e registra usuario'''
        usuarios = open("DadosUsuarios.txt", 'a')
        tempcad = self.tipo + "," + self.login + "," + self.senha + ',' + self.nome + ',' + self.email + ',' + self.tell+','+self.status
        usuarios.write(tempcad + '\n')

        usuarios.close()











