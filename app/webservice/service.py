from flask import request, jsonify
from app import app, mgDLF, cr_0
import json

#inferance interface begin
from app.webservice import forward_inf as inf
from app.webservice import blackboard as blackboard
#inferance interface end

@app.route('/', methods=['GET'])
def test_get():
    response = {
        "response" : "This is test GET method"
    }
    return jsonify(response)

@app.route('/test-input', methods=['POST'])
def test_post():
    msg = request.json.get('msg')
    response = {
        "response" : msg
    }
    return jsonify(response)

@app.route('/test-return', methods=['POST'])
def test_return():
    fact = request.json.get('fact')
    bb = request.json.get('backborad')
    print(fact,bb)
    response = {
        "backborad" : bb
    }
    return jsonify(response)

@app.route('/inferance-engine', methods=['POST'])
def inferance_engine():
    # pull data
    fact = request.json.get('fact')
    data_blackboard_user = request.json.get('blackboard')
    data_not_exist_blackborad_user = request.json.get('not_exist_blackboard')

    print(fact)
    print(data_blackboard_user)
    print(data_not_exist_blackborad_user)

    data_blackboard = blackboard.bb_manage.get_fact_id(data_blackboard_user)
    data_not_exist_blackborad = blackboard.bb_manage.get_fact_id(data_not_exist_blackborad_user)

    print(data_blackboard)
    print(data_not_exist_blackborad)

    # define data
    blackboard.bb = data_blackboard
    blackboard.no_bb = data_not_exist_blackborad

    # processing intent
    intent = {"{}".format(fact)}
    res_fulfill, intent_name = mgDLF.detect_intent_texts(intent,'th')
    # default intent (You can add if you want.)
    default_intent = [
        "Default Welcome Intent",
        "Default Fallback Intent",
        "คุยเล่น",
        "คำหยาบ",
        "ตลก",
        "มีอาการ",
        "ไม่มีอาการ"
    ]
    excep_intent = [
        "มีอาการ",
        "ไม่มีอาการ"
    ]
    if intent_name in default_intent:
        if fact == "อยากตรวจใหม่" :
            # define response data TYPE "DEFAULT"
            data = {
                'response' : "ได้สิ แน่นอนเลย",
                'blackboard' : [],
                'not_exist_blackboard' : [],
                'type_response' : 'DEFAULT' 
            }
        elif intent_name in excep_intent:
            # define response data TYPE "DEFAULT"
            data = {
                'response' : "ตอบให้มันดีๆ หน่อยสิ",
                'blackboard' : data_blackboard,
                'not_exist_blackboard' : data_not_exist_blackborad,
                'type_response' : 'DEFAULT' 
            }
        else:
            # define response data TYPE "DEFAULT"
            data = {
                'response' : res_fulfill,
                'blackboard' : data_blackboard,
                'not_exist_blackboard' : data_not_exist_blackborad,
                'type_response' : 'DEFAULT' 
            }
    else:
        inf.inference(res_fulfill).forward_()
        data_ask_user = blackboard.bb_manage.unique(blackboard.bb_manage.get_fact_bb(blackboard.ask_arr))
        data_blackboard = blackboard.bb_manage.unique(blackboard.bb_manage.get_fact_bb(blackboard.bb))
        data_not_exist_blackborad = blackboard.bb_manage.unique(blackboard.bb_manage.get_fact_bb(blackboard.no_bb))
        if not data_ask_user:
            blackboard.ask_arr = []
            
            ter=[]
            sql = 'SELECT fact_id FROM fact_data WHERE terminal_id="1"'
            cr_0.execute(sql)
            for terminal in cr_0.fetchall():
                if terminal[0] < 10:
                    ter_0 = ("%s%s" % ("00000", terminal[0]))
                elif terminal[0] >= 10 and terminal[0] <= 99:
                    ter_0 = ("%s%s" % ("0000", terminal[0]))
                elif terminal[0] >= 100 and terminal[0] <= 999:
                    ter_0 = ("%s%s" % ("000", terminal[0]))
                elif terminal[0] >= 1000 and terminal[0] <= 9999:
                    ter_0 = ("%s%s" % ("00", terminal[0]))
                elif terminal[0] >= 10000 and terminal[0] <= 99999:
                    ter_0 = ("%s%s" % ("0", terminal[0]))
                else:
                    ter_0 = terminal[0]
                if (ter_0 in blackboard.bb):
                    ter.append(blackboard.bb_manage.get_factname(ter_0))

            # define response data TYPE "CONCUSION"
            if not ter:
                data = {
                    'response' : 'งั้นหมอไม่แน่ใจ ลองบอกอาการอื่นมาได้ไหม',
                    'blackboard' : data_blackboard,
                    'not_exist_blackboard' : data_not_exist_blackborad,
                    'type_response' : 'NO-CONCUSION' 
                }
            else:
                data = {
                    'response' : '{}'.format(ter),
                    'blackboard' : data_blackboard,
                    'not_exist_blackboard' : data_not_exist_blackborad,
                    'type_response' : 'CONCUSION' 
                }       
        else:
            # define response data TYPE "ASK"
            blackboard.ask_arr = []
            data = {
                'response' : data_ask_user[0],
                'blackboard' : data_blackboard,
                'not_exist_blackboard' : data_not_exist_blackborad,
                'type_response' : 'ASK' 
            }
    return jsonify(data)


@app.route('/detect-intent',methods=['POST'])
def detect_dlf():
    intent = {"{}".format(request.json.get('intent'))}
    res_fulfill, intent_name = mgDLF.detect_intent_texts(intent,'th')
    fullfillment = {
        "fullfillment" : res_fulfill,
        "intent_name" : intent_name
    }
    return jsonify(fullfillment)

@app.route('/train-dlf', methods=['POST'])
def train_dlf():
    text_train = request.json.get('text')
    
    result_data = None
    dlf_display = "{}".format(text_train)
    dlf_train_phr = {"{}".format(text_train)}
    dlf_message_txt = {"{}".format(text_train)}
    print('{} {} {}'.format(dlf_display, dlf_train_phr, dlf_message_txt))

    res = mgDLF.create_intent(display_name=dlf_display,
                            training_phrases_parts=dlf_train_phr,
                            message_texts=dlf_message_txt)

    if res is 0:
        print('Intent {} is already exist.'.format(dlf_display))
    else :
        print(res)
    result_data = {
        "exist" : res,
        "intent" : text_train
    }
    return jsonify(result_data)