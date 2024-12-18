# -*- coding: utf-8 -*-
"""INPADOC_Data_Normalization_01_From_Web_of_Science_TXT_to_CSV_Download_GoogleColab.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UTPPkRrN3-wRU4THsLKAqgCz3rLzbJ8I

<pre>
<img align="center" width="900" src="https://raw.githubusercontent.com/andrelmfsantos/INPADOC-Data-Normalization/main/Images/FAPESP_Header_Google_Colab_english.png">
</pre>

> * __INPADOC: International Patent Documentation__
* [FAPESP Process Number: 23/12389-1](https://bv.fapesp.br/pt/auxilios/113767/solucoes-diagnosticas-e-terapeuticas-da-covid-19-protegidas-por-patentes-sistematizacao-das-principa/)

|   |   |
|--:|:--|
|**Authors:**|[Priscila Rezende da Costa](https://bv.fapesp.br/pt/pesquisador/67192/priscila-rezende-da-costa/) $-$ [Camila Naves Arantes](http://lattes.cnpq.br/3897204543440920) $-$ [Alex Fabianne de Paulo](http://lattes.cnpq.br/9690861410844635) $-$ </br> [Geciane Silveira Porto](https://bv.fapesp.br/pt/pesquisador/89388/geciane-silveira-porto/) $-$ [André Luis Marques Ferreira dos Santos](http://lattes.cnpq.br/9690861410844635) $-$ [Celise Marson](http://lattes.cnpq.br/2618279063609476)|
|**Host Institution:**|[Universidade Nove de Julho (UNINOVE). Campus Vergueiro. São Paulo , SP, Brasil](https://bv.fapesp.br/pt/instituicao/1496/campus-vergueiro/)|
|**Date:**|July 13, 2024|

**18,298 results from Derwent Innovations Index for:**

* Topic:

    * ("COVID*" OR "coronavirus disease 2019" OR "coronavirus pneumonia" OR "novel coronavirus disease" OR "COVID" OR "COVID disease" OR "COVID virus" OR "coronavirus pandemic" OR "SARS-CoV-2" OR "coronavirus 2" OR "novel coronavirus" OR "COVID virus" OR "sarsa" OR "Wuhan coronavirus")
* [Derwent $-$ Web of Science](https://www.webofscience.com/wos/diidw/summary/01631a4b-22fd-40a9-886c-e1087358711f-fb23bb19/diidw-relevance/1)
* Export: "Tab delimited file"
* Record Content: Full Record

**About this Notebook:**

1. Downloads text files from [GitHub](https://github.com/andrelmfsantos/INPADOC-Data-Normalization/tree/main/Exports_Web_of_Science).
2. Converts each file into a DataFrame.
3. Saves each DataFrame as a CSV file in the `TXT_Web_of_Science_to_CSV` folder.
4. Zips the folder containing the CSV files into a ZIP file.
5. Provides a download link for the ZIP file.
"""

import pandas as pd
import os
import requests

# Ensure the output directory exists
output_folder_path = 'TXT_Web_of_Science_to_CSV'
os.makedirs(output_folder_path, exist_ok=True)

# Base URL for the files on GitHub
base_url = 'https://raw.githubusercontent.com/andrelmfsantos/INPADOC-Data-Normalization/main/Exports_Web_of_Science/savedrecs_'

# Define column names
columns = ['PN', 'TI', 'AU', 'AE', 'GA', 'AB', 'TF', 'EA', 'DC', 'MC', 'IP', 'PD', 'AD', 'FD', 'PI', 'DS', 'FS', 'CP', 'CR', 'DN', 'MN', 'RI', 'CI', 'RG']

# Function to read a file from a URL and return a DataFrame
def read_file_to_dataframe(file_url):
    response = requests.get(file_url)
    response.raise_for_status()  # Ensure we notice bad responses
    lines = response.text.splitlines()
    if lines:
        lines[0] = lines[0].replace('\ufeff', '')  # Strip BOM character if present

        # Split lines by tab and create a list of dictionaries
        data = []
        for line in lines[1:]:  # Skip header line
            split_line = line.split('\t')
            entry = {col: split_line[i] if i < len(split_line) else None for i, col in enumerate(columns)}
            data.append(entry)

        # Create DataFrame
        df = pd.DataFrame(data, columns=columns)
        return df
    else:
        return pd.DataFrame(columns=columns)

# Read all files from 0 to 18 and save them as CSV
for i in range(19):
    file_url = f'{base_url}{i}.txt'
    try:
        df = read_file_to_dataframe(file_url)
        print(f'savedrecs_{i}.txt: {len(df)} rows')

        # Save DataFrame to CSV
        output_file_path = os.path.join(output_folder_path, f'savedrecs_{i}.csv')
        df.to_csv(output_file_path, index=False)
        print(f'Saved {output_file_path}')
    except requests.exceptions.RequestException as e:
        print(f'Failed to download {file_url}: {e}')

# Optionally, you can do further processing with the list of DataFrames
# For example, display the first few rows of each DataFrame
for i in range(19):
    output_file_path = os.path.join(output_folder_path, f'savedrecs_{i}.csv')
    if os.path.exists(output_file_path):
        df = pd.read_csv(output_file_path)
        print(f'DataFrame from savedrecs_{i}.csv head:')
        #print(df.head())

# Zip the folder containing CSV files
!zip -r TXT_Web_of_Science_to_CSV.zip TXT_Web_of_Science_to_CSV

# Provide a link to download the zipped folder
from google.colab import files
files.download('TXT_Web_of_Science_to_CSV.zip')