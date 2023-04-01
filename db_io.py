## Jonathan Vazquez
## db_io.py
##
## Desc: Functions to interact with online database
## Note: Database is 7 col table => User | Oldest | Msg0 | Msg1 | Msg2 | Msg3 | Msg4

import mysql.connector
from mysql.connector import Error

import os
from dotenv import load_dotenv


class Database():
    ## This block is used to see if a connection can be made
    def __init__(self) -> None:
        try:
            load_dotenv()
            self.host = str(os.getenv('DBHOST'))
            self.database = str(os.getenv('DBNAME'))
            self.user = str(os.getenv('DBUSER'))
            self.password = str(os.getenv('DBPASS'))            
            self.connection = mysql.connector.connect(host=self.host,
                                                  database =self.database,
                                                  user=self.user,
                                                  password=self.password)
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
            self.connection = mysql.connector.connect(host=self.host,
                                                  database =self.database,
                                                  user=self.user,
                                                  password=self.password)
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


    ## Get user's row from database
    ## Note: this will only be called if already connected so do not connect/disconnect
    def get_user_row(self, userid):
        result = []

        ## Make sure user is in table
        if(not self.user_in_table(userid)):
            raise Exception('User not in table')

        try:
            sql_query = "select * from msg_table where userid = %s"
            self.cursor.execute(sql_query, [userid])
            result = self.cursor.fetchone()
        except mysql.connector.Error as error:
            print("Failed to get record from MySQL table at get_user_row(): {}".format(error))

        return result

    ## Make db calls to save message to db
    def add_message(self, userid, message):
        self.connect()

        sql_query = ''
        oldest = 0
        
        try:
            ## User not in table so add them and their message
            if (not self.user_in_table(userid)):
                sql_query = 'insert into msg_table (userid, oldest, msg1) values(%s, %s, %s)'
                ## This is brand new so the oldest is itself 
                self.cursor.execute(sql_query, [userid, 1, message])
                self.connection.commit()
                print(self.cursor.rowcount, "User inserted successfully into msg_table")
            ## User in table so get oldest and then add
            else:
                oldest = int(self.get_user_row(userid)[1]) 

                ## Last entry in table so go back
                if (oldest == 5):
                    oldest = 1
                    sql_query = 'update msg_table set msg1 = %s, oldest = %s where userid = %s'
                else:
                    ## oldest is now the current string
                    oldest = oldest + 1
                    ## I regret storing oldest as 0-4 and msgs as msg1-5
                    sql_query = 'update msg_table set msg'+str(oldest)+' = %s, oldest = %s where userid = %s'

                self.cursor.execute(sql_query, [message, oldest, userid])
                self.connection.commit()
                print("msg_table updated successfully ")

        except mysql.connector.Error as error:
            print("Failed to update table record at add_message(): {}".format(error))


        self.disconnect()
        return

    ## Func that checks whether the user is already in the table
    ## Note: this will only be called if already connected so do not connect/disconnect
    def user_in_table(self, userid):
        ## Parameratize incase someone uses a "weird" userid lol
        sql_query = "select userid from msg_table where userid = %s"
        
        try:
            self.cursor.execute(sql_query, [userid])
            result = self.cursor.fetchone()
        except mysql.connector.Error as error:
            print("Failed to get record from MySQL table at user_in_table(): {}".format(error))

        if (result != None):
            return True

        return False

    def get_gptin(self, userid):
        self.connect()
        gpt_input = "Give me a psych eval based on someone that talks in the following way.\n"
        row = self.get_user_row(userid)
        msgs = row[2:]

        ## Go through all the messages even when it says none
        for i in range(5):
            if(msgs[i] != None):
                gpt_input = gpt_input + msgs[i] + "\n"

        self.disconnect()
        return gpt_input
        
