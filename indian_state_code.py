"""
    @File :   indian_state_code.py
    @Author : mukul
    @Date :   22-12-2021
"""
import pandas as pd


class IndianStateCode:

    def load_indian_state_code_data(self, csv_file):
        """
            desc: load data of file
            return: dataframe
        """
        dataframe = pd.read_csv(csv_file)
        return dataframe

    def count_number_of_records(self, csv_file):
        """
            desc: count total number of rows
            return: count_records
        """
        dataframe = self.load_indian_state_code_data(csv_file)
        count_records = dataframe.shape[0]
        return count_records


if __name__ == "__main__":
    csv_data = IndianStateCode()
    file_name = "indian_state_code_data.csv"

    print(csv_data.count_number_of_records(file_name))
