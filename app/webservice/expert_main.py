from app.webservice import forward_inf as inf
from app.webservice import blackboard as blackboard
from app.webservice import conn_sql as conn

# connect = conn.database('127.0.0.1', 'root', '', 'expert_system')
# connect = connect.get_conn()
# cr_0 = connect.cursor()

# data = input('Enter fact: ')
# fact = str(data)
# inf.inference(fact).forward_()
# print((blackboard.bb_manage.unique(blackboard.bb_manage.get_fact_bb(blackboard.bb))))
# print((blackboard.bb_manage.unique(blackboard.bb_manage.get_fact_bb(blackboard.no_bb))))
# print((blackboard.bb_manage.unique(blackboard.bb_manage.get_fact_bb(blackboard.ask_arr))))

# ask = input("%s%s" % (blackboard.bb_manage.get_factname(blackboard.ask_arr[0]) ," is true by check BB?(y/n):"))
# print((blackboard.bb_manage.unique(blackboard.bb_manage.get_fact_bb(blackboard.no_bb))))
# if ask == "n":
#     blackboard.no_bb.append(blackboard.ask_arr[0])
# else:
#     blackboard.bb.append(blackboard.ask_arr[0])
# blackboard.ask_arr = []
# inf.inference(fact).forward_()


# ter=[]
# sql = 'SELECT fact_id FROM fact_data WHERE terminal_id="1"'
# cr_0.execute(sql)
# for terminal in cr_0.fetchall():
#     if terminal[0] < 10:
#         ter_0 = ("%s%s" % ("00000", terminal[0]))
#     elif terminal[0] >= 10 and terminal[0] <= 99:
#         ter_0 = ("%s%s" % ("0000", terminal[0]))
#     elif terminal[0] >= 100 and terminal[0] <= 999:
#         ter_0 = ("%s%s" % ("000", terminal[0]))
#     elif terminal[0] >= 1000 and terminal[0] <= 9999:
#         ter_0 = ("%s%s" % ("00", terminal[0]))
#     elif terminal[0] >= 10000 and terminal[0] <= 99999:
#         ter_0 = ("%s%s" % ("0", terminal[0]))
#     else:
#         ter_0 = terminal[0]
#     if (ter_0 in blackboard.bb):
#         ter.append(blackboard.bb.index(ter_0))
# i = ["A","B","C"]

# print(blackboard.bb_manage.get_fact_id(i))
