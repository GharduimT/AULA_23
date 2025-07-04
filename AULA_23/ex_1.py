from datetime import datetime
import pandas as pd
import polars as pl
#  pandas 20
#  polars 7

#  obtendo dados

try:
    ENDERECO_DADOS = r'../dados/'

    hora_inicio = datetime.now()

    print('Carregando...')

    # # #  Pandas
    # df_janeiro = pd.read_csv(ENDERECO_DADOS + '202501_NovoBolsaFamilia.csv', sep=';', encoding='iso-8859-1')
    # print(df_janeiro.head())
    #  Polars
    df_janeiro = pl.read_csv(ENDERECO_DADOS + '202501_NovoBolsaFamilia.csv', separator=';', encoding='iso-8859-1')

    print(df_janeiro.head())

    #  tempo final
    hora_final = datetime.now()

    print(f'Tempo de Execução:{hora_final - hora_inicio}')
except Exception as e:
    print(f'Erro ao obter dados {e}')