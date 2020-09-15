from itertools import zip_longest
# ZIP: Junta listas|tuplas até a menor lista
print('#'*100)
print('ZIP')
cidades = ['Itabuna', 'São Paulo', 'Belo Horizonte', 'Porto alegre']
estados = ['BA', 'SP', 'MG']
cidades_estados = zip(estados, cidades)
print(list(cidades_estados))

# ZIP_LONGEST: junta listas|tuplas e adiciona None no valor da menor lista
print('#'*100)
print('ZIP_LONGEST')
cidades_estados_zip = zip_longest(estados, cidades)
print(list(cidades_estados_zip))
