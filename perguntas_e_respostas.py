perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2?',
        'respostas': {'a': '1', 'b': '2', 'c': '4'},
        'resposta_certa': 'c'
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 2*3?',
        'respostas': {'a': '1', 'b': '6', 'c': '4'},
        'resposta_certa': 'b'
    },
}

respostas_certas = 0

for pergunta_k, pergunta_v in perguntas.items():
    print(f'{pergunta_k}: {pergunta_v["pergunta"]}')
    print('Opções Abaixo: ')
    for resposta_k, resposta_v in pergunta_v['respostas'].items():
        print(f'[{resposta_k}]: {resposta_v}')
    resposta_usuario = input('Digite sua resposta: ')

    if resposta_usuario == pergunta_v['resposta_certa']:
        print('Acertou miseravi!!!')
        respostas_certas += 1
    else:
        print('ERROUUUUUU - Faustão !!!')
    print()

qtd_perguntas = len(perguntas)
porcentagem_acertos = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} perguntas')
print(f'Sua porcentagem de acerto foi de: {porcentagem_acertos}%')
