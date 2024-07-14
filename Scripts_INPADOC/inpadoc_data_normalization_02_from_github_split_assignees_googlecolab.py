# -*- coding: utf-8 -*-
"""INPADOC_Data_Normalization_02_From_GitHub_Split_Assignees_GoogleColab.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15gxBBRdpd5Cyo0EjPsPQpsYlPL-hjLco

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

# About this Notebook:

1. **Import Necessary Modules:**
   - `pandas` for data manipulation.
   - `StringIO` for handling string data as file-like objects.
   - `files` from `google.colab` for file download functionality.

2. **Configure Pandas:**
   - Set the display option to show the full content of each column without truncating.

3. **Read Multiple CSV Files from GitHub:**
   - Define the base URL of the CSV files.
   - Read CSV files numbered from 0 to 18 and store them in a list of dataframes.

4. **Combine DataFrames:**
   - Concatenate all dataframes into a single dataframe.
   - Print the length of the combined dataframe and display the first few rows.

5. **Split and Reshape Data:**
   - Split the 'AE' column by the semicolon delimiter and create a new dataframe with split values in separate columns.
   - Join this new dataframe with the original dataframe to retain 'PN' and 'AE' columns.
   - Reshape the dataframe to get unique values from each column, dropping NaN values and the 'Coluna' column.

6. **Print Information and Sample Data:**
   - Print the length and count of unique values in the 'assignee_split' column.
   - Sort the dataframe by 'PN' and display a random sample of 10 rows.

7. **Save and Download the Final DataFrame:**
   - Define the folder name and file path for the output CSV.
   - Save the final dataframe to a CSV file.
   - Download the CSV file using Google Colab's file download functionality.

This script processes CSV files from a GitHub repository, performs data manipulation and reshaping, and finally saves and downloads the processed data as a CSV file.

# <center>Variables Dicionary</center>

|n   |Column|Non-Null |Count    |Dtype   |Description
|:---|:-----|--------:|:--------|:-------|:---------------
|1   |PN    |18298    |non-null |object  |Patent Number(s)
|2   |TI    |18298    |non-null |object  |Title
|3   |AU    |18175    |non-null |object  |Author
|4   |AE    |18298    |non-null |object  |Assignee(s)
|5   |GA    |18298    |non-null |object  |General Annotation
|6   |AB    |18297    |non-null |object  |Abstract
|7   |TF    |0        |non-null |float64 |Text Field
|8   |EA    |52       |non-null |object  |Equivalent Abstracts
|9   |DC    |18298    |non-null |object  |Derwent Class Code(s)
|10  |MC    |18298    |non-null |object  |Derwent Manual Code(s)
|11  |IP    |18298    |non-null |object  |International Patent Classification (IPC)
|12  |PD    |18298    |non-null |object  |Patent Details
|13  |AD    |18298    |non-null |object  |Addresses
|14  |FD    |7761     |non-null |object  |Funding Details
|15  |PI    |18298    |non-null |object  |Priority Application Information
|16  |DS    |8091     |non-null |object  |Designated States
|17  |FS    |99       |non-null |object  |Field of Search
|18  |CP    |10691    |non-null |object  |Cited Patents
|19  |CR    |8335     |non-null |object  |Cited References
|20  |DN    |11282    |non-null |object  |DCR Numbers (Derwent Citation Records)
|21  |MN    |2099     |non-null |object  |Markush Number
|22  |RI    |3169     |non-null |object  |Reference Identification Number
|23  |CI    |11120    |non-null |object  |Cited Inventors (or Context Information)
|24  |RG    |4597     |non-null |object  |Derwent Registry Numbers

# Code
"""

# @title Package Requires

# Import necessary modules
import pandas as pd
# Set the display option to show the full content of each column without truncating
pd.set_option('display.max_colwidth', None)
#pd.options.display.float_format = '{:,.2f}'.format
#import glob
#import os
from io import StringIO
from google.colab import files

# @title Get multiple csv files from github
#import requests
#import pandas as pd
#from io import StringIO

# Base URL of the CSV files
base_url = "https://raw.githubusercontent.com/andrelmfsantos/INPADOC-Data-Normalization/main/TXT_Web_of_Science_to_CSV/savedrecs_{}.csv"

# List to hold dataframes
dataframes = []

