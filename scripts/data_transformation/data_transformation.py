import os
import glob
import numpy as np
import pandas as pd
import csv
from tqdm import tqdm

class DataTransformation(object):
  
  def transform(path):
    header = ["TIPREG", "DATA", "CODBDI", "CODNEG", "TPMERC",
              "NOMRES", "ESPECI", "PRAZOT", "MODREF", "PREABE",
              "PREMAX", "PREMIN", "PREMED", "PREULT", "PREOFC",
              "PREOFV", "TOTNEG", "QUATOT", "VOLTOT", "PREEXE",
              "INDOPC", "DATAEN", "FATCOT", "PTOEXE", "CODISI",
              "DISMES"]
    registro = [1, 3, 11, 13, 25, 28, 40, 50,
                53, 57, 70, 83, 96, 109, 122, 135,
                148, 153, 171, 189, 202, 203, 211,
                218, 231, 243, 246]

    # print("entrou aqui")
    # import pdb; pdb.set_trace()
    for filename in tqdm(glob.glob(path + "*.TXT")):
      with open("../data/ibovespa_csv/" + '{}.csv'.format(os.path.basename(filename)), mode='a') as data_file:
        csv_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        csv_writer.writerow(header)

        file = open(filename,"r", errors="replace")
        tqdm.write(filename)

        for i, line in enumerate(file):
          row = []
          if i != 0:
            for j in range(len(registro)-1):
              row.append(line[(registro[j]-1):(registro[j+1]-1)].strip())

            csv_writer.writerow(row)
          
        data_file.close()

DataTransformation.transform("../data/ibovespa/")
