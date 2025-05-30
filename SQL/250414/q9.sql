CREATE TABLE EMPLOYEE(
  employee_id		INT 		NOT NULL PRIMARY KEY,
  department_name	VARCHAR(30) NOT NULL,
  salary			INT 		NOT NULL
);

INSERT INTO EMPLOYEE VALUES
(10000, '영업', 9000),
(10001, '개발', 8500),
(10002, '개발', 9000),
(10003, '운영', 7000),
(10004, '기획', 9500),
(10005, '사업', 7500),
(10006, '영업', 6000),
(10007, '기획', 10000),
(10008, '사업', 8000),
(10009, '개발', 9000),
(10010, '개발', 7500);

-- 아래는 EMPLOYEE 테이블에 대한 구조를 보여줍니다. 테이블을 수정하실 필요는 없습니다.
DESC EMPLOYEE;

-- 1. 부서이름이 '개발'인 직원의 직원ID, 급여 정보를 가지는 뷰(EMPLOYEE_DEV)를 만드는 쿼리를 작성해봅시다.
CREATE VIEW EMPLOYEE_DEV AS
SELECT employee_id, salary FROM EMPLOYEE WHERE department_name = '개발';

-- 2. 위에서 만든 뷰(EMPLOYEE_DEV)의 모든 데이터를 조회하는 쿼리를 작성해봅시다.
SELECT * FROM EMPLOYEE_DEV;