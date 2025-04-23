class Carro:
    def __init__(self, marca, modelo, ano):
        # Inicializando os atributos da instância
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0  # Velocidade inicial é 0

    def acelerar(self, incremento):
        # Método para aumentar a velocidade do carro
        self.velocidade += incremento
        print(f"{self.marca} {self.modelo} acelerou para {self.velocidade} km/h.")

    def frear(self, decremento):
        # Método para diminuir a velocidade do carro
        self.velocidade -= decremento
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"{self.marca} {self.modelo} reduziu para {self.velocidade} km/h.")

    def exibir_informacoes(self):
        # Método para exibir as informações do carro
        print(f"Carro: {self.marca} {self.modelo} ({self.ano})")
        print(f"Velocidade atual: {self.velocidade} km/h")

# Criando uma instância da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2022)

# Exibindo as informações do carro
meu_carro.exibir_informacoes()

# Acelerando o carro
meu_carro.acelerar(30)
meu_carro.acelerar(20)

# Freando o carro
meu_carro.frear(15)

# Exibindo as informações atualizadas do carro
meu_carro.exibir_informacoes()