CREATE TABLE request_past (
    id			INT             NOT NULL,
    name		VARCHAR(100)	NOT NULL,
  	number		VARCHAR(20)		NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO request_past VALUES
(1, '김원숭', 01012345678),
(2, '김호랑', 01011112222),
(3, '이기린', 01098765432),
(4, '권펭귄', 01011116789),
(5, '김강아지', 01099998765);


CREATE TABLE request_new (
    id			INT             NOT NULL,
    name		VARCHAR(100)	NOT NULL,
  	number		VARCHAR(20)		NOT NULL,
    email		VARCHAR(100)	NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO request_new VALUES
(1, '최호랑', 01022221234, 'ho@naver.com'),
(2, '이기린', 01098765432, 'girin@naver.com'),
(3, '김공룡', 01033331234, 'gong@naver.com'),
(4, '이토끼', 01012345679, 'rabbit@naver.com'),
(5, '박수달', 01012345555, 'park@naver.com'),
(6, '김강아지', 01099998765, 'dog@naver.com');

-- 아래 쿼리는 request_past, request_new 테이블의 구조를 나타냅니다. 해당 테이블을 수정할 필요는 없습니다.
DESC request_past;
DESC request_new;

-- 1. 각 테이블에서 이름(name)과 번호(number)를 조회하고, 집합연산자를 통해 중복을 제거하지 않고 데이터를 연결해보세요.
SELECT name, number FROM request_past
UNION ALL
SELECT name, number FROM request_new;

-- 2. 각 테이블에서 이름(name)과 번호(number)를 조회하고, 집합연산자를 통해 중복을 제거하여 데이터를 연결해보세요.
SELECT name, number FROM request_past
UNION
SELECT name, number FROM request_new;

