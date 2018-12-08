-- schema.sql

DROP TABLE IF EXISTS USERSLIST;
DROP TABLE IF EXISTS GOAL;
DROP TABLE IF EXISTS DETAIL;


-- 名前・パスワード管理
CREATE TABLE USERSLIST(
  userid       INT,
  name         TEXT,
  password     TEXT
);

-- 目標管理
CREATE TABLE GOAL(
  userid       INT,
  goal         TEXT
);

-- 入力データの詳細管理
CREATE TABLE DETAIL(
  userid       INT,
  DATE         TEXT,
  behavior     TEXT,
  winlose      TEXT
);

-- 初期データ
INSERT INTO USERSLIST
VALUES ('001', 'MISAKI', 'kkkkkanuka0320');
INSERT INTO GOAL
VALUES ('001', '体力が欲しい！');
INSERT INTO DETAIL
VALUES ('001', '2018/12/06', '3キロ走った', 1);