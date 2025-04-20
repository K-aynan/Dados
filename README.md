# estudo_lambda.py
# Elevação ao Cubo em Python com Pandas

Este arquivo demonstra duas formas diferentes de elevar números ao cubo e aplicar isso a uma coluna de um DataFrame utilizando a biblioteca `pandas`.

## 💡 Definindo Operações

- Uma função tradicional é usada para retornar um valor ao cubo com a instrução `return x ** 3`.
- Em paralelo, uma função `lambda`, que é anônima e definida em uma única linha, realiza o mesmo cálculo.

## 🔢 Trabalhando com o DataFrame

- Um DataFrame é criado com uma coluna chamada `'numeros'` contendo inteiros.
- Duas novas colunas são adicionadas:
  - Uma aplica a **função tradicional** sobre cada valor da coluna original.
  - A outra aplica a **lambda**.

## 🔍 Objetivo

Comparar os resultados da função comum com a lambda e demonstrar como ambas podem ser utilizadas com o método `.apply()` do `pandas` para aplicar transformações em colunas.

## ✅ Resultado Esperado

- Uma tabela com três colunas:
  - A original com os números.
  - Uma com os números elevados ao cubo usando função.
  - Outra com os cubos obtidos pela lambda.

# intro_tratamento_dados.py
# Análise Exploratória de Dados com Pandas

Este arquivo realiza uma inspeção inicial de um conjunto de dados armazenado em um arquivo CSV, utilizando ferramentas da biblioteca `pandas`.

## 📄 Leitura de Dados

- Um arquivo CSV chamado `clientes.csv` é carregado em um DataFrame.
- A leitura é feita com `pandas`, o que transforma os dados em uma estrutura tabular para análise.

## 🔍 Primeiras Impressões

- As **primeiras 5 linhas** são exibidas com `head()`.
- As **últimas 5 linhas** com `tail()`.
- Ambas as visualizações usam `to_string()` para evitar truncamento de colunas.

## 📐 Dimensões

- A quantidade total de linhas e colunas é exibida usando `.shape`.
- O retorno tem o formato `(n_linhas, n_colunas)`.

## 🧬 Tipagem

- A função `dtypes` revela o tipo de dado de cada coluna:
  - Por exemplo: texto (`object`), números inteiros (`int64`), etc.

## 🚨 Valores Nulos

- Usa-se `.isnull().sum()` para:
  - Identificar quantos valores ausentes (`NaN`) existem por coluna.
  - A soma dá uma visão clara de colunas com dados incompletos.

## 📌 Conclusão

Esse script é útil para uma **primeira análise exploratória** e permite:
- Detectar colunas problemáticas,
- Entender o tipo de cada dado,
- E se preparar para etapas de limpeza e transformação.

# 🧼 Limpeza e Tratamento de Dados com Pandas

Este processo realiza uma limpeza completa em um DataFrame criado a partir de um arquivo CSV contendo dados de clientes. Abaixo, estão os passos explicados de forma detalhada:

---

# Limpeza_dados.py
## 📥 1. Leitura dos Dados

- Um arquivo chamado `clientes.csv` é carregado em um DataFrame.
- As opções de visualização são ajustadas para exibir o conteúdo completo sem quebra de linha.

---

## 🧹 2. Remoção de Dados

- Verifica-se se uma coluna chamada `'pais'` existe e, se existir, ela é removida.
- Uma linha específica (identificada por índice) também é excluída.

---

## ✏️ 3. Normalização de Texto

- A coluna com nomes recebe formatação de título (primeira letra maiúscula).
- A coluna de endereços é convertida para letras minúsculas.
- A coluna de estados tem espaços removidos e letras transformadas para maiúsculas.

---

## 🔄 4. Conversão de Tipos de Dados

- A coluna de idades é convertida explicitamente para o tipo inteiro.

---

## ❌ 5. Tratamento de Valores Ausentes

Várias abordagens são usadas:

- Substituição de valores nulos por `0`.
- Remoção completa de linhas com qualquer valor nulo.
- Manutenção apenas de registros que possuem pelo menos **4 valores não nulos**.
- Remoção de linhas onde o campo `'cpf'` está vazio.

Além disso:

- Coluna `'estado'` recebe o valor `'Desconhecido'` se estiver vazia.
- Endereços ausentes recebem o texto `'Endereco nao informado'`.
- Para a coluna `'idade'`, quando houver valores ausentes, eles são preenchidos com a **média** dessa coluna.

---

## 📅 6. Conversão de Datas

- Uma nova coluna é criada com as datas convertidas para o formato `datetime` com base no padrão `dia/mês/ano`.
- Erros na conversão são tratados e substituídos por valores nulos (`NaT`).

---

## 📛 7. Tratamento de Duplicatas

- O número de linhas antes e depois da remoção de duplicatas é exibido.
- Duplicatas são eliminadas com base na coluna `'cpf'`, garantindo registros únicos por cliente.

---

## 💾 8. Salvando o Resultado Final

- As colunas antigas de data e idade são substituídas pelas versões tratadas.
- Um novo DataFrame com colunas selecionadas é criado para exportação.
- O resultado final é salvo em um novo arquivo CSV chamado `clientes_limpeza.csv`.

---

## 📈 9. Verificação Final

