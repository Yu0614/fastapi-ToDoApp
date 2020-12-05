# users
INSERT INTO users (name, age) VALUES ("太郎", 15);
INSERT INTO users (name, age) VALUES ("次郎", 18);
INSERT INTO users (name, age) VALUES ("花子", 20);


# todos
INSERT INTO todos (user_id, title, place, url, memo, start_date, end_date) VALUES (1, 'title1', '東京都八王子市 鑓水 2丁目', 'https://www.google.com/', 'memo1', '2020-12-05 00:00:00' , '2020-12-05 12:00:00') ;
INSERT INTO todos (user_id, title, place, url, memo, start_date, end_date) VALUES (1, 'title2', '東京都八王子市 鑓水 2丁目', 'https://www.yahoo.co.jp/', 'memo2', '2020-12-05 00:00:00' , '2020-12-05 23:59:59') ;
INSERT INTO todos (user_id, title, place, url, memo, start_date, end_date) VALUES (1, 'title3', '東京都八王子市 鑓水 2丁目', 'https://www.facebook.com/', 'https://www.facebook.com/', '2020-12-05 00:00:00' , '2020-12-06 00:00:00') ;
INSERT INTO todos (user_id, title) VALUES (2, '2') ;
INSERT INTO todos (user_id, title) VALUES (3, '3') ;