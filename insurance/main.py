from load_insurance_data import DataLoaderInsurance
from plot_insurance_data import InsuranceDataVisualizer
import pandas as pd 

def main():
    insurance_data = DataLoaderInsurance("insurance.csv")
    insurance_data.load_data()
    insurance_data.get_summary_stats()
    insurance_data_numerical_copy_df = insurance_data.get_numerical_cols()
    insurance_data.convert_cat_cols()

    data_visualizer = InsuranceDataVisualizer(insurance_data_numerical_copy_df)
    data_visualizer.plot_histogram()


#The script function does the same thing
def script():
    insurance_df = pd.read_csv("insurance.csv")
    print(insurance_df)

main()