CREATE TABLE REQUEST_HIST(
	request_id		INT			NOT NULL PRIMARY KEY,
	req_status		VARCHAR(50)	NOT NULL,
	req_member_id	VARCHAR(10)	NOT NULL
);

INSERT INTO REQUEST_HIST VALUES
(10001, 'success', 'P001'),
(10002, 'success', 'P002'),
(10003, 'fail', 'P001'),
(10004, 'success', 'P002'),
(10005, 'fail', 'P003'),
(10006, 'fail', 'P001');


CREATE TABLE MEMBER(
	member_id		VARCHAR(10)	NOT NULL PRIMARY KEY,
	member_name		VARCHAR(50)	NOT NULL
);

INSERT INTO MEMBER VALUES
('P001', 'Kim'),
('P002', 'Park'),
('P003', 'Lee');

-- 아래 쿼리는 REQUEST_HIST, MEMBER 테이블의 구조를 나타냅니다. 해당 테이블을 수정할 필요는 없습니다.
DESC REQUEST_HIST;
DESC MEMBER;

-- REQUEST_HIST 테이블과 MEMBER 테이블을 INNER JOIN하여 조회하되, 요청상태(req_status)가 fail인 정보만 조회하는 쿼리를 작성하세요.
SELECT * FROM REQUEST_HIST INNER JOIN MEMBER WHERE req_status = 'fail';
