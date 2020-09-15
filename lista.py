secreto = 'perfume'
digitados = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu :(')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Opa, você não pode digitar mais de uma letra...')
        continue
    digitados.append(letra)

    if letra in secreto:
        print(f'ISSO AÍÍÍÍ: a letra "{letra}" existes na palavra secreta')
    else:
        print(f'OOPS: a letra "{letra}" não existre na palavra secreta')
        digitados.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitados:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Muito bem, você ganhouuu!!! A palavra era {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1
        print(f'Você ainda tem {chances} chances.')
