from POO.ex_banco.banco import Banco
from POO.ex_banco.contas import ContaCorrente, ContaPoupanca
from POO.ex_banco.cliente import Cliente


banco = Banco()

cliente1 = Cliente('Aron', 28)
cliente2 = Cliente('João', 25)
cliente3 = Cliente('Zé', 19)

conta1 = ContaPoupanca(1111, 254136, 0)
conta2 = ContaCorrente(2222, 254237, 0)
conta3 = ContaPoupanca(1111, 254238, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(50)
    cliente1.conta.sacar(20)
else:
    print('Cliente não autenticado')

print('##############################################')

if banco.autenticar(cliente2):
    cliente2.conta.depositar(50)
    cliente2.conta.sacar(20)
else:
    print('Cliente não autenticado')
