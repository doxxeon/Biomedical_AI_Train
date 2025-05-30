-- kickboard 테이블을 정의하세요.
CREATE TABLE kickboard(
    member_id VARCHAR(16),
    member_name VARCHAR(16),
    kickboard_id VARCHAR(16),
    kickboard_name VARCHAR(16),
    rental_location VARCHAR(16),
    rental_date DATETIME,
    distance INT,
    price INT
);

-- 데이터베이스에 정의된 테이블 목록을 출력하세요.
SHOW TABLES;

-- kickboard 테이블의 구조를 출력하세요.
DESC kickboard;