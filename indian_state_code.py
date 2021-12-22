"""
    @File :   indian_state_code.py
    @Author : mukul
    @Date :   22-12-2021
"""
import pandas as pd


class IndianStateCode:

    def load_indian_census_data(self, csv_file):
        """
            desc: load data of file
            return: dataframe
        """
        dataframe = pd.read_csv(csv_file, encoding='unicode_escape')
        return dataframe


csv_data = IndianStateCode()
file_name = "indian_state_code_data.csv"

print(csv_data.load_indian_census_data(file_name))
