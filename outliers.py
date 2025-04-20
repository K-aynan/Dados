import pandas as pd
from scipy import stats

pd.set_option('display.width', None)

# Carregar o arquivo CSV
df = pd.read_csv('clientes_limpeza.csv')

# Filtro básico para idades acima de 100
df_filtro_basico = df[df['idade'] < 100]
print('Filtro básico:\n', df_filtro_basico[['nome', 'idade']])

# Identificar outliers com Z-score
z_scores = stats.zscore(df['idade'].dropna())
outliers_z = df[(z_scores >= 3)]
print("Outliers pelo Z-score:\n", outliers_z)

# Filtrar outliers com Z-score
df_zscore = df[(stats.zscore(df['idade'].dropna()) < 3)]

# Identificar outliers com IQR
Q1 = df['idade'].quantile(0.25)
Q3 = df['idade'].quantile(0.75)
IQR = Q3 - Q1

limite_baixo = Q1 - 1.15 * IQR
limite_alto = Q3 + 1.15 * IQR

print("Limites IQR:\n", limite_baixo, limite_alto)

outliers_iqr = df[(df['idade'] < limite_baixo) | (df['idade'] > limite_alto)]
print("Outliers pelo IQR:\n", outliers_iqr)

# Filtrar outliers com IQR
df_iqr = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]

#filtrar outliers manualmente
limite_baixo = 1
limite_alto = 100
df = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]

#filtrar enderecos inválidos
df['endereco'] = df['endereco'].apply(lambda x: 'Endereco inválido' if len(x.split('\n')) < 3 else x)

#tratar campos de texto
df['nome'] = df['nome'].apply(lambda x: 'Nome inválido' if  isinstance(x, str) and len(x) > 50 else x)
print('Qtd registros com nomes grandes: ', (df['nome'] == 'Nome inválido').sum())
print('Dados com outliers tratados:\n', df)

df.to_csv('clientes_remove_outliers.csv', index=False)