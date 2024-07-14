# -*- coding: utf-8 -*-
"""INPADOC_Data_Normalization_00_From_Web_of_Science_TXT_Rename_Files.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EWuM0Dh-PbvYhOcrh8Gq4ncvvzpiLpzd

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
"""

import os

# Path to the directory
directory = "/home/brow/Documents/Artigo_FAPESP_Protocolo/Exports_Web_of_Science/"

# Function to rename the files
def rename_files(directory):
    for filename in os.listdir(directory):
        if filename.startswith("savedrecs"):
            if filename == "savedrecs.txt":
                new_filename = "savedrecs_0.txt"
            else:
                new_filename = filename.replace("savedrecs ", "savedrecs_").replace("(", "").replace(")", "")

            # Full path of the old and new file
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)

            # Rename the file
            os.rename(old_file, new_file)
            print(f'Renamed: {old_file} to {new_file}')

# Call the function to rename the files
rename_files(directory)