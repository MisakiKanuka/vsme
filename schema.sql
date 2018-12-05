-- schema.sql

DROP TABLE IF EXISTS users_list;

CREATE TABLE users_list(
  name     TEXT,
  password TEXT,
  goal     TEXT,
  wins     INTEGER,
  losses   INTEGER
);

-- 初期データ
INSERT INTO users_list
VALUES ('MANA', 'mana0115', 'TOEIC700点以上！', 2, 0);