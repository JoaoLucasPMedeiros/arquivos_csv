from pathlib import Path
import csv

#Criar o caminho

CAMINHO_NOVO = Path(__file__).parent / 'cursos.csv'
print('Caminho ===>', CAMINHO_NOVO)


lista_cursos = [
['python', '22.93', 'udemy'],
['oracle', '22.90', 'udemy'],
['aws', '22.90', 'udemy'],
]
# em modo de escrita ( w )
# keys pega as chaves que será minhas colunas

with open(CAMINHO_NOVO,'w') as arquivo:
    # colunas = lista_cursos[0].keys() <- modo automatico
    colunas = ['nomCurso', 'valorCurso', 'plataforma']
    escritor= csv.writer(arquivo)

    escritor.writerow(colunas)  
    for curso in lista_cursos:

        escritor.writerow(curso)
