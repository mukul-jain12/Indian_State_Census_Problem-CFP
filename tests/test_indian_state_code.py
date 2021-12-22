import pytest
from indian_state_code import IndianStateCode
from indian_census_exception import IndianCensusException


class TestCase:
    file_path = "../indian_state_code_data.csv"
    wrong_file_extension = "../indian_state_code_data.txt"

    @pytest.fixture()
    def state_code(self):
        state_code = IndianStateCode()
        return state_code

    def test_match_number_of_rows(self, state_code):
        """
            desc: test the method to count number of records in file
        """
        expected = 37
        result = state_code.count_number_of_records(self.file_path)
        assert result == expected

    def test_match_file_path(self, state_code):
        """
            desc: test the method to check file extension
        """
        expected = self.file_path
        result = state_code.check_file_extension(self.file_path)
        assert result == expected

    def test_not_match_file_path(self, state_code):
        """
            desc: test the method to raise exception while checking file extension
        """
        expected = "File is Invalid"
        with pytest.raises(IndianCensusException) as exception:
            state_code.check_file_extension(self.wrong_file_extension)
        assert exception.value.message == expected

    def test_match_delimiter(self, state_code):
        """
            desc: test the method to check delimiter
        """
        expected = ','
        result = state_code.delimiter_validation(self.file_path)
        assert result == expected

    def test_not_match_delimiter(self, state_code):
        """
            desc: test the method to raise exception while checking delimiter
        """
        expected = "Error occurred in delimiter matching"
        with pytest.raises(IndianCensusException) as exception:
            state_code.delimiter_validation(self.wrong_file_extension)
        assert exception.value.message == expected

    def test_match_header(self, state_code):
        """
            desc: test the method to check header
        """
        expected = True
        result = state_code.validate_header(self.file_path)
        assert result == expected

    def test_not_match_header(self, state_code):
        """
            desc: test the method to raise exception while checking headers
        """
        expected = "Heading is corrupted"
        with pytest.raises(IndianCensusException) as exception:
            state_code.validate_header(self.wrong_file_extension)
        assert exception.value.message == expected
