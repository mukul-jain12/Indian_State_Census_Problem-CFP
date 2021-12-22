"""
    @File :   indian_census_exception
    @Author : mukul
    @Date :   21-12-2021
"""


class IndianCensusException(Exception):
    """
        desc: catch raised exception message
    """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
