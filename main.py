#!/usr/bin/python
# -*- coding: UTF-8 -*-
import importlib
import smtplib
import pymysql
import requests
import time
import config
import task #可以通过task.tasks获取模块名

def push(push_through, target_id, push_message, push_title = "更新检查器推送"): #TODO title改为模块名+推送
    """
        推送函数
        push_through 推送方式 = ["email","phone","sc","tg"]
        target_id 推送目标ID
        push_message 推送信息
        push_title 推送标题
    """
    if push_through == "sc":
        sc_req = requests.post(url="https://sc.ftqq.com/"+get_push_info(target_id)['serverchan_key']+".send", data={"text":push_title, "desp":push_message + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())})
        time.sleep(3)
        if sc_req.json()['errmsg'] == "success":
            return
        else:
            print("推送错误："+sc_req.json()['errmsg'])
            return "fail"
    elif push_through == "tg":
        return
    elif push_through == "email":
        return
    elif push_through == "phone":
        return

def connect_db():
    """
    连接数据库
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
        gpi_cursor.close
        gpi_info = {
            'push_id' : gpi_results[0],
            'push_name' : gpi_results[1],
            'email_address' : gpi_results[2],
            'phone_number' : gpi_results[3],
            'serverchan_key' : gpi_results[4],
            'tg_chat_id' : gpi_results[5]
        }
    except:
        print("[get_push_info] Error: unable to fetch data")
        return "error"
    return gpi_info

def get_config(config_name):
    """
    从数据库获取配置
    """
    get_config_sql = "SELECT * FROM `config` \
                      WHERE `config_name` = '" + config_name + "'"
    gc_cursor = db.cursor()
    try:
        gc_cursor.execute(get_config_sql)
        gc_results = gc_cursor.fetchone()
        gc_cursor.close
        return gc_results[2]
    except:
        print("[get_push_info] Error: unable to fetch data")
        return "error"

def get_task():
    """
    从数据库中获取task信息
    返回1.总task个数 -- [task_count]
        2.一个包含了N个字典的元组，包含每个任务id，模块名，启用状态，上一个版本号，推送目标id -- [tasks]
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
        gt_cursor.close
        del gt_cursor
        del results
    except:
        db.rollback()

    gt_cursor = db.cursor()
    try:
        gt_cursor.execute(get_task_sql)
        results = gt_cursor.fetchall()
        gt_cursor.close
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


if __name__ == '__main__':
    connect_db()
    get_task()

    for i in range(0, task_count):
        if tasks[i]['enabled'] != "yes":
            continue
        imp = importlib.import_module('task.' + tasks[i]['module_name'])
        check_result = imp.check_update(tasks[i]['latest_version'])
        #check_update函数，返回一个list。[状态(success,error), 如果状态为error则为错误信息，如果为success则为是否有更新(0为无更新，1为有更新)，如果有更新则依次为新版本号，发布时间，发布内容]
        if check_result[0] == 'error' or check_result[0] != 'success':
            pass #TODO 更新最后运行时间以及状态
        elif check_result[1] == 0:
            continue
        elif check_result[1] == 1:
            push('sc', tasks[i]['push_to'], check_result[4])
            update_sql = "UPDATE `task` SET `task_status` = 'success', `latest_version` = '%s', `release_date` = '%s' WHERE `task_id` = %d" % (check_result[2], check_result[3], i + 1)
            cursor = db.cursor()
            try:
                cursor.execute(update_sql)
                db.commit()
            except:
                db.rollback()
            cursor.close()
            #print(update_sql)
        #print(imp.check_update(tasks[i]['latest_version'])) 

    db.close()