def aumento(valor, percentual):
    novo_valor = valor + (percentual/100 * valor)
    return novo_valor


print(aumento(1000, 15))
