import mysql.connector as conn
class database:

    def __init__(self,host,username,password,dbname):
        self.host = host
        self.username = username
        self.password = password
        self.dbname = dbname
        self.connection = self.conn_sql()

    def get_conn(self):
        return self.connection

    def close_conn(self):
        self.connection.close()

    def conn_sql(self):
        try:
            connection = conn.connect(host=self.host,
                                      user=self.username,
                                      password=self.password,
                                      database=self.dbname)
        except conn.Error as err:
            print(err)
            return 0
        return connection



#
# host = '127.0.0.1'
# username = 'root'
# password = 'test'
# dbname = 'expert_system'
#
# connection = conn.connect(host=host,
#                           user=username,
#                           password=password,
#                           database=dbname)
#
# cur = connection.cursor()
# query = ('delete from {} where {}'.format('rule_data','user_id = 0'))
# cur.execute(query)
# connection.commit()
#
# print(cur)
