from app.webservice import conn_sql as conn
from app.webservice import blackboard as blackboard
from app import cr_0

f_wait = []
class inference:

    def __init__(self,fact):
        self.fact = fact
        self.fact_all2 = []
        self.fact_all = []

    def forward_(self):
        # print("%s%s" % ("Fact Input = ",self.fact))
        self.fact_all = self.find_fact()
        self.ch_digit()
        end = blackboard.bb_manage.input_bb(self.fact_all2)
        blackboard.bb = blackboard.bb_manage.unique(blackboard.bb)
        # print("%s%s" % ("             BB = ", (blackboard.bb_manage.get_fact_bb(blackboard.bb))))
        if end == "end":
            return "end"
        else:

            if len(self.fact_all2) < 1:
                return blackboard.bb
            else:
                for f in self.fact_all2:
                    if_all = self.find_if(f)
                    if len(if_all) > 0 :
                        for f_all in if_all:
                            end = self.find_and(f_all)
                            if end == "end":
                                return "end"
                    else:
                        return
        return

    def find_fact(self):
        arr = []
        sql = ('SELECT {} FROM {} WHERE {}'.format('fact_id', 'fact_data', 'fact_name=\'{}\''.format(self.fact)))
        cr_0.execute(sql)
        for fact_all in cr_0.fetchall():
            arr.append(fact_all)
        if arr is None:
            return arr
        return arr

    def find_if(self,f):
        ret_arr =[]
        sql2 = ('SELECT {} FROM {} WHERE {} LIKE {} '.format('*', 'rule_data', 'part_if', '\'%{}%\''.format(str(f))))
        cr_0.execute(sql2)
        for if_ in cr_0.fetchall():
            ret_arr.append("%s%s%s%s%s" % (if_[0],"*",if_[2],"*",if_[3]))
        return  ret_arr

    def find_and(self, if_all):
        if_all = if_all.split('*')
        rule_id = if_all[0]
        part_if = if_all[1]
        part_then = if_all[2]
        if ((part_if).find(',') > -1):
            end = blackboard.bb_manage.check_bb(part_if,rule_id,part_then)
            if end == "end":
                return "end"
        else:
            blackboard.bb_manage.input_bb_str(part_then)
            end = blackboard.bb_manage.recv_fact(part_then)
            if end == "end":
                return "end"
        return

    def ch_digit(self):
        for i in self.fact_all:
            if i[0] < 10:
                self.fact_all2.append("%s%s" % ("00000",i[0]))
            elif i[0] >= 10 and i[0] < 99:
                self.fact_all2.append("%s%s" % ("0000",i[0]))
            elif i[0] >= 100 and i[0] < 999:
                self.fact_all2.append("%s%s" % ("000",i[0]))
            elif i[0] >= 1000 and i[0] < 9999:
                self.fact_all2.append("%s%s" % ("00",i[0]))
            elif i[0] >= 10000 and i[0] < 99999:
                self.fact_all2.append("%s%s" % ("0",i[0]))
            else: self.fact_all2.append(i[0])
        return



