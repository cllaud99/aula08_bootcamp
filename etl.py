import pandas as pd
import os
import glob

pasta = 'data'

def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total


def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    print(df)
    return df


def carregar_dados(df: pd.DataFrame, format_saida: list):
    for formato in format_saida:
        if formato == 'csv':
            df.to_csv("dados.csv")
            print('passou por aqui')
        if formato == 'parquet':
            print('passou por aqui tambem')
            df.to_parquet("dados.parquet")

if __name__ == "__main__":
    pasta_argumento = 'data'
    # Chamar a função para extrair dados e consolidar
    df = extrair_dados_e_consolidar(pasta_argumento)
    # Chamar a função para calcular o KPI de total de vendas
    df = calcular_kpi_de_total_de_vendas(df)
    # Chamar a função para carregar os dados
    format_saida = ['csv', 'parquet']
    carregar_dados(df, format_saida)
