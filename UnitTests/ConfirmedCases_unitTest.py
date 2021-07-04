import unittest
from BusinessLogic.ConfirmedCases import calc_CasesPer100kms,avgConfirmedObj


class MyConfirmed_TC(unittest.TestCase):
    def test_SKM_values(self):
        #
        fakeList2sort = []
        fakeList2sort.append(avgConfirmedObj('Afghanistan',120216,652090))
        fakeList2sort.append(avgConfirmedObj('Albania', 132534, 28748))
        fakeList2sort.append(avgConfirmedObj('Algeria', 141007, 2381741))
        fakeList2sort.append(avgConfirmedObj('Andorra', 13918, 468))

        expectedRes='Afghanistan:  18 cases/100[skm]\nAlbania:  461 cases/100[skm]\nAlgeria:  6 cases/100[skm]\nAndorra:  2974 cases/100[skm]'

        res = calc_CasesPer100kms(fakeList2sort)

        self.assertEqual(expectedRes,res,"expected response from calc_CasesPer100kms was incorect")



if __name__ == '__main__':
    unittest.main()
