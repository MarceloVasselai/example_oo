class Carro:
    def __init__(self, marca, modelo):  # Construtor da classe
        self.marca = marca  # Atributo da instância
        self.modelo = modelo

    def exibir_info(self):  # Método da instância
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

# Criando uma instância da classe
meu_carro = Carro("Toyota", "Corolla")

# Acessando os atributos e métodos da instância usando 'self'
meu_carro.exibir_info()  # Output: Marca: Toyota, Modelo: Corolla