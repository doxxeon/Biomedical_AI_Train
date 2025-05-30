-- 대출,반납에 대한 정보를 user 테이블과 연결해 조회해 봅시다.


SELECT * FROM rental INNER JOIN user ON rental.user_id = user.id;