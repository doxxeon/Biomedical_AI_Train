-- kickboard 테이블의 id 속성에 PRIMARY KEY 제약 조건을 추가하세요.
CREATE TABLE kickboard(
    member_id       VARCHAR(16)  NOT NULL UNIQUE,
    member_name     VARCHAR(16)  NOT NULL,
    member_birthday DATE,
    id              VARCHAR(16)  PRIMARY KEY,
    brand           VARCHAR(16)  NOT NULL,   
    rental_location VARCHAR(32)  NOT NULL,
    rental_time     TIME, 
    price           INT          DEFAULT 1000,
    CONSTRAINT id_unique UNIQUE (id),
    CONSTRAINT member_birthday_check CHECK (member_birthday < '2000-01-01')
);

-- id 속성의 Key가 PRI로 설정되는 것을 확인하세요. 아래 코드는 수정하면 안됩니다.
DESC kickboard;

-- 기본키를 삽입하지 않으면 어떻게 되는지 확인해보세요.
-- INSERT INTO kickboard(member_id, member_name, member_birthday, brand, rental_location, rental_time, price)
-- VALUES('kmax6', '김민준', '1989-03-09', 'boardkick', '서울시 관악구 신림동', '00:05:25', 4700);
