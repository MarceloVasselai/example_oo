class Pessoa:
    def __init__(self, nome, idade):
        # Atributos da instância
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        # Método que utiliza o atributo da instância
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

# Criando uma instância da classe Pessoa
pessoa1 = Pessoa("João", 30)

# Chamando o método apresentar
pessoa1.apresentar()