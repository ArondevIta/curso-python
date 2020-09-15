carrinho = []

carrinho.append(('Cadeira', 200))
carrinho.append(('Mesa', 150))
carrinho.append(('Mouse', 50))

total = sum([float(t) for p, t in carrinho])
print(total)
