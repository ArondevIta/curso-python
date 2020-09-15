from mapeamento.dados import produtos, pessoas, lista


precos = map(lambda p: p['preco'], produtos)

for preco in precos:
    print(preco)
