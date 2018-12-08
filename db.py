import sqlite3


def init_db():
    conn = sqlite3.connect("vsme.sqlite")

    cursor = conn.cursor()

    with open("schema.sql") as f:
        cursor.executescript(f.read())
    conn.commit()
    conn.close()


# 行動詳細表示
def find_detail_date():
    conn = sqlite3.connect("vsme.sqlite")

    cursor = conn.cursor()

    sql = "SELECT * FROM DETAIL"

    detail_date = cursor.execute(sql).fetchall()

    conn.close()

    return detail_date


# 行動記入
def add_detail_date(userid, date, behavior, winlose):
    conn = sqlite3.connect("vsme.sqlite")

    cursor = conn.cursor()

    sql = "INSERT INTO DETAIL (userid, date, behavior, winlose) VALUES(?, ?, ?, ?)"
    cursor.execute(sql, (userid, date, behavior, winlose))

    conn.commit()

    conn.close()


# 目標表示
def find_goal():
    conn = sqlite3.connect("vsme.sqlite")

    cursor = conn.cursor()

    sql = "SELECT goal FROM GOAL"

    gorl = cursor.execute(sql).fetchall()

    conn.close()

    return gorl


# 目標記録 まだ書いてない


if __name__ == "__main__":
    init_db()
