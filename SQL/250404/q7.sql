CREATE TABLE emp (
    empnum INT(3) not null AUTO_INCREMENT,
    name varchar(10) not null,
    job varchar(10) not null,
    birthdate varchar(12) not null,
    sal int(5) not null,
    deptno int(2) not null,
    PRIMARY KEY (empnum)
);
CREATE TABLE dept (
    deptno int(2),
    dname VARCHAR(14),
    loc VARCHAR(13),
    CONSTRAINT PK_DEPT PRIMARY KEY (deptno) 
);
INSERT INTO dept VALUES (10,'ACCOUNTING','NEW YORK');
INSERT INTO dept VALUES (20,'RESEARCH','DALLAS');
INSERT INTO dept VALUES (30,'SALES','CHICAGO');
INSERT INTO dept VALUES (40,'OPERATIONS','BOSTON');
INSERT INTO emp(name,job,birthdate,sal,deptno) VALUES ('SMITH','CLERK',STR_TO_DATE('17-12-1990','%d-%m-%Y'),800,10);
INSERT INTO emp(name,job,birthdate,sal,deptno) VALUES ('SMITH','SALESMAN',STR_TO_DATE('20-2-1982','%d-%m-%Y'),1600,20);
INSERT INTO emp(name,job,birthdate,sal,deptno) VALUES ('WARD','SALESMAN',STR_TO_DATE('22-2-1983','%d-%m-%Y'),1250,30);
INSERT INTO emp(name,job,birthdate,sal,deptno) VALUES ('JONES','MANAGER',STR_TO_DATE('2-4-1981','%d-%m-%Y'),2975,40);
INSERT INTO emp(name,job,birthdate,sal,deptno) VALUES ('MARTIN','SALESMAN',STR_TO_DATE('28-9-1981','%d-%m-%Y'),1250,10);
INSERT INTO emp(name,job,birthdate,sal,deptno) VALUES ('BLAKE','MANAGER',STR_TO_DATE('1-5-1981','%d-%m-%Y'),2850,20);
INSERT INTO emp(name,job,birthdate,sal,deptno) VALUES ('CLARK','MANAGER',STR_TO_DATE('9-6-1981','%d-%m-%Y'),2450,30);
INSERT INTO emp(name,job,birthdate,sal,deptno) VALUES ('SCOTT','ANALYST',STR_TO_DATE('13-7-1987','%d-%m-%Y'),2000,40);
INSERT INTO emp(name,job,birthdate,sal,deptno) VALUES ('KING','PRESIDENT',STR_TO_DATE('17-11-1982','%d-%m-%Y'),5000,10);
INSERT INTO emp(name,job,birthdate,sal,deptno) VALUES ('TURNER','SALESMAN',STR_TO_DATE('8-9-1983','%d-%m-%Y'),1900,20);
INSERT INTO emp(name,job,birthdate,sal,deptno) VALUES ('ADAMS','CLERK',STR_TO_DATE('13-7-1987', '%d-%m-%Y'),1100,30);
INSERT INTO emp(name,job,birthdate,sal,deptno) VALUES ('JAMES','CLERK',STR_TO_DATE('3-12-1990','%d-%m-%Y'),950,40);
INSERT INTO emp(name,job,birthdate,sal,deptno) VALUES ('FORD','ANALYST',STR_TO_DATE('3-12-1981','%d-%m-%Y'),3000,10);
INSERT INTO emp(name,job,birthdate,sal,deptno) VALUES ('MILLER','CLERK',STR_TO_DATE('23-1-1982','%d-%m-%Y'),1300,20);

SELECT * FROM emp;
-- 부서번호가 40인 부서의 급여 평균보다 높게 받는 사원들의 모든 컬럼과 나이를 조회하는 쿼리를 작성해주세요.
SELECT e.*, 
       FLOOR( 
           (CAST(REPLACE(CURRENT_DATE,'-','') AS UNSIGNED) - 
            CAST(REPLACE(e.birthdate,'-','') AS UNSIGNED)) / 10000) AS age
FROM emp
WHERE sal > (
    SELECT AVG(sal)
    FROM emp
    WHERE deptno = 40 GROUP BY deptno
    );