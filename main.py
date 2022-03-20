perguntas = {
    '\nPergunta 1': {
        'pergunta': 'Quem é Linus Torvalds? \n',
        'respostas': {'a': 'Criador da Linguagem C', 'b': 'Criador do Linux', 'c': 'Criador da FSF',
                      'd': 'Criador do Youtube\n'},
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Qual foi o nome do primeiro computador? \n',
        'respostas': {'a': 'ENIAC', 'b': 'Macintosh', 'c': 'Assembly', 'd': 'COBOL\n'},
        'resposta_certa': 'a',
    },


}

for pk, pv in perguntas.items():  # (PK) = Chave da Pergunta, (PV) = Valor da Pergunta
    print(f'{pk}: {pv["pergunta"]}')

    for rk, rv in pv['respostas'].items():  # (RK) = Chave da Resposta, (RV) = Valor da Resposta
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Selecione uma alternativa: ')

    if resposta_usuario == pv['resposta_certa']:
        print('\nResposta Verdadeira\n')
    else:
        print('\nResposta Falsa\n')
