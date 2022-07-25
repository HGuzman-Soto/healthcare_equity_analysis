import pandas as pd 
from collections import Counter 

class DataLoaderInsurance:
    def __init__(self, pathToInsuranceData):
        self.pathToInsuranceData = pathToInsuranceData

    def load_data(self):
        self.insurance_df = pd.read_csv(self.pathToInsuranceData)
    

    #https://pandas.pydata.org/pandas-docs/dev/getting_started/intro_tutorials/06_calculate_statistics.html
    def get_summary_stats(self):
        #return only numerical data
        #todo - improve summary statistics
        summary_df = self.insurance_df.drop(columns=["sex", "smoker", "region"])
        for col_name in list(summary_df):
            print("mean of {}: {}".format(col_name, summary_df[col_name].mean()))
            print("median of {}: {}\n".format(col_name, summary_df[col_name].median()))

    def get_numerical_cols(self):
        numerical_cols = self.insurance_df.drop(columns=["sex", "smoker", "region"])
        return numerical_cols

    
    def convert_cat_cols(self):
        cat_df = self.insurance_df.filter(['sex', 'smoker', 'region'])
        for col_name in list(cat_df):
            new_data = dict(Counter(self.insurance_df[col_name].values))
            #convert new_data into a dataframe and return 