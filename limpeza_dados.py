import pandas as pd

df = pd.read_csv('clientes.csv')

pd.set_option('display.width', None)
print(df.head())

#remover dados
if 'pais' in df.columns:
  df.drop('pais', axis=1, inplace=True)
df.drop(2, axis=0, inplace=True)

#normalizar campo de texto
df['nome'] = df['nome'].str.title()
df['endereco'] = df['endereco'].str.lower()
df['estado'] = df['estado'].str.strip().str.upper()

#converter tipo de dado
df['idade'] = df['idade'].astype(int)

#tratar valores nulos/ausentes
df_fillna = df.fillna(0)# substitui valores nulos por 0
df_dropna = df.dropna()# remove registro com valores nulos
df_dropna4 = df.dropna(thresh=4) #mantem registro com min. 4 valores nao nulos
df = df.dropna(subset=['cpf'])# remove cpf nulo

print('Valores nulos:\n', df.isnull().sum())
print('Qts de registro nulos com fillna:\n', df_fillna.isnull().sum().sum())
print('Qts de registro nulos com dropna:\n', df_dropna.isnull().sum().sum())
print('Qts de registro nulos com dropna4:\n', df_dropna4.isnull().sum().sum())
print('Qts de registro nulos com CPF:\n', df.isnull().sum().sum())

df.fillna({'estado': 'Desconhecido'}, inplace=True)
df['endereco'] = df['endereco'].fillna('Endereco nao informado')
df['idade_corrigida'] = df['idade'].fillna(df['idade'].mean())

#tratar formato de dados
df['data_corrigida'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

#tratar dados duplicados
print('Qtd de registros atual: ', df.shape[0])
df.drop_duplicates()
df.drop_duplicates(subset='cpf', inplace=True)
print('Qtd registros removendo as duplicadas: ', len(df))

print('Dados Limpos:\n', df)

#salvar dataframe
df['data'] = df['data_corrigida']
df['idade'] = df['idade_corrigida']

df_salvar = df[['nome', 'cpf', 'idade', 'data', 'endereco', 'estado']]
df_salvar.to_csv('clientes_limpeza.csv', index=False)

print('Novo DataFrame: \n', pd.read_csv('clientes_limpeza.csv'))