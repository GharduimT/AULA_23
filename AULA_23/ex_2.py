from datetime import datetime
import pandas as pd
import polars as pl

#  obtendo dados
# rodando os 5 levou 5 minutos
# rodando os 2 levou 50 segundos
# try:
#     ENDERECO_DADOS = r'../dados/'

#     hora_inicio = datetime.now()

#     lista_arquivos = ['202501_NovoBolsaFamilia.csv', '202502_NovoBolsaFamilia.csv', '202503_NovoBolsaFamilia.csv', '202504_NovoBolsaFamilia.csv', '202505_NovoBolsaFamilia.csv']

#     df_bolsa_familia = None

#     for arquivo in lista_arquivos:
#         print(f'Processando o arquivo {arquivo}')

#         df = pd.read_csv(ENDERECO_DADOS + arquivo, sep=';', encoding='iso-8859-1')

#         if df_bolsa_familia is None:
#             df_bolsa_familia = df
#         else:
#             df_bolsa_familia = pd.concat([df_bolsa_familia, df])
#         print(df)
#         print(df.shape)
        
#         #  limpar a memória
#         del df
#     print('Bolsa Familia Concatenado')
#     print(df_bolsa_familia.head())
#     print(df_bolsa_familia.shape)

#     #  Tempofinal
#     hora_final = datetime.now()

#     print(f'Tempo de Execução:{hora_final - hora_inicio}')

# except Exception as e:
#     print(f'Deu ruim {e}')

 #'''Rodando com pollars'''   
# rodando os 5 levou 40 segundos
# rodando os 2 levou 12 segundos
try:
    ENDERECO_DADOS = r'../dados/'

    hora_inicio = datetime.now()

    lista_arquivos = ['202501_NovoBolsaFamilia.csv', '202502_NovoBolsaFamilia.csv']

    df_bolsa_familia = None

    for arquivo in lista_arquivos:
        print(f'Processando o arquivo {arquivo}')

        df = pl.read_csv(ENDERECO_DADOS + arquivo, separator=';', encoding='iso-8859-1')

        if df_bolsa_familia is None:
            df_bolsa_familia = df
        else:
            df_bolsa_familia = pl.concat([df_bolsa_familia, df])
        print(df)
        print(df.shape)
        
        #  limpar a memória
        del df
    print('Bolsa Familia Concatenado')
    print(df_bolsa_familia.head())
    print(df_bolsa_familia.shape)

    #  Tempofinal
    hora_final = datetime.now()

    print(f'Tempo de Execução:{hora_final - hora_inicio}')

except Exception as e:
    print(f'Deu ruim {e}')