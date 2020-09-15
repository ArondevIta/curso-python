from itertools import groupby
alunos = [
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Maria', 'nota': 'C'},
    {'nome': 'Jose', 'nota': 'B'},
    {'nome': 'Carlos', 'nota': 'D'},
    {'nome': 'Jhon', 'nota': 'A'},
    {'nome': 'Juliana', 'nota': 'E'},
    {'nome': 'James', 'nota': 'A'},
    {'nome': 'Carol', 'nota': 'F'},
    {'nome': 'Paulo', 'nota': 'D'},
    {'nome': 'Roberto', 'nota': 'C'},
    {'nome': 'Marcio', 'nota': 'B'},
    {'nome': 'Marinaldo', 'nota': 'D'},
    {'nome': 'Ueliton', 'nota': 'B'},
    {'nome': 'Marcelo', 'nota': 'A'},
]

ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    print(f'Nota: {agrupamento}')
    quantidade = len(list(valores_agrupados))
    print(f'{quantidade} alunos que tiraram a nota {agrupamento}')
