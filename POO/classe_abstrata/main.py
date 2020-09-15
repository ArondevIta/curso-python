from POO.classe_abstrata.poupanca import ContaPoupanca
from POO.classe_abstrata.corrente import ContaCorrente

cp = ContaPoupanca(111, 2222, 0)
cp.depositar(20)
cp.sacar(15)
cp.sacar(5)
cp.sacar(5)

print('###########################################')

cc = ContaCorrente(agencia=123, conta=6546, saldo=0, limite=500)
cc.depositar(100)
cc.sacar(250)