# Loop to read CSV files from 0 to 18
for i in range(19):
    url = base_url.format(i)
    df = pd.read_csv(url)
    dataframes.append(df)

# Combining all dataframes into one
combined_data = pd.concat(dataframes, ignore_index=True)

# Displaying the length of the combined dataframe
print(len(combined_data))

# Displaying the first few rows of the combined dataframe to understand its structure
combined_data.head(3)

# @title Split the column and create a new DataFrame with the split values

# Split the 'optimized_assignee' column by '|' and create a new DataFrame
new_df = combined_data['AE'].str.split(';', expand=True)
new_df.head(10)

# @title Join dataframes

# Create a new DataFrame with 'publication_number' and 'optimized_assignee' columns
new_df1 = combined_data[['PN','AE']]
# Join the new DataFrame with the split columns DataFrame
new_df1 = new_df1.join(new_df)
# Display the sample of joined DataFrame
new_df1.sample(5,random_state = 43)

# @title Get unique values from each column - with ID option

# Reshape the DataFrame to get unique values from each column with ID options
df_stacked = new_df1.melt(id_vars =['PN','AE'],var_name='Coluna', value_name='assignee_split')
# Drop rows with NaN values
df_stacked = df_stacked.dropna()#.drop_duplicates().dropna()

# Drop the 'Coluna' column
df_stacked.drop(['Coluna'], axis = 1, inplace = True)

print('Len Dataframe:',len(df_stacked.assignee_split))
# Print the count of unique values in 'assignee_split'
print('Unique Assignees:',len(df_stacked.assignee_split.unique()))
print("-----------------------")

# Sort the DataFrame by 'publication_number' and take a random sample of 10 rows
df_stacked.sort_values(by = ['PN'], ascending = False).sample(10, random_state = 43)

# @title Split the 'assignee_split' column and create new columns to individual and legal person
#import pandas as pd

# Function to split the 'assignee_split' column and create new columns
def split_assignee_column(df):
    # Extracting the 'assignee_name'
    df['assignee_name'] = df['assignee_split'].str.extract(r'^(.*?)\s*\(')

    # Extracting the 'assignee_abbreviation'
    df['assignee_abbreviation'] = df['assignee_split'].str.extract(r'\((.*?)-')

    # Extracting the 'assignee_individual_legal'
    df['assignee_individual_legal'] = df['assignee_split'].str.extract(r'\((.{5})(.*)\)')[1]

    return df

# Simulating the combined dataframe with the 'assignee_split' column
#data = {
#    'assignee_split': [
#        "ETERNIVAX BIOMEDICAL INC (ETER-Non-standard)",
#        "GENETECH PHARMA (GEN-Standard)",
#        "HEALTHY LIFE CORP (HL-Non-standard)"
#    ]
#}
#combined_data = pd.DataFrame(data)

# Applying the function to create new columns
df_stacked = split_assignee_column(df_stacked)

# Displaying the dataframe to show the result
df_stacked.head()

"""## Assignee terms
In the assignee column of a patent database, the following terms have specific meanings:

1. **C (Company)**: This indicates that the assignee of the patent is a company or a corporate entity. This means the rights to the patent are held by a business organization rather than an individual.

2. **Individual**: This indicates that the assignee is an individual person. The rights to the patent are held by a single inventor or a person rather than a corporation or organization.

3. **Non-standard**: This term is used for assignees that do not fit into the typical categories of companies, individuals, or recognized institutions. It may include various types of organizations or entities that do not conform to the standard classifications.

4. **Soviet Institute**: This specifically refers to research institutes or organizations that were part of the Soviet Union. These institutes were often involved in scientific research and development and were common assignees for patents filed during the era of the Soviet Union.

These terms help categorize the ownership of patents and provide insight into who holds the rights to the inventions.
"""

# @title Count individual and legal person
df_stacked.groupby('assignee_individual_legal').size().reset_index(name='count')

# @title Download the csv file

# Define folder name and file path
folder_name = 'Assignees_Splits_with_Publications_Numbers_Notebook_02_From_GitHub_Split_Assignees'
file_path = f'{folder_name}.csv'

# Save the final DataFrame to a CSV file
df_stacked.to_csv(file_path, index=False)

# Download the CSV file
files.download(file_path)