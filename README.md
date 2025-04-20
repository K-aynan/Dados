# 📁 Data Processing Scripts (Pandas + Python)

This collection of Python scripts demonstrates various data transformation, cleaning, and inspection techniques using the `pandas`, `numpy`, and `scipy` libraries.

---

## 📌 `estudo_lambda.py`

### 🎯 Cubing Numbers in Python with Pandas

This script shows two different methods to cube numbers and apply them to a column in a Pandas DataFrame.

### 💡 Defining Operations

- A **regular function** is created to return a number cubed (`x ** 3`).
- A **lambda function** (anonymous one-liner) performs the same operation.

### 🔢 DataFrame Transformation

- A DataFrame with a `'numbers'` column is created.
- Two new columns are added:
  - One using the **traditional function** via `.apply()`.
  - Another using the **lambda function** via `.apply()`.

### ✅ Expected Output

The resulting DataFrame should contain:
- The original numbers.
- The cubed values (via the regular function).
- The cubed values (via the lambda function).

---

## 📌 `intro_tratamento_dados.py`

### 📊 Exploratory Data Analysis with Pandas

Performs an initial inspection of the dataset found in `clientes.csv`.

### 📥 Data Loading

- Loads `clientes.csv` into a DataFrame.
- Display settings are adjusted to prevent column truncation.

### 🔍 First Look at the Data

- Shows the **first 5 rows** using `head()`.
- Shows the **last 5 rows** using `tail()`.
- Uses `.to_string()` for full-width visibility.

### 📐 Shape and Structure

- Uses `.shape` to return `(rows, columns)`.
- Uses `.dtypes` to display column data types (e.g., `int64`, `object`).

### 🚨 Null Values

- `.isnull().sum()` shows the number of missing values in each column.

### ✅ Summary

A simple script to explore the structure and health of the dataset before deeper processing.

---

## 📌 `limpeza_dados.py`

### 🧼 Data Cleaning and Standardization

Processes and cleans the `clientes.csv` dataset using several standard data cleaning techniques.

### 📥 1. Load Data

- Loads the raw data into a DataFrame.
- Adjusts Pandas display settings for better visibility.

### 🧹 2. Column and Row Removal

- Drops the `'pais'` column if it exists.
- Removes specific rows (e.g., by index).

### ✏️ 3. Text Normalization

- Capitalizes names (`str.title()`).
- Converts addresses to lowercase.
- Strips and capitalizes state codes.

### 🔁 4. Data Type Conversion

- Converts the `'idade'` column to `int`.

### ❌ 5. Handling Missing Values

- Replaces nulls with 0.
- Drops rows with any missing value.
- Keeps rows with at least 4 non-null values.
- Drops rows with an empty `'cpf'` field.
- Fills empty `'estado'` with `"Desconhecido"`.
- Fills missing addresses with `"Endereco nao informado"`.
- Fills missing ages with the mean of the column.

### 📅 6. Date Conversion

- Converts date strings to datetime objects (`dd/mm/yyyy`).
- Invalid formats become `NaT`.

### 📛 7. Duplicate Removal

- Removes duplicates based on `'cpf'`.

### 💾 8. Final Export

- Saves cleaned data to `clientes_limpeza.csv`.

### 📈 9. Final Check

- Reads back the saved CSV to verify the cleaning process.

---

## 📌 `outliers.py`

### 🚨 Outlier Detection and Removal

Cleans client data by removing statistical outliers and validating fields.

### 📥 1. Load Cleaned Data

- Reads `clientes_limpeza.csv`.

### 🔍 2. Basic Age Filter

- Removes entries where `idade >= 100`.

### 📊 3. Z-Score Outlier Detection

- Computes Z-scores for `'idade'`.
- Values with `z >= 3` are considered outliers.
- Filters DataFrame to only keep acceptable values.

### 📈 4. IQR Outlier Detection

- Calculates Q1, Q3, and IQR.
- Sets bounds:  
  `lower = Q1 - 1.15 * IQR`,  
  `upper = Q3 + 1.15 * IQR`.
- Filters out ages outside the bounds.

### ✋ 5. Manual Filtering

- Keeps only ages between 1 and 100.

### 🏡 6. Address Validation

- Marks as invalid if address has fewer than 3 lines (`\n` separated).

### 🧾 7. Name Validation

- Names longer than 50 characters are flagged as `"Nome inválido"`.

### 📤 8. Save Cleaned Data

- Saves final DataFrame to `clientes_remove_outliers.csv`.

---

## 📌 `inconsistencia.py`

### 📄 Advanced Cleaning and Personal Data Sanitization

Handles deeper inconsistencies and applies anonymization to personal data.

### 🧹 1. Load Initial Data

- Loads `clientes.csv` and adjusts display settings.

### 🕵️‍♂️ 2. Personal Data Masking

- Masks CPF as `123.***.***-45`.
- Short or missing CPFs become `"CPF inválido"`.

### 📅 3. Date Correction

- Converts dates to `datetime`.
- Replaces future dates with `1900-01-01`.
- Calculates adjusted age.
- Invalid ages (`>100`) become `NaN`.

### 🏘️ 4. Address Extraction

- Splits address field by line breaks:
  - Line 1 → street
  - Line 2 → neighborhood
  - Last part after `' / '` → state
- Invalid if too short/long.

### 📌 5. State Validation

- Converts to uppercase and trims.
- Retains only valid Brazilian states.
- Others become `"Desconhecido"`.

### 🔁 6. Final Substitutions

- Replaces original fields (`cpf`, `idade`, `endereco`, `estado`) with cleaned versions.
- Selects only relevant columns for final DataFrame.

### 💾 7. Export Final Version

- Saves to `clientes_tratados.csv`.
- Reads back the CSV for confirmation.

---

## ✅ Summary

These scripts form a complete pipeline for real-world data preparation, covering:

- 🧼 Text and format cleaning
- 🔍 Null and outlier handling
- 📅 Date parsing and validation
- 🕵️‍♀️ Personal data anonymization
- 💾 Exporting clean, structured datasets ready for analysis or modeling
