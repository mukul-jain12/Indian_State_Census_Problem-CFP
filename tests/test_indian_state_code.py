import pytest
from indian_state_code import IndianStateCode


class TestCase:

    file_path = "../indian_state_code_data.csv"
    wrong_file_path = "../indian_state_code_data.txt"

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
