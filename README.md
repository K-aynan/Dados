# Elevação ao Cubo de Números

Este exemplo demonstra como usar funções convencionais e lambdas para elevar números ao cubo em Python, aplicando esses métodos a um `DataFrame` do `pandas`.

## Código

```python
import pandas as pd

# Definição de uma função convencional que eleva um número ao cubo
def eleva_cubo(x):
  return x ** 3

# Definindo uma função lambda que eleva um número ao cubo
eleva_cubo_lambda = lambda x: x ** 3

# Testando a função convencional
print(eleva_cubo(2))  # Resultado esperado: 8

# Testando a função lambda
print(eleva_cubo_lambda(2))  # Resultado esperado: 8

# Criando um DataFrame com uma coluna de números
df = pd.DataFrame({'numeros': [1, 2, 3, 4, 5, 10]})

# Aplicando a função convencional usando 'apply'
df['cubo_funcao'] = df['numeros'].apply(eleva_cubo)

# Aplicando a função lambda usando 'apply'
df['cubo_lambda'] = df['numeros'].apply(lambda x: x ** 3)

# Exibindo o DataFrame resultante
print(df)

# Análise Inicial de um DataFrame com Pandas

Este exemplo realiza uma análise inicial de um conjunto de dados lido de um arquivo CSV chamado `clientes.csv`, utilizando a biblioteca `pandas`.

## Código

```python
import pandas as pd

# Leitura do arquivo CSV
df = pd.read_csv('clientes.csv')

# Exibir as 5 primeiras linhas do DataFrame
print(df.head().to_string())

# Exibir as 5 últimas linhas do DataFrame
print(df.tail().to_string())

# Exibir a quantidade de linhas e colunas (shape)
print('Qtd: ', df.shape)

# Exibir os tipos de dados de cada coluna
print('Tipagem:\n', df.dtypes)

# Exibir a quantidade de valores nulos por coluna
print('Valores nulos:\n', df.isnull().sum())