- O novo arquivo CSV é carregado e exibido para garantir que os dados limpos foram corretamente salvos.

---

🎯 **Resumo**: Esse processo é essencial em projetos de ciência de dados para garantir que os dados estejam limpos, padronizados, completos e prontos para análise ou modelagem.

# outliers
# 🚨 Detecção e Remoção de Outliers com Pandas e SciPy

Este script realiza a limpeza avançada dos dados de clientes, com foco especial na remoção de *outliers* e validação de campos. Abaixo, está um guia detalhado das etapas realizadas:

---

## 📂 1. Leitura dos Dados

- Um DataFrame é criado a partir do arquivo `clientes_limpeza.csv`.
- A visualização do Pandas é configurada para não quebrar as linhas no console.

---

## 🔍 2. Filtro Básico de Idades

- Um primeiro filtro simples é aplicado para remover registros com idade igual ou superior a 100 anos.
- Apenas os registros com idade inferior são mantidos nesse subconjunto.

---

## 📊 3. Detecção de Outliers com Z-Score

- Os valores de idade são padronizados usando o **Z-score**, que mede o quão distante um valor está da média, em desvios-padrão.
- Registros com Z-score igual ou maior que 3 são considerados *outliers* e são listados.
- Um novo DataFrame é criado apenas com os registros dentro do intervalo aceitável de Z-score.

---

## 📈 4. Detecção de Outliers com IQR

- O **Intervalo Interquartil (IQR)** é calculado com base nos quartis 1 (Q1) e 3 (Q3).
- Limites inferior e superior são definidos com uma margem multiplicada por 1.15 para dar mais tolerância.
- Registros fora desses limites são identificados como *outliers*.
- Um novo DataFrame é criado mantendo apenas os valores dentro do intervalo IQR.

---

## ✋ 5. Filtro Manual de Outliers

- Uma abordagem direta é usada: manter apenas registros com idade entre 1 e 100 anos.

---

## 🏡 6. Validação de Endereços

- Endereços são validados com base no número de linhas (divididas por quebra de linha `\n`).
- Se o número de partes for inferior a 3, o endereço é marcado como **inválido**.

---

## 🧾 7. Tratamento de Nomes

- Nomes com mais de 50 caracteres são substituídos pela marcação `"Nome inválido"`.
- O total de registros com nomes considerados inválidos é contabilizado e exibido.

---

## 📤 8. Salvando os Dados Finais

- Os dados limpos, sem outliers e com campos verificados, são salvos em um novo arquivo chamado `clientes_remove_outliers.csv`.

---

🎯 **Resumo Final**:
Este fluxo é crucial para garantir que os dados usados em análises estatísticas ou modelos de machine learning estejam limpos, consistentes e sem valores extremos que possam distorcer os resultados.

# Inconsistencia.py
# 📄 Limpeza e Tratamento Avançado de Dados Pessoais em um DataFrame

Este guia documenta o processo de limpeza, padronização e anonimização de um conjunto de dados de clientes utilizando `pandas` e `numpy`.

---

## 🧹 1. Leitura Inicial do Arquivo

- O arquivo CSV com os dados originais de clientes é carregado em um DataFrame.
- As opções de exibição do Pandas são ajustadas para mostrar colunas e conteúdos longos de forma completa.

---

## 🕵️‍♂️ 2. Anonimização de Dados Pessoais

- O campo **CPF** é mascarado, substituindo os dígitos do meio por asteriscos (`***.***`) e mantendo apenas os três primeiros e os dois últimos.
- Registros inválidos (com menos de 11 caracteres) são marcados como `'CPF inválido'`.

---

## 📅 3. Correção de Datas

- As datas são convertidas para o formato `datetime`, tratando erros de formatação com um valor nulo (`NaT`).
- Para garantir consistência, datas futuras são substituídas por uma data padrão: `1900-01-01`.
- A idade é recalculada com base no ano atual, ajustando para o mês e o dia de nascimento.
- Idades acima de 100 anos são consideradas inconsistentes e substituídas por `NaN`.

---

## 🏘️ 4. Extração e Validação de Endereços

- O campo de endereço, originalmente contendo múltiplas linhas, é dividido:
  - O endereço principal é extraído da primeira linha.
  - O **bairro** é retirado da segunda linha, se existir.
  - A **sigla do estado** é capturada da parte final, separada por `' / '`.
- Endereços muito curtos ou muito longos são marcados como inválidos.

---

## 📌 5. Validação de Estados

- Os estados são convertidos para letras maiúsculas.
- Apenas siglas válidas do Brasil são mantidas; o restante é substituído por `'Desconhecido'`.

---

## 🔁 6. Substituições Finais

- O CPF original é substituído pela versão mascarada.
- A idade original é trocada pela idade ajustada.
- Os campos de endereço e estado também são substituídos pelas versões tratadas.
- Um novo DataFrame é formado contendo apenas os campos finais desejados.

---

## 💾 7. Exportação dos Dados

- O DataFrame tratado é salvo em um novo arquivo: `clientes_tratados.csv`.
- Esse novo arquivo é lido e exibido para verificação dos dados processados.

---

✅ **Resultado**:
Esse processo garante que os dados estejam:
- Completos e padronizados;
- Corrigidos de inconsistências de datas e endereços;
- Anonimizados para preservar a privacidade.

