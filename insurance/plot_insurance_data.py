import matplotlib.pyplot as plt 


class InsuranceDataVisualizer:
    def __init__(self, insurance_df):
        self.insurance_df = insurance_df 

    def plot_histogram(self):
        print(self.insurance_df)
        plt.hist(self.insurance_df)
        plt.show()