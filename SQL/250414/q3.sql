CREATE TABLE lecture_basic (
    id				INT             NOT NULL,
    lecture_name	VARCHAR(50)		NOT NULL,
    student_number	INT				NOT NULL,
    student_name	VARCHAR(30)		NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO lecture_basic VALUES
(1, 'math', 10001, 'HongGildong'),
(2, 'korean', 10001, 'HongGildong'),
(3, 'math', 10003, 'HongGilsun'),
(4, 'math', 10004, 'KimChulsoo');


CREATE TABLE lecture_special (
    id				INT             NOT NULL,
    lecture_name	VARCHAR(50)		NOT NULL,
    student_number	INT				NOT NULL,
    student_name	VARCHAR(30)		NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO lecture_special VALUES
(1, 'piano', 10001, 'HongGildong'),
(2, 'kendo', 10002, 'KimAmugae'),
(3, 'piano', 10003, 'HongGilsun'),
(4, 'kendo', 10003, 'HongGilsun');

-- 아래 쿼리는 lecture_basic, lecture_special 테이블의 구조를 나타냅니다. 해당 테이블을 수정할 필요는 없습니다.
DESC lecture_basic;
DESC lecture_special;

-- 1. lecture_basic 테이블에서 학생번호(student_number)와 학생이름(student_name)을 조회하는 쿼리를 작성하세요.
SELECT student_number, student_name FROM lecture_basic;

-- 2. lecture_special 테이블에서 학생번호(student_number)와 학생이름(student_name)을 조회하는 쿼리를 작성하세요.
SELECT student_number, student_name FROM lecture_special;

-- 3. 위 2개의 쿼리에 대해서 집합 연산자를 이용하여 lecture_special 테이블에는 존재하지만, lecture_basic에는 
-- 존재하지 않는 학생번호와 학생이름을 조회하는 쿼리를 작성하세요.
SELECT student_number, student_name FROM lecture_special
EXCEPT
SELECT student_number, student_name FROM lecture_basic;

