"""
    @File :   indian_state_census.py
    @Author : mukul
    @Date :   21-12-2021
"""
import pandas as pd


class IndianCensus:

    def load_indian_census_data(self, csv_file):
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
        dataframe = self.load_indian_census_data(csv_file)
        count_records = dataframe.shape[0]
        return count_records


if __name__ == '__main__':
    csv_data = IndianCensus()
    file_name = "indian_census_data.csv"
    print("No. Of Data", csv_data.count_number_of_records(file_name))
