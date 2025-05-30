CREATE TABLE STORE(
  store_id		INT 		NOT NULL PRIMARY KEY,
  store_name	VARCHAR(30) NOT NULL
);

INSERT INTO STORE VALUES
(1000, 'pizza'),
(1001, 'bunsik'),
(1002, 'ice-cream'),
(1003, 'coffee'),
(1004, 'cake');

CREATE TABLE PAYMENT(
  payment_id	INT NOT NULL PRIMARY KEY,
  store_id		INT NOT NULL,
  pay_amount	INT NOT NULL
);

INSERT INTO PAYMENT VALUES
(10123, 1000, 1000),
(10124, 1002, 6000),
(10125, 1001, 10000),
(10126, 1001, 3000),
(10127, 1003, 4500),
(10128, 1002, 5000);



-- 아래는 STORE, PAYMENT 테이블에 대한 구조를 보여줍니다. 테이블을 수정하실 필요는 없습니다.
DESC STORE;
DESC PAYMENT;

-- EXISTS문을 응용하여, 결제금액이 5000원 이상인 가게ID, 가게이름을 조회하는 쿼리를 작성해보세요.
SELECT store_id, store_name
FROM STORE s
WHERE EXISTS (SELECT '1' FROM PAYMENT p WHERE s.store_id = p.store_id AND p.payment_amount >= 5000) 
ORDER BY store_id asc;
