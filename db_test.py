

import mysql.connector
from mysql.connector import Error


try:
    connection = mysql.connector.connect(host='golfpapaindigo-1.cbfyzw2jj1pn.us-west-2.rds.amazonaws.com',
                                        database ='GPTGivesPsychEval',
                                        user='Gorroa691',
                                        password='FunGpTEval')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()

        ## My tests
        cursor.execute('select * from msg_table')
        print(cursor.fetchall())

        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

