CREATE TABLE EMPLOYEE(
  employee_id	INT NOT NULL PRIMARY KEY,
  manager_id	INT,
  salary		INT NOT NULL
);

INSERT INTO EMPLOYEE VALUES
(10000, NULL, 9000),
(10001, NULL, 8500),
(10002, 10000, 9000),
(10003, 10002, 7000),
(10004, 10001, 9500),
(10005, 10003, 7500),
(10006, 10003, 5000);

-- 아래는 EMPLOYEE 테이블에 대한 구조를 보여줍니다. 테이블을 수정하실 필요는 없습니다.
DESC EMPLOYEE;

-- 자신의 관리자의 급여보다 높거나 같은 급여를 가진 직원의 ID를 출력하는 쿼리를 작성해봅시다.
SELECT employee_id FROM EMPLOYEE a WHERE salary >= (SELECT salary FROM EMPLOYEE b WHERE a.manager_id = b.employee_id) ORDER BY employee_id asc;
25