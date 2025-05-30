CREATE TABLE REQUEST(
  request_id		INT NOT NULL PRIMARY KEY,
  request_status	VARCHAR(10) NOT NULL
);

INSERT INTO REQUEST VALUES
(10001, 'SUCCESS'),
(10002, 'FAILED'),
(10003, 'SUCCESS'),
(10004, 'SUCCESS');

CREATE TABLE REQUEST_DTL(
  request_dtl_id	INT			NOT NULL PRIMARY KEY,
  request_id		INT			NOT NULL,
  request_name		VARCHAR(50) NOT NULL,
  request_content	VARCHAR(300)
);

INSERT INTO REQUEST_DTL VALUES
(21548, 10001, 'FOR_TEST', NULL),
(21567, 10002, 'GET', 'FOR GET'),
(22211, 10003, 'POST', 'DATA INPUT'),
(34527, 10004, 'DB', 'DATA INPUT'),
(36788, 10005, 'HELLO', NULL);

-- 아래는 REQUEST, REQUEST_DTL 테이블에 대한 구조를 보여줍니다. 테이블을 수정하실 필요는 없습니다.
DESC REQUEST;
DESC REQUEST_DTL;

-- 1. 요청상태가 FAILED인 요청 데이터를 조회하는 쿼리를 작성해보세요.
SELECT request_id FROM REQUEST WHERE request_status = 'FAILED';

-- 2. 위에서 작성한 쿼리를 서브쿼리로 이용하여 REQUEST_DTL 테이블에서 요청 상세를 조회하는 쿼리를 작성해보세요.
SELECT request_dtl_id, request_id, request_name, request_content 
FROM REQUEST_DTL 
WHERE request_id IN (SELECT request_id FROM REQUEST WHERE request_status = 'FAILED');
