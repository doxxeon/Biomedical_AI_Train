CREATE TABLE FOOD(
  food_id	INT 			NOT NULL PRIMARY KEY,
  food_type	VARCHAR(30)		NOT NULL,
  food_name	VARCHAR(100)	NOT NULL,
  price		INT
);

INSERT INTO FOOD VALUES
(1, 'Appetizer', 'Salad', 5000),
(2, 'Appetizer', 'Soup', 3500),
(3, 'Main', 'Pasta', 8000),
(4, 'Main', 'Steak', 11000),
(5, 'Main', 'rice', 7000),
(6, 'Dessert', 'Ice-cream', 10000),
(7, 'Dessert', 'Cookie', 5000),
(8, 'Dessert', 'Coffee', 8000);

-- 아래는 FOOD 테이블에 대한 구조를 보여줍니다. 테이블을 수정하실 필요는 없습니다.
DESC FOOD;

-- 음식타입이 Main인 임의의 음식의 가격보다 비싼 음식들을 조회해봅시다.
SELECT food_id, food_type, food_name, price
FROM FOOD 
WHERE price > (SELECT price FROM FOOD WHERE food_type = 'Main') 
ORDER BY food_id asc;