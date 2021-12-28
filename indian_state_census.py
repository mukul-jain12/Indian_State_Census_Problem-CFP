"""
    @File :   indian_state_census.py
    @Author : mukul
    @Date :   21-12-2021
"""
import csv
import pandas as pd
from indian_census_exception import IndianCensusException
import logging

logging.basicConfig(filename='state_census_analyser.log', filemode='a', level=logging.DEBUG, format='%(levelname)s :: %(name)s :: %(asctime)s :: %(message)s')


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
        logging.info("Load Indian Census Data")

        dataframe = self.load_indian_census_data(csv_file)
        count_records = dataframe.shape[0]

        logging.info("Data Loaded Completely")
        logging.debug("Number of records are :{}".format(count_records))

        return count_records

    def check_file_extension(self, csv_name):
        """
            desc: check file extension
            return: file name
        """
        if csv_name.endswith(".csv"):
            return csv_name
        else:
            raise IndianCensusException("File is Invalid")

    def delimiter_validation(self, csv_file):
        with open(csv_file, newline="") as file_data:
            dialect = csv.Sniffer().sniff(file_data.read())
            if not dialect.delimiter == ';':
                raise IndianCensusException("Error occurred in delimiter matching")
            else:
                return dialect.delimiter

    def validate_header(self, csv_file):
        with open(csv_file, newline="") as file_data:
            dialect = csv.Sniffer().has_header(file_data.read())
            if not dialect:
                raise IndianCensusException("Heading is corrupted")
            else:
                return dialect


if __name__ == '__main__':
    csv_data = IndianCensus()
    file_name = "indian_census_data.csv"

    print("No. Of Data :", csv_data.count_number_of_records(file_name))

    try:
        print("Name of file is :", csv_data.check_file_extension(file_name))
    except IndianCensusException as exception:
        logging.warning("File extension is not valid")
        print(exception.__str__())

    try:
        print("Delimiter is :", csv_data.delimiter_validation(file_name))
    except IndianCensusException as ex:
        logging.error("Delimiter is Invalid")
        print(ex.__str__())

    try:
        print("Is Header Correct? :", csv_data.validate_header(file_name))
    except IndianCensusException as ex:
        logging.exception("Header is Incorrect")
        print(ex.__str__())
