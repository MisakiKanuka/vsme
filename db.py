import sqlite3


def init_db():
    conn = sqlite3.connect("vsme.sqlite")

    cursor = conn.cursor()

    with open("schema.sql") as f:
        cursor.executescript(f.read())
    conn.commit()
    conn.close()


# 行動詳細
def find_detail_date():
    conn = sqlite3.connect("vsme.sqlite")

    cursor = conn.cursor()

    sql = "SELECT * FROM DETAIL"

    detail_date = cursor.execute(sql).fetchall()

    conn.close()

    return detail_date


def add_detail_date(userid, date, behavior, winlose):
    conn = sqlite3.connect("vsme.sql")

    cursor = conn.cursor()

    sql = "INSERT INTO DETAIL (userid, date, behavior, winlose) VALUES(?, ?)"
    cursor.execute(sql, (userid, date, behavior, winlose))

    conn.commit()

    conn.close()


if __name__ == "__main__":
    init_db()
