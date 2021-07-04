import unittest
from BusinessLogic.CovidRecovered import MostRecoveredObj, sortMyRecoveredList


class MyCovidRecovery_TC(unittest.TestCase):
    def test_sorting(self):
    #Test check that list sorted work as expected
    #1. Fake list with Desc order
    #2. Fake record and check if record should be added to list or not
    #3. expected results - list should be added to expectedList[2] and last record Albania should be removed.

        #region Data Preperation">
        fakeList2sort = []
        fakeList2sort.append(MostRecoveredObj('Argentina', 169773))
        fakeList2sort.append(MostRecoveredObj('Afghanistan', 6598))
        fakeList2sort.append(MostRecoveredObj('Algeria', 2370))
        fakeList2sort.append(MostRecoveredObj('Angola', 1053))
        fakeList2sort.append(MostRecoveredObj('Albania', 63))

        fakeCandidateRecord = MostRecoveredObj('Israel', 5000)


        expectedList = []
        expectedList.append(MostRecoveredObj('Argentina', 169773))
        expectedList.append(MostRecoveredObj('Afghanistan', 6598))
        expectedList.append(MostRecoveredObj('Israel', 5000))
        expectedList.append(MostRecoveredObj('Algeria', 2370))
        expectedList.append(MostRecoveredObj('Angola', 1053))
        #endregion

        sortRes = sortMyRecoveredList(fakeList2sort,fakeCandidateRecord )

        #region Check assertion
        i=0
        for item in sortRes:
            if expectedList[i].countryname == item.countryname and expectedList[i].val == item.val:
                i += 1
            else:
                self.assertEqual(expectedList[i].countryname, item.countryname,
                                 f'Country {item.countryname} should not be part of final sorting list')
                self.assertEqual(expectedList[i].val, item.val,
                                 f'Value {item.val} for {item.countryname} should not be part of final sorting list')
        #endregion


if __name__ == '__main__':
    unittest.main()
