import mysql.connector
import pandas as pd
def insert_varibles_into_bi_data_details( accountId, analyticTypeValue,cameraName, cameraDate, cameraHour, countType, count, countId, arrivalTime, departureTime,
                                         totalTime, image, createdTime,createdId, ProgramName, remarks):
    try:
        connection = mysql.connector.connect(host='ussitemanager.iviscloud.net',###You dirty fellow this is live db link
                                             database='ivigil_crm',
                                             user='opdb_rw',
                                             password='testdbpw')
        # print("Database connected Successfully")
        cursor = connection.cursor()
        sql = "SELECT id FROM bi_data b WHERE b.accountId="+str(accountId)+" AND analyticTypeValue="+"'"+str(analyticTypeValue)+"'"
        print("sql",sql)
        cursor.execute(sql)
        selectResult = cursor.fetchall()
        print("myresult",  selectResult)
        df = pd.DataFrame( selectResult,
                          columns=['id'])
        print(df)
        Id = list(df['id'])
        BI_data_id=Id[0]
        mySql_insert_query = """INSERT INTO bi_data_details ( BI_data_id,cameraName, cameraDate, cameraHour, countType, count, countId, arrivalTime, departureTime,
                                         totalTime, image, createdTime,createdId, ProgramName, remarks)
                                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        record = ( BI_data_id,cameraName, cameraDate, cameraHour, countType, count, countId, arrivalTime, departureTime,
                                         totalTime, image, createdTime,createdId, ProgramName, remarks)
        # print('sql', mySql_insert_query)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into PersonDetails table")
        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection is closed")

# insert_varibles_into_bi_data_details(1016,'1','cameraName1','cameradate1','camerahour1',"enter",'enter',0,00,00,00,"noImage",'time',4305,"finalBharbeePharmacyCode","peopleCount")
