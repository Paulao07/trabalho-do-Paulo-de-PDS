import random

class JogoAdivinhacao:
    def __init__(self, tamanho_lista):
        self.lista = random.sample(range(1, 100), tamanho_lista) 
        self.lista_ordenada = self.selection_sort(self.lista)  
        self.tentativas = 0  

    def selection_sort(self, lista):
        n = len(lista)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if lista[j] < lista[min_index]:
                    min_index = j
            lista[i], lista[min_index] = lista[min_index], lista[i]
        return lista

    def procurar_numero(self, lista, alvo, inicio, fim):
        if inicio > fim:  
            return -1
        
        meio = (inicio + fim) // 2 
        
        if lista[meio] == alvo:
            return meio  
        elif lista[meio] < alvo:
            return self.procurar_numero(lista, alvo, meio + 1, fim)  
        else:
            return self.procurar_numero(lista, alvo, inicio, meio - 1) 

    def jogar(self):
        print("Bem-vindo ao game do Paulo")
        print("A lista do game foi embaralhada.")
        print("diga um número ai e tente acertálo.")
        
        while True:

            try:
                numero = int(input(f"Diga um numero aí de 1 a 100(sem repetição) ou 0 para sair: "))
            except ValueError:
                print("ops NUMERO NAO ENCONTRADO!!.")
                continue
            
            if numero == 0:
                print("Jogo encerrado. Até mais campeão")
                break

            if numero not in self.lista:
                print("Este número não está na lista.")
                continue
            
            self.tentativas += 1
            indice = self.procurar_numero(self.lista_ordenada, numero, 0, len(self.lista_ordenada) - 1)
            
            if indice != -1:
                print(f"BOA!!!!! O número {numero} foi encontrado na posição {indice} na lista do game!.")
            else:
                print(f"O número {numero} não foi encontrado na lista do game. jogue novamente.")

            print(f"Tentativas feitas: {self.tentativas}")


jogo = JogoAdivinhacao(10)
jogo.jogar()
