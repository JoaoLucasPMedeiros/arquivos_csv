condicao = True
#LISTAS
colunas = ['NOME','FORMACAO', 'IDADE', 'INSTITUICAO']
nome        = []
formacao    = []
idade       = []
instituicao = []

#LOGICA PRA ADD LISTA
while condicao:
    pergunta = input('s - sair ')
    ## SAIR DO LAÇO
    if pergunta == 'S' or pergunta == 's':
        break
    NOME        = input('Digite seu nome: ');
    FORMACAO    = input('Sua formação: ');
    IDADE       = input('Idade: ');
    INSTITUICAO = input('Instituição de ensino: ');
    
    nome.append(NOME);
    formacao.append(FORMACAO);
    idade.append(IDADE);
    instituicao.append(INSTITUICAO);

    CSV = [list(a) for a in zip(nome, formacao, idade, instituicao)]

print(CSV[0])


    




