import time
from threading import Timer
from os import path

import itchat
import pyodbc as po


def getdata():
    try:
        server = '10.224.81.131,3000'
        database = 'WechatDB'
        username = 'sa'
        password = 'foxconn168!!'
        conn = po.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                          server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM [dbo].[WCMessageContent2] where status=0")
        row = cursor.fetchone()
        while row:
            # Print the row
            message = str(row[0]) + ", " + str(row[1] or '') + ", " + str(row[2] or '') + ", " + str(
                row[3] or '') + "," + str(row[4] or '')
            # cursor.execute(update)
            print(message)
            # send_msg(message)
            # update = "update WCMessageContent2 set status ='1' where id='"+str(row[0])+"'"
            # updateStatus(update)
            # print(message)
            row = cursor.fetchone()
        # Close the cursor and delete it
        cursor.close()
        del cursor
        # Close the database connection
        conn.close()

    except Exception as err:
        print(err)


def updateStatus(update):
    server = '10.224.81.131,3000'
    database = 'WechatDB'
    username = 'sa'
    password = 'foxconn168!!'
    conn = po.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                      server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    print(update)
    cursor = conn.cursor()
    cursor.execute(update)
    conn.commit()
    cursor.close()
    del cursor
    # Close the database connection
    conn.close()


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
    except Exception as err:
        log = err
        print(log)
        writelog(log)


if __name__ == '__main__':
    # itchat.auto_login()
    # Timer(30,  getdata()).start()
    getdata()
