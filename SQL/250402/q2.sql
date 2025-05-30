-- DESC 명령어를 통해 정의된 kickboard 테이블을 확인할 수 있습니다.
DESC kickboard;

-- 2개의 데이터를 삽입하세요.
INSERT INTO kickboard (member_id, member_name, kickboard_id, kickboard_brand, rental_location, rental_date, distance, price) VALUES
('kmax6', '김민준', '7YWC', 'boardkick', '서울시 관악구 신림동', '2020-05-24 12:01:55', 354, 4700),
('flykite', '이서연', 'JXAN', 'willgo', '서울시 동작구 대방동', '2020-11-12 19:30:00', 560, 7200);

-- kickboard 테이블의 데이터를 출력하세요.
SELECT * FROM kickboard;