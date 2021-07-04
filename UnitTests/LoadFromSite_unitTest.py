import unittest
from Helper.LoadFromSiteHelper import get_All_Covid_Cases , get_HistoryRecoverd_ByAllCountries

class TestApiSiteResponse(unittest.TestCase):
    def test_API_Cses(self):
        res = get_All_Covid_Cases()
        self.assertTrue(len(res) == 196, f'expected to have 196 records, return {len(res)}')

    def test_API_Recovered(self):
        res = get_HistoryRecoverd_ByAllCountries()
        self.assertTrue(len(res) == 196, f'expected to have 196 records, return {len(res)}')


if __name__ == '__main__':
    unittest.main()
