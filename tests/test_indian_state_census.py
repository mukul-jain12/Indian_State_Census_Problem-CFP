
import pytest
from indian_state_census import IndianCensus
from indian_census_exception import IndianCensusException


class TestCase:
    file_path = "../indian_census_data.csv"
    wrong_file_extension = "../indian_census_data.txt"

    @pytest.fixture()
    def indian_census(self):
        csv_data = IndianCensus()
        return csv_data

    def test_match_number_of_rows(self, indian_census):
        """
            desc: test the method to count number of records in file
        """
        expected = 29
        result = indian_census.count_number_of_records(self.file_path)
        assert result == expected

    def test_match_file_path(self, indian_census):
        """
            desc: test the method to check file extension
        """
        expected = self.file_path
        result = indian_census.check_file_extension(self.file_path)
        assert result == expected

    def test_not_match_file_path(self, indian_census):
        """
            desc: test the method to raise exception while checking file extension
        """
        expected = "File is Invalid"
        with pytest.raises(IndianCensusException) as exception:
            indian_census.check_file_extension(self.wrong_file_extension)
        assert exception.value.message == expected

    def test_match_delimiter(self, indian_census):
        """
            desc: test the method to check delimiter
        """
        expected = ','
        result = indian_census.delimiter_validation(self.file_path)
        assert result == expected

    def test_not_match_delimiter(self, indian_census):
        """
            desc: test the method to raise exception while checking delimiter
        """
        expected = "Error occurred in delimiter matching"
        with pytest.raises(IndianCensusException) as exception:
            indian_census.delimiter_validation(self.wrong_file_extension)
        assert exception.value.message == expected

    def test_match_header(self, indian_census):
        """
            desc: test the method to check header
        """
        expected = True
        result = indian_census.validate_header(self.file_path)
        assert result == expected

    def test_not_match_header(self, indian_census):
        """
            desc: test the method to raise exception while checking headers
        """
        expected = "Heading is corrupted"
        with pytest.raises(IndianCensusException) as exception:
            indian_census.validate_header(self.wrong_file_extension)
        assert exception.value.message == expected
