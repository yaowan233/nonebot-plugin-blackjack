import sqlite3
import datetime
import random


def sign_today(uid, group_id) -> str:
    init()
    flag = random.randint(1, 100)
    if flag <= 50:
        point = random.randint(1, 5)
    elif flag <= 80:
        point = random.randint(6, 10)
    elif flag <= 95:
        point = random.randint(11, 15)
    else:
        point = random.randint(16, 20)
    now = datetime.datetime.now()
    conn = sqlite3.connect("identifier.sqlite")
    cursor = conn.cursor()
    sql = f"select * from sign_in where uid={uid} and belonging_group={group_id}"
    data = cursor.execute(sql).fetchall()
    if data:
        date = data[0][1]
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
        timedelta = now - date
        point_past = data[0][3]
        if timedelta.days < 1:
            return f"你今天已经签到过啦，请明天再来！\n你现在的点数是{point_past}"
        count = data[0][2] + 1
        if point_past >= 0:
            point_now = data[0][3] + point
            point_word = f"{point_now}"
        elif -100 < point_past < 0:
            point_now = point_past + abs(point_past) * point
            point_word = f"{point_past}+{-point_past}*{point}={point_now}"
        elif -1000 < point_past <= -100:
            point_now = point_past + int(abs(point_past) * (1.11 ** point))
            point_word = f"{point_past}+{-point_past}*1.11^{point}={point_now}"
        else:
            point_now = point_past + int(abs(point_past) * (1.1 ** point))
            point_word = f"{point_past}+{-point_past}*1.1^{point}={point_now}"
        sql = f"UPDATE sign_in set sign_in_date = date(CURRENT_TIMESTAMP,'localtime'), total_sign_in = {count}," \
              f" points = {point_now}, today_point = {point} where uid = {uid} and belonging_group = {group_id}"
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()
        words = f"签到成功，今日获得点数为{point}，你现在的点数是" + point_word
        return words
    else:
        sql = f"INSERT INTO sign_in VALUES(null, date(CURRENT_TIMESTAMP,'localtime'), 1, {point}, {group_id}," \
              f" {uid}, {point})"
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()
        words = f"签到成功，今日获得点数为{point}，你现在的点数是{point}"
        return words


def get_point(group: int, uid: int) -> int:
    init()
    conn = sqlite3.connect("identifier.sqlite")
    cursor = conn.cursor()
    sql = f"select * from sign_in where belonging_group={group} and uid={uid}"
    cursor.execute(sql)
    point = int(cursor.fetchone()[3])
    cursor.close()
    conn.commit()
    conn.close()
    return point


def update_point(group: int, uid: int, point: int):
    init()
    conn = sqlite3.connect("identifier.sqlite")
    cursor = conn.cursor()
    sql = f"""update sign_in set points={point} where belonging_group={group} and uid={uid}"""
    cursor.execute(sql)
    cursor.close()
    conn.commit()
    conn.close()


def init():
    conn = sqlite3.connect("identifier.sqlite")
    cursor = conn.cursor()
    sql = """create table if not exists sign_in(
        id integer primary key autoincrement,
        sign_in_date datetime not null,
        total_sign_in int not null,
        points int not null,
        belonging_group int not null,
        uid int not null,
        today_point int
    )
    """
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
