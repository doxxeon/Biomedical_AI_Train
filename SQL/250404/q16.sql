CREATE TABLE EMPLOYEE(
  employee_id	INT NOT NULL PRIMARY KEY,
  salary		INT NOT NULL,
  position		VARCHAR(10) NOT NULL
);

INSERT INTO EMPLOYEE VALUES
(10000, 9000, '사장'),
(10001, 8000, '부장'),
(10002, 7800, '과장'),
(10003, 7500, '과장'),
(10004, 6800, '대리'),
(10005, 7000, '대리'),
(10006, 6000, '대리'),
(10007, 5500, '사원'),
(10008, 4500, '사원'),
(10009, 7000, '사원');


-- 아래는 EMPLOYEE 테이블에 대한 구조를 보여줍니다. 테이블을 수정하실 필요는 없습니다.
DESC EMPLOYEE;

-- 1. 직급이 '사원'인 직원의 급여를 조회하는 쿼리를 작성해봅시다.
SELECT salary 
FROM EMPLOYEE 
WHERE position = '사원'
ORDER BY salary asc;

-- 2. 앞에서 작성한 쿼리와 ALL을 이용하여, 모든 사원들의 급여보다 높거나 같은 급여를 가진 직원을 조회하는 쿼리를 작성해봅시다.

SELECT *
FROM EMPLOYEE 
WHERE salary >= ALL (
    SELECT salary FROM EMPLOYEE 
    WHERE position = '사원')
ORDER BY employee_id asc;