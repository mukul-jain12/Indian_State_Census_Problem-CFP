
import pytest
from indian_state_census import IndianCensus
from indian_census_exception import IndianCensusException


class TestCase:

    file_name = "../indian_census_data.csv"

    @pytest.fixture()
    def indian_census(self):
        csv_data = IndianCensus()
        return csv_data

    def test_match_number_of_rows(self, indian_census):
        """
            desc: test the method to count number of records in file
        """
        result = indian_census.count_number_of_records(self.file_name)
        assert result == 29

