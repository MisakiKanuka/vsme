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
def add_detail_date(userid, behavior, winlose):
    conn = sqlite3.connect("vsme.sqlite")

    cursor = conn.cursor()

    sql = "INSERT INTO DETAIL (userid, date, behavior, winlose) VALUES(?, datetime('now', 'localtime'), ?, ?)"
    cursor.execute(sql, (userid, behavior, winlose))

    conn.commit()

    conn.close()


# 勝敗を取得する
def cnt_winlose_data(winlose):
    conn = sqlite3.connect("vsme.sqlite")

    cursor = conn.cursor()

    lose = "SELECT count(winlose) FROM DETAIL WHERE winlose='lose';"
    win = "SELECT count(winlose) FROM DETAIL WHERE winlose='win';"

    cursor.execute(lose, (winlose))
    cursor.execute(win, (winlose))

    conn.commit()

    conn.close()


# 勝敗を表示する
def find_winlose_data():
    conn = sqlite3.connect("vsme.sqlite")

    cursor = conn.cursor()

    lose = "SELECT * FROM DETAIL WHERE winlose='lose'"
    win = "SELECT * FROM DETAIL WHERE winlose='win'"

    cnt_lose = cursor.execute(lose).fetchall()
    cnt_win = cursor.execute(win).fetchall()

    conn.close()

    return cnt_lose, cnt_win


# 目標表示
def find_goal():
    conn = sqlite3.connect("vsme.sqlite")

    cursor = conn.cursor()

    sql = "SELECT * FROM GOAL"

    goal = cursor.execute(sql).fetchall()

    conn.close()

    return goal


# 目標記録
def add_goal(userid, goal):
    conn = sqlite3.connect("vsme.sqlite")

    cursor = conn.cursor()

    sql = "INSERT INTO GOAL (userid, goal) VALUES(?, ?)"
    cursor.execute(sql, (userid, goal))

    conn.commit()

    conn.close()


# ユーザー表示
def find_user():
    conn = sqlite3.connect("vsme.sqlite")

    cursor = conn.cursor()

    sql = "SELECT * FROM USERSLIST"

    user_info = cursor.execute(sql).fetchall()

    conn.close()

    return user_info


# ユーザー登録
def create_user(userid, name, password):
    conn = sqlite3.connect("vsme.sqlite")

    cursor = conn.cursor()

    sql = "INSERT INTO USERSLIST (userid, name, password) VALUES(?, ?, ?)"
    cursor.execute(sql, (userid, name, password))

    conn.commit()

    conn.close()


if __name__ == "__main__":
    init_db()
