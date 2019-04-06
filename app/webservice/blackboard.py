from app.webservice import conn_sql as conn
from app.webservice import blackboard as blackboard
from app.webservice import forward_inf as inf
from app import cr_0

bb = []
no_bb = []
ask_arr = []
class bb_manage:

    def input_bb(fact):
        for f in fact:
            # if (f in bb):
            #     return
            # else:
                sql = ('SELECT {} FROM {} WHERE {}'.format('terminal_id', 'fact_data', 'fact_id=\'{}\''.format(f)))
                cr_0.execute(sql)
                result = cr_0.fetchall()
                if result[0][0] == 1:
                    bb.append(f)
                    # print("%s%s" % ("คุณเเป็น :",blackboard.bb_manage.get_factname(f)))
                    return "end"
                else:
                    bb.append(f)
        return

    def input_bb_str(fact):
        bb.append(fact)
        # sql = ('SELECT {} FROM {} WHERE {}'.format('terminal_id', 'fact_data', 'fact_id=\'{}\''.format(fact)))
        # cr_0.execute(sql)
        # result = cr_0.fetchall()
        # if result[0][0] == 1:
        #     print("%s%s" % ("คุณเเป็น :",blackboard.bb_manage.get_factname(fact)))
        #     return "end"
        return


    def check_bb(if_,r,then_):
        length = 0
        if_ = if_.split(',')
        for i in if_:
            if (i in bb):
                length += 1
            else:
                ask = blackboard.bb_manage.check_start(i)
                # ask = input("%s%s" % (blackboard.bb_manage.get_factname(i)," is true by check BB?(y/n):"))
                if ask == "y":
                    # blackboard.bb_manage.input_bb_str(i)
                    end = blackboard.bb_manage.recv_fact(i)
                    if end == "end":
                        return "end"
                    length += 1
                elif ask == "end":
                    return "end"
                else:
                    no_bb.append(i)
                    return
        if len(if_) == length:
            if ((then_).find(',') > -1):
                end = blackboard.bb_manage.check_then(then_,r)
                if end == "end":
                    return "end"
            else:
                blackboard.bb_manage.input_bb_str(then_)
                end = blackboard.bb_manage.recv_fact(then_)
                if end == "end":
                    return "end"
        return

    def check_then(then_,r):
        then_ = then_.split(',')
        for i in then_:
            end = blackboard.bb_manage.recv_fact(i)
            if end == "end":
                return "end"
        return

    def recv_fact(fact):
        sql = ('SELECT {} FROM {} WHERE {}'.format('fact_name', 'fact_data', 'fact_id=\'{}\''.format(fact)))
        cr_0.execute(sql)
        for fact_name in cr_0.fetchall():
            end = inf.inference(fact_name[0]).forward_()
            if end=="end":
                return "end"
        return

    def get_factname(id):
        ret = ""
        sql = ('SELECT {} FROM {} WHERE {}'.format('fact_name', 'fact_data', 'fact_id=\'{}\''.format(id)))
        cr_0.execute(sql)
        for fact_name in cr_0.fetchall():
            ret = fact_name[0]
        return ret

    def check_start(fact):
        a = []
        sql2 = ('SELECT {} FROM {} WHERE {} LIKE {} '.format('*', 'rule_data', 'part_then', '\'%{}%\''.format(str(fact))))
        cr_0.execute(sql2)
        for then_ in cr_0.fetchall():
            a.append(then_[2])
        if len(a) < 1:
            if (fact in bb):
                return "y"
            else:
                if(fact in no_bb):
                    return "n"
                else:
                    ask_arr.append(fact)
                    return "end"
                    # ask = input("\n%s%s" % (blackboard.bb_manage.get_factname(fact), " is true? by check start(y/n):"))
                    # if ask == "y":
                    #     end = blackboard.bb_manage.recv_fact(fact)
                    #     if end == "end":
                    #         return "end"
                    #     return "y"
                    # elif ask == "end":
                    #     return "end"
                    # else:
                    #     no_bb.append(fact)
                    #     return "n"
        else:
            for fact_ in a:
                if ((fact_).find(',') > -1):
                    fact_2 = fact_.split(',')
                    c = 0
                    for i in fact_2:
                        non = 0
                        for j in fact_2:
                            if(j in no_bb):
                                non += 1
                        if non is 0:
                            ask = blackboard.bb_manage.check_start(i)
                            if ask == "y":
                                end = blackboard.bb_manage.recv_fact(i)
                                if end == "end":
                                    return "end"
                                else:
                                    c += 1
                            elif ask == "end":
                                return "end"
                            else:
                                no_bb.append(i)
                        else:
                            return "n"
                    if c == len(fact_2):
                        return "y"
                    else:
                        return "n"
                else:
                    ask = blackboard.bb_manage.check_start(fact_)
                    if ask == "y":
                        return ask
                    elif ask == "end":
                        return "end"
                    else:
                        no_bb.append(fact_)
                        return
        return

    def unique(list1):
        unique_list = []
        for x in list1:
            if x not in unique_list:
                unique_list.append(x)
        return unique_list

    def get_fact_bb(bb):
        ret = []
        for i in bb:
            sql = ('SELECT {} FROM {} WHERE {}'.format('fact_name', 'fact_data', 'fact_id=\'{}\''.format(i)))
            cr_0.execute(sql)
            for fact_name in cr_0.fetchall():
                ret.append(fact_name[0])
        return ret

    def get_fact_id(bb_in):
        ret = []
        for i in bb_in:
            sql = ('SELECT {} FROM {} WHERE {}'.format('fact_id', 'fact_data', 'fact_name=\'{}\''.format(i)))
            cr_0.execute(sql)
            for fact_id in cr_0.fetchall():
                ret.append(blackboard.bb_manage.ch_digit(fact_id[0]))
        return ret

    def ch_digit(id):
        if id < 10:
            id_str = ("%s%s" % ("00000",id))
        elif id >= 10 and id < 99:
            id_str = ("%s%s" % ("0000",id))
        elif id >= 100 and id < 999:
            id_str = ("%s%s" % ("000",id))
        elif id >= 1000 and id < 9999:
            id_str = ("%s%s" % ("00",id))
        elif id >= 10000 and id < 99999:
            id_str = ("%s%s" % ("0",id))
        else: id_str = str(id)
        return id_str








