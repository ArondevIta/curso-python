lista = [
    ['P1', 13],
    ['P1', 16],
    ['P1', 5],
    ['P1', 50],
    ['P1', 8],
]

lista.sort(key=lambda item: item[1])
print(f'lista com sort {lista}')

print('lista com sorted', sorted(lista, key=lambda i: i[1]))
