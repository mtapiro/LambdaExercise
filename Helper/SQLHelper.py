import pyodbc


def Open_SQL_InsertRecords(topX_countries):

    try:
        TruncateOldData()

        for item in topX_countries:
            sqlServerName = "dbm-Controller3"
            DBname = "Covid19DB"
            conn = pyodbc.connect('Driver={SQL Server};'
                                  'Server=dbm-Controller3;'
                                  'Database=Covid19DB;'
                                  'Trusted_Connection=yes;')
            cursor = conn.cursor()
            cursor.execute(f'''
                            INSERT INTO Covid19DB.dbo.topRecoveryCountries (CountryName, measure)
                            VALUES
                            ('{item.countryname}','{item.val}')
                            ''')
            conn.commit()

    except:
        print("Oops.. something bad happened while execution Open_SQL_InsertRecords method")

def TruncateOldData():
    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                                'Server=dbm-Controller3;'
                                'Database=Covid19DB;'
                                'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute(f'''
                        DELETE From Covid19DB.dbo.topRecoveryCountries
                        ''')
        conn.commit()

    except:
        print("Oops.. something bad happened while Deleting OLD data.")
