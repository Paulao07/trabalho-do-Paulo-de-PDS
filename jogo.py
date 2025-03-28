import random

def jogar():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 10  

    print("Bem-vindo ao jogo de adivinhar o número!")
    print(f"Eu pensei em um número entre 1 e 100. Você tem {max_tentativas} tentativas para acertar.")
    
    while tentativas < max_tentativas:
        tentativas += 1
        palpite = int(input(f"Tentativa {tentativas}/{max_tentativas}. Qual é o seu palpite? "))
        
        if palpite < numero_secreto:
            print("O número é maior. Tente novamente!")
        elif palpite > numero_secreto:
            print("O número é menor. Tente novamente!")
        else:
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas!")
            break
    else:
        print(f"Você não acertou o número. O número secreto era {numero_secreto}.")

jogar()
