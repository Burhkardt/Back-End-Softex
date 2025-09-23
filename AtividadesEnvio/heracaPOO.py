#Exercício 1
class Usuario():
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    def exibir_informacoes(self):
        print(f"Nome: {self.nome}\nEmail: {self.email}")
    def saudacao(self):
        print("Olá, usuário")
    def __str__(self):
        return f"Esta pessoa se chama {self.nome} e o email dela é {self.email}"

class Cliente(Usuario):
    def __init__(self, nome, email, saldo):
        super().__init__(nome, email)
        self.saldo = saldo
    def saudacao(self):
        print("Olá, cliente")

cara = Cliente("Mano", "juzé@imeiu.con", 200)
cara.exibir_informacoes()
cara.saudacao()

class Funcionarios(Usuario):
    print("Isso não deveria ser printado")
class Gerente(Funcionarios):
    def n(self):
        pass

gerente = Gerente("Mr.Gerente", "emaildogerente@gerencia.gerente")
print(gerente)
gerente.exibir_informacoes()
print(gerente.nome)

class Autenticacao():
    def login(self):
        print("Uau, feito login :p")
    def status(self):
        print("A")

class Permissao():
    def verificar_permissao(self):
        print("Feito permissão")
    def status(self):
        print()

class Administrador(Autenticacao, Permissao):
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
pessoa = Administrador("Mr. Administração", "emailmuitobrabo@email.moc")
pessoa.verificar_permissao()
pessoa.status()
print(Administrador.__mro__)