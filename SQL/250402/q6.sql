-- 아래 테이블을 직접 수정하지는 않습니다.
CREATE TABLE kickboard(
    member_id       VARCHAR(16)  NOT NULL,
    member_name     VARCHAR(16)  NOT NULL,
    member_birthday DATE,
    id              VARCHAR(16)  NOT NULL,
    brand           VARCHAR(16)  NOT NULL,   
    rental_location VARCHAR(32)  NOT NULL,
    rental_time     TIME, 
    price           INT          DEFAULT 0,
    CONSTRAINT id_unique UNIQUE (id),
    CONSTRAINT member_birthday_check CHECK (member_birthday < '2000-01-01'),
    CONSTRAINT rental_time_check CHECK(rental_time < '01:00:00')
);

-- kickboard 테이블에 제약 조건을 추가 및 삭제하세요.
ALTER TABLE kickboard
ADD CONSTRAINT member_id UNIQUE (member_id),

ALTER TABLE kickboard DROP CONSTRAINT rental_time_check;

ALTER TABLE kickboard
ALTER price SET DEFAULT 1000;


-- 제약 조건이 올바르게 설정되었는지 직접 데이터를 넣어보세요.
-- INSERT INTO kickboard(member_id, member_name, member_birthday, id, brand, rental_location, rental_time, price)
-- VALUES('kmax6', '김민준', '1989-03-09', '7YWC', 'boardkick', '서울시 관악구 신림동', '00:05:25', 4700);
-- INSERT INTO kickboard(member_id, member_name, member_birthday, id, brand, rental_location, rental_time, price)
-- VALUES('kmax6', '이서연', '1999-01-01', 'JXAN', 'willgo', '서울시 동작구 대방동', '00:09:00', 7200);
