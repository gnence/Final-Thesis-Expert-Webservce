import mysql.connector as conDB

class connectDB:

    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.connection = self.conn()

    def conn(self):
        con = None
        try:
            con = conDB.connect(user=self.username, password=self.password, host=self.host, database=self.database)
        except ConnectionError :
            print(ConnectionError.args)
        finally:
            return con

    def displayData(self):
        print("Host : {} \nUsername : {} \nDatabase : {}".format(self.host, self.username, self.database))

    def getInfoDB(self):
        return self.host

    def getConnection(self):
        return self.connection

    def closeConnection(self):
        self.connection.close()