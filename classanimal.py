class Animal:
    def __init__(self, nome, especie, som):
        self.nome = nome
        self.especie = especie
        self.som = som

    def fazer_som(self):
        print(f"O {self.nome}, que é um(a) {self.especie}, faz o som: {self.som}")

    def mostrar_dados(self):
        print(f"Nome do animal: {self.nome}")
        print(f"Espécie: {self.especie}")
        print(f"Som que ele faz: {self.som}")

animal1 = Animal("Cachorro", "Au au")

animal1.mostrar_dados()

animal1.fazer_som()
