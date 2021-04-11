import time
from os import path

import itchat
import cx_Oracle


def getdata():
    try:
        cx_Oracle.init_oracle_client(r"D:\instantclient_19_9")
        dsn = cx_Oracle.makedsn('10.224.81.31', '1521', 'VNAP')
        conn = cx_Oracle.connect("AP2", "NSDAP2LOGPD0522", dsn)
        if isinstance(conn, cx_Oracle.Connection):
            with conn.cursor() as  cursor:
                cursor.execute("select * from MES4.R_SYSTEM_LOG where emp_no ='APP_AUTO' and PRG_NAME ='ALERT WECHAT'")
                # res = cursor.fetchall()
                res = cursor.fetchall()
                for row in res:
                    message = row[1] + '-' + row[3]
                    print(message)
                    writelog(message)
                    # send_msg(message)
                    # cursor.execute("update MES4.R_SYSTEM_LOG set ACTION_TYPE ='1' where ACTION_DESC='" + row[3] + "'")
                    conn.commit()
        conn.close()
    except Exception as err:
        writelog(err)
        print(err)


def writelog(data):
    d = path.dirname(__file__)
    f = open(d + "/log.txt", "a")
    f.writelines(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ":" + data + "\n")
    f.close()


def send_msg(message):
    try:
        users = itchat.search_friends(name='Vuongnd')
        # users = itchat.search_chatrooms(name='IDtest')
        username = users[0]['UserName']
        itchat.send(message, toUserName=username)
        print("sucess" + username)
        log = "send to : " + users + " Message :" + message
        writelog(log)
    except Exception as erro:
        log = erro
        writelog(log)
        print(log)


if __name__ == '__main__':
    # itchat.auto_login()
    getdata()
    # send_msg('Xin chao vietnam')
