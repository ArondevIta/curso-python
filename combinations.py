from itertools import combinations, permutations, product

pessoas = ['Aron', 'Saulo', 'Zaine', 'Raimunda', 'Milena', 'Italo']

for grupo in product(pessoas, repeat=2):
    print(grupo)
