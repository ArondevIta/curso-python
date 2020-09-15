clientes = {
    'cliente1': {
        'nome': 'Aron',
        'sobrenome': 'Madson'
    },
    'cliente2': {
        'nome': 'Carlos',
        'sobrenome': 'Silva'
    },
}

for cliente_id, cliente_valor in clientes.items():
    print(f'exibindo {cliente_id}')
    for dados_id, dados_valor in cliente_valor.items():
        print(f'\t{dados_id} = {dados_valor}')
