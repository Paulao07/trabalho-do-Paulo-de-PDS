class Carro:
    def __init__(self, marca, modelo, ano, velocidade=0):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade

    def mostrar_dados(self):
        print(f"Marca do carro: {self.marca}")
        print(f"Modelo do carro: {self.modelo}")
        print(f"Ano de fabricação: {self.ano}")
        print(f"Velocidade atual: {self.velocidade} km/h")

    def mover(self, aumento_velocidade):
        """Aumenta a velocidade do carro e simula o movimento."""
        self.velocidade += aumento_velocidade
        print(f"O carro está se movendo a {self.velocidade} km/h.")

carro1 = Carro("Volkswagen", "Fusca", 1970)

carro1.mostrar_dados()

carro1.mover(40) 

carro1.mostrar_dados()