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
    返回一个字典，包含该推送目标的所有信息
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

def get_task():
    """
    从数据库中获取task信息
    返回1.总task个数
        2.一个包含了N个字典的元组，包含每个任务id，模块名，启用状态，上一个版本号，推送目标id
    """
    get_task_count_sql = "SELECT COUNT(*) FROM `task`"
    get_task_sql = "SELECT * FROM `task`"
    global task_count
    global tasks
    gt_task = []
    gt_cursor = db.cursor()
    try:
        gt_cursor.execute(get_task_count_sql)
        results = gt_cursor.fetchone()
        task_count = int(results[0])
        del gt_cursor
        del results
    except:
        db.rollback()

    gt_cursor = db.cursor()
    try:
        gt_cursor.execute(get_task_sql)
        results = gt_cursor.fetchall()
        for row in results:
            gt_task.append({
                'task_id' : row[0],
                'module_name' : row[2],
                'enabled' : row[3],
                'task_status' : row[4],
                'last_run' : row[5],
                'latest_version' : row[6],
                'push_to' : row[8]
            })
    except:
        pass
    tasks = tuple(gt_task)
    del gt_task


connect_db()
get_task()
tasks = tuple(tasks)
print(tasks)

db.close()


""" 
im = ["AX86U_official_sourcecode", "AX86U_official_firmware"]
for pkg in im:
    imp = importlib.import_module('task.'+pkg)
    # imp.get_version()
    del imp
 """
