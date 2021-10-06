import plotly.express as px
import pandas as pd

tabela = pd.read_csv('nome_do_arquivo.csv')
# Método .drop para excluir colunas indesejadas
tabela = tabela.drop('nome_da_coluna', axis=1)
display(tabela)

# Tratando os dados
# 1 Valores reconhecidos de forma errada
tabela['nome_da_coluna'] = pd.to_numeric(
    tabela['nome_da_coluna'], errors='coerce')
# 2 Deletar colunas e linhas vazias
tabela = tabela.dropna(how='all', axis=1)
tabela = tabela.dropna(how='any', axis=0)
print(tabela.info())

# Analisando...
print(tabela['nome_da_coluna'].value_counts())
print(tabela['nome_da_coluna'].value_counts(
    normalize=True).map('{:.1%}'.format))

# Detalhamento da Análise
# color_descrete_sequence=[colors]
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color='nome_da_coluna')
    grafico.show()
