import cnpj

cnpj1 = 'aaa'
cnpj2 = '00.000.000/0000-00'
cnpj3 = '04.252.011/0001-10'

if cnpj.valida(cnpj1):
    print(f'{cnpj1} é válido')
else:
    print(f'{cnpj1} é inválido')

for i in range(100):
    novo_cnpj = cnpj.gera()
    formatado = cnpj.formata(novo_cnpj)
    print(novo_cnpj, formatado)
