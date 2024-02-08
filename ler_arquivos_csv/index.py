from pathlib import Path
#Gera um caminho do arquivo
import csv
CAMINHO_CSV = Path(__file__).parent / 'alunos.csv'

print('CAMINHO DO ARQUIVO --> ',CAMINHO_CSV);

# Abrir um arquivo 
""" 
with open (CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha) 

 """# Abrir um em forma de dicionario
with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(linha)