-- customer 테이블을 정의하세요.
CREATE TABLE customer (
    customer_id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(10) NOT NULL,
    id VARCHAR(10) NOT NULL UNIQUE,
    pw VARCHAR(20) NOT NULL,
    phone_number VARCHAR(11),
    birth_date DATE
);

-- kickboard 테이블을 정의하세요.
CREATE TABLE kickboard (
    id VARCHAR(10) PRIMARY KEY,
    brand VARCHAR(20) NOT NULL,
    model_year INT NOT NULL,
    price_per_minute INT NOT NULL,
    basic_price INT NOT NULL,
    company VARCHAR(20) NOT NULL
);

-- 정의한 두 테이블을 확인하는 코드입니다. 아래 주석을 해제하여 결과를 확인하세요.
-- DESC customer;
-- DESC kickboard;

-- 정의한 테이블에 데이터가 올바르게 삽입되는지 확인해보세요.
-- INSERT INTO customer
-- VALUES('0187642351', '김민준', 'kmax6', 'HASH-lui235dfi2', '08786173448', '1989-03-09');
-- INSERT INTO kickboard
-- VALUES('7YWC', 'boardkick', 2015, 100, 1000, 'elice');
