from POO.composicao.classes import Cliente

cliente1 = Cliente('Luiz', 32)
cliente1.insere_endereco('Rio de janeiro', 'RJ')
cliente1.lista_enderecos()
print()

cliente2 = Cliente('João', 56)
cliente2.insere_endereco('Salvador', 'BA')
cliente2.insere_endereco('Itabuna', 'BA')
cliente2.lista_enderecos()
print()

cliente3 = Cliente('Carlos', 18)
cliente3.insere_endereco('Fortaleza', 'CE')
cliente3.lista_enderecos()
