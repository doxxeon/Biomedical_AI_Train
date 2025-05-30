-- 아래는 EMPLOYEE 테이블에 대한 구조를 보여줍니다. 테이블을 수정하실 필요는 없습니다.
DESC EMPLOYEE;

-- 급여가 8000미만인 직원의 관리자 아이디와 급여를 출력하는 쿼리를 작성하세요.
SELECT manager_id, salary FROM EMPLOYEE WHERE employee_id in (SELECT manager_id FROM EMPLOYEE WHERE salary<8000) ORDER BY manager_id asc;