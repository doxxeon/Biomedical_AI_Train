CREATE TABLE student (
    id			    INT             NOT NULL,
    student_number  int				NOT NULL,
    name  			VARCHAR(30)     NOT NULL,
    grade  			INT 		    NOT NULL,
    email      		VARCHAR(100)			,    
    PRIMARY KEY (id)
);

INSERT INTO student VALUES
(1, 10001, 'HongGildong', 2, 'hong@naver.com'),
(2, 10002, 'KimAmoogae', 3, null),
(3, 10003, 'HongGilsun', 1, 'hong.sun@naver.com'),
(4, 10004, 'KimChulsoo', 3, null),
(5, 10005, 'LeeMooMyeong', 4, null);


CREATE TABLE lecture_special (
    id				INT             NOT NULL,
    lecture_name	VARCHAR(50)		NOT NULL,
    name			VARCHAR(30)		NOT NULL,
    email			VARCHAR(100)	NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO lecture_special VALUES
(1, 'piano', 'Kimseulki', 'seulki@naver.com'),
(2, 'kendo', 'KimGuest', 'guest@naver.com'),
(3, 'piano', 'HongGildong', 'hong@naver.com'),
(4, 'kendo', 'HongGilsun', 'hsun@naver.com');

-- 아래 쿼리는 student, lecture_special 테이블의 구조를 나타냅니다. 해당 테이블을 수정할 필요는 없습니다.
DESC student;
DESC lecture_special;

-- 1. student 테이블에서 이름(name)와 이메일(email)을 조회하는 쿼리를 작성하세요.
SELECT name, email FROM student;

-- 2. lecture_special 테이블에서 이름(name)와 이메일(email)을 조회하는 쿼리를 작성하세요.
SELECT name, email FROM lecture_special;

-- 3. 위 2개의 쿼리에 대해서 집합 연산자를 이용하여 공통적으로 존재하는 데이터를 조회하는 쿼리를 작성해주세요.
SELECT name, email FROM student
INTERSECT
SELECT name, email FROM lecture_special;
