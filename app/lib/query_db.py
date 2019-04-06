import mysql.connector
class queryDB :

    def __init__(self, connection):
        self.conn = connection

    #Create Table
    def createTable(self, tableName, fieldPart):
        cur = self.conn.cursor()
        try :
            query = ('create table {}({})'.format(tableName, fieldPart))
            cur.execute(query)
        except mysql.connector.Error as err:
            print("Failed Create table: {}".format(err))
            return(0)
        finally :
            print(cur)
            cur.close()
        print('Create {} success.'.format(tableName))

    def dropTable(self, table):
        cur = self.conn.cursor()
        try:
            query = ('DROP table {}'.format(table))
            cur.execute(query)
        except mysql.connector.Error as err:
            print("Failed Drop table: {}".format(err))
            return(0)
        finally:
            print(cur)
            cur.close()
        print('Drop {} success.'.format(table))

    #Don't select function
    def queryAll(self,operation):
        cur = self.conn.cursor()
        try :
            cur.execute(operation)
            self.conn.commit()
        except mysql.connector.Error as err:
            print("Failed Query database: {}".format(err))
            return(0)
        finally :
            #result = cur.fetchall()
            print(cur)
            cur.close()
        print('{} is success.'.format(operation))

    #Use SQL select
    def querySelect(self, selectPart, fromPart, wherePart):
        cur = self.conn.cursor()
        try :
            query = ('select {} from {} where {}'.format(selectPart, fromPart, wherePart))
            cur.execute(query)
        except mysql.connector.Error as err:
            print("Failed Select database: {}".format(err))
            return(0)
        finally:
            result = cur.fetchall()
            cur.close()
        return result

    #Use SQL insert
    def queryInsert(self, table, valueTaget, newValue):
        cur = self.conn.cursor()
        try :
            query = ('insert into {}({}) values({})'.format(table, valueTaget, newValue))
            cur.execute(query)
            self.conn.commit()
        except mysql.connector.Error as err:
            print("Failed Insert database: {}".format(err))
            return(0)
        finally :
            print(cur)
            cur.close()
        print('Insert in {} success.'.format(table))

    #Use SQL delect
    def queryDelect(self, table, wherePart):
        cur = self.conn.cursor()
        try :
            query = ('delete from {} where {}'.format(table, wherePart))
            cur.execute(query)
            self.conn.commit()
        except mysql.connector.Error as err:
            print("Failed Delete database: {}".format(err))
            return(0)
        finally :
            print(cur)
            cur.close()
        print('Delect in {} success.'.format(table))

    #Use SQL Update
    def queryUpdate(self, table, setPart, wherePart):
        cur = self.conn.cursor()
        try :
            query = ('update {} set {} where {}'.format(table, setPart, wherePart))
            cur.execute(query)
            self.conn.commit()
        except mysql.connector.Error as err:
            print("Failed Update database: {}".format(err))
            return(0)
        finally :
            print(cur)
            cur.close()
        print('Update in {} success.'.format(table))

    #Close connection
    def closeConnect(self):
        self.conn.close()