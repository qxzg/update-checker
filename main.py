import importlib
import smtplib
import pymysql
import config 
import task #可以通过task.tasks获取模块名

def push(push_through, target_id, message): 
    """
        推送函数
        push_through 推送方式
        target_id 推送目标ID
        message 推送信息
    """
    return

def connect_db():
    """
    docstring
    """
    global db
    db = pymysql.connect(host = config.DATABASE_CONFIG['host'],
                     port = config.DATABASE_CONFIG['port'],
                     user = config.DATABASE_CONFIG['username'],
                     password = config.DATABASE_CONFIG['password'],
                     db = config.DATABASE_CONFIG['dbname'],
                     charset = config.DATABASE_CONFIG['charset'])
    return

def get_push_info(target_push_id):
    """
    获取目标的推送信息
    返回一个字典
    """
    get_push_info_sql = "SELECT * FROM `push` \
                         WHERE `push_id` = '" + str(target_push_id) + "'"
    gpi_cursor = db.cursor()
    try:
        gpi_cursor.execute(get_push_info_sql)
        gpi_results = gpi_cursor.fetchone()
        gpi_info = {
            'push_id' : gpi_results[0],
            'push_name' : gpi_results[1],
            'email_address' : gpi_results[2],
            'phone_number' : gpi_results[3],
            'serverchan_key' : gpi_results[4]
        }
    except:
        print("[get_push_info] Error: unable to fetch data")
        return
    return gpi_info


connect_db()

print(get_push_info(1))

db.close()


""" 
im = ["AX86U_official_sourcecode", "AX86U_official_firmware"]
for pkg in im:
    imp = importlib.import_module('task.'+pkg)
    # imp.get_version()
    del imp
 """