## Jonathan Vazquez
## db_io.py
##
## Desc: Functions to interact with online database
## Note: Database is 7 col table => User | Oldest | Msg0 | Msg1 | Msg2 | Msg3 | Msg4

import mysql.connector
from mysql.connector import Error


class Database():
    ## This block is used to see if a connection can be made
    def __init__(self) -> None:
        try:
            self.connection = mysql.connector.connect(host='golfpapaindigo-1.cbfyzw2jj1pn.us-west-2.rds.amazonaws.com',
                                                  database ='GPTGivesPsychEval',
                                                  user='Gorroa691',
                                                  password='FunGpTEval')
            if self.connection.is_connected():
                self.db_Info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", self.db_Info)
                self.cursor = self.connection.cursor()
                self.cursor.execute("select database();")
                self.record = self.cursor.fetchone()
                print("You're connected to database: ", self.record)
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if self.connection.is_connected():
                self.cursor.close()
                self.connection.close()
                print("MySQL connection is closed")

    ## Func used to connect to database
    ## TODO Check if you can just use open() or connection.connect()
    def connect(self):
        try:
            self.connection = mysql.connector.connect(host='golfpapaindigo-1.cbfyzw2jj1pn.us-west-2.rds.amazonaws.com',
                                                  database ='GPTGivesPsychEval',
                                                  user='Gorroa691',
                                                  password='FunGpTEval')
            if self.connection.is_connected():
                self.db_Info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", self.db_Info)
                self.cursor = self.connection.cursor()
                self.cursor.execute("select database();")
                self.record = self.cursor.fetchone()
                print("You're connected to database: ", self.record)
        except Error as e:
            print("Error while connecting to MySQL", e)
    
    ## Func used to disconnect from database
    ## Do not want to leave left over connections
    def disconnect(self):
        if self.connection.is_connected():
                self.cursor.close()
                self.connection.close()
                print("MySQL connection is closed")



    ## TODO Make db calls and append to string
    def get_data(self, username):
        self.connect()
        gpt_input = 'Give me a psych eval based on someone that talks in the following way.\n'

        if(self.user_in_table(username)):



        self.disconnect()
        return gpt_input

    ## TODO Make db calls to save message to db
    def add_message(self, user, message):
        return

    ## TODO Func that checks whether the user is already in the table
    def user_in_table(self, username):
        self.connect()
        sql_query = "select username from msg_table where username = %s"
        
        self.cursor.execute(sql_query, (username))
        result = self.cursor.fetchall()

        if (len(result) > 0):
            return True

        return False


        
