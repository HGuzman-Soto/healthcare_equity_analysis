import pandas as pd 


#TODO - Add step to automatically download, and unzip files 
# conver them to csv 
def read_sas_file(filePath):
    df = pd.read_sas(filePath)
    print(list(df))

read_sas_file("hhpub18early_18par.sas7bdat")