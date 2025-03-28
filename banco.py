class ContaBancaria:
    def __init__(self, titular, numero_conta, saldo=0):
        """Inicializa a conta bancária com titular, número da conta e saldo inicial (padrão 0)."""
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.conta_ativa = True  # A conta começa como ativa
    
    def deposito(self, valor):
        """Realiza um depósito na conta, aumentando o saldo."""
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido. O valor deve ser maior que 0.")
    
    def saque(self, valor):
        """Realiza um saque, diminuindo o saldo da conta, se houver saldo suficiente."""
        if not self.conta_ativa:
            print("A conta foi excluída. Não é possível realizar transações.")
            return
        
        if valor <= 0:
            print("Valor de saque inválido. O valor deve ser maior que 0.")
        elif valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
    
    def mostrar_saldo(self):
        """Exibe o saldo atual da conta."""
        if not self.conta_ativa:
            print("A conta foi excluída. Não é possível verificar o saldo.")
            return
        
        print(f"Saldo atual da conta {self.numero_conta} de {self.titular}: R${self.saldo:.2f}")
    
    def excluir_conta(self):
        """Exclui a conta bancária (a conta fica inativa)."""
        if not self.conta_ativa:
            print("A conta já foi excluída.")
        else:
            self.conta_ativa = False
            print(f"A conta {self.numero_conta} foi excluída com sucesso.")


conta1 = ContaBancaria("João", 12345, 1000)

conta1.mostrar_saldo()

conta1.deposito(500)

conta1.saque(200)

conta1.mostrar_saldo()

conta1.excluir_conta()

conta1.saque(100)

conta1.mostrar_saldo()
