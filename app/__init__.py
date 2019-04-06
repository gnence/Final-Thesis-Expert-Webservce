from flask import Flask
from flask_cors import CORS

from app.lib import connect_db as connn
from app.lib import query_db as qr
from app.lib import manage_dlf as mgdia 
from app.webservice import conn_sql as conn

db_host = '--host--'
db_user = '--username--'
db_pw = '--pw--'
db_name = '--dbname--'

dlf_project_id = '--GoogleCS-project-id--'
dlf_session_id = '--GoogleCS-session-id--'

connect = conn.database(host=db_host, 
                        username=db_user,
                        password=db_pw,
                        dbname=db_name)
connect = connect.get_conn()
cr_0 = connect.cursor()

mgDLF = mgdia.manageDLF(projectID=dlf_project_id,
                        sessionID=dlf_session_id)

conDB = connn.connectDB(host=db_host,
                       username=db_user,
                       password=db_pw,
                       database=db_name)

qy = qr.queryDB(conDB.getConnection())

text_train_list = qy.querySelect(selectPart='fact_name',
                                fromPart='fact_data',
                                wherePart='1')

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

from app.webservice import service