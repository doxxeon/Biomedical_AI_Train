create table if not exists book(
    id varchar(32) not null,
    title varchar(64) not null,
    author varchar(64),
    publisher varchar(32),
    date_received date,
    primary key (id)
);

create table if not exists user(
    id int not null,
    name varchar(16) not null,
    email varchar(32),
    phone varchar(16),
    address text,
    primary key (id)
);

create table if not exists rental(
    id int not null,
    book_id varchar(32) not null,
    user_id int not null,
    rental_begin_date datetime,
    rental_end_date datetime,
    primary key (id),
    foreign key (book_id) references book(id),
    foreign key (user_id) references user(id) 
);

insert into book values(1000, 'Romeo and Juliet', 'William Shakespeare', null, '2012-04-01');
insert into book values(1001, 'Don Quixote', 'Miguel de Cervantes Saavedra', null, '2015-03-31');
insert into book values(1002, 'The Little Prince', 'Antoine de Saint-Exupery', null, '2018-12-21');
insert into book values(1003, 'Harry Potter and the Philosopher\'s Stone', 'Joanne Kathleen Rowling', 'Bloomsbury Publishing', '2017-06-26');
insert into book values(1004, 'The Lord of the Rings', 'John Ronald Reuel Tolkien', 'Allen & Unwin', '2014-07-29');
insert into book values(1005, 'Hobbit', 'John Ronald Reuel Tolkien', 'Allen & Unwin', '2014-07-29');
insert into book values(1006, 'Alice\'s Adventures in Wonderland', 'Lewis Carroll', 'Macmillan ', '2015-11-26');
insert into book values(1007, 'The Old Man and the Sea', 'Ernest Miller Hemingway', 'Charles Scribner\'s Sons', '2014-11-02');
insert into book values(1008, 'The Great Gatsby', 'Francis Scott Key Fitzgerald', null, '2019-01-12');
insert into book values(1009, 'Harry Potter and the Deathly Hallows', 'Joanne Kathleen Rowling', 'Bloomsbury Publishing', '2017-07-21');

insert into `user` values(1000, 'Elice', 'elice@elice.com', '010-1234-5678', '101-23 CeileDong');
insert into `user` values(1001, 'Cheshire', 'cheshire@elice.com', '010-8765-4321', '101-24 CeileDong');
insert into `user` values(1002, 'Dodo', 'dodo@elice.com', '010-1111-2222', '100-11 CeileDong');
insert into `user` values(1003, 'Caterpillar', 'caterpillar@elice.com', '010-1212-3434', '100-12 CeileDong');
insert into `user` values(1004, 'Hatter', 'hatter@elice.com', '010-1357-2468', '103-34 CeileDong');

insert into rental values(1000, 1000, 1000, '2018-10-30 15:30:00', '2018-10-31 13:00:00');
insert into rental values(1001, 1001, 1000, '2018-11-02 10:20:00', '2018-11-05 10:30:00');
insert into rental values(1002, 1000, 1001, '2018-11-02 11:00:00', '2018-11-04 12:00:00');
insert into rental values(1003, 1006, 1000, '2018-11-10 18:00:00', '2018-11-13 16:00:00');
insert into rental values(1004, 1009, 1000, '2018-11-16 15:40:00', '2018-11-23 10:30:00');
insert into rental values(1005, 1002, 1001, '2018-12-01 09:00:00', '2018-12-13 10:30:00');
insert into rental values(1006, 1003, 1003, '2018-12-15 13:15:00', '2019-01-01 09:00:00');
insert into rental values(1007, 1004, 1002, '2018-10-30 15:30:00', '2018-10-31 13:00:00');
insert into rental values(1008, 1006, 1002, '2019-01-02 14:00:00', '2019-01-03 11:30:00');
insert into rental values(1009, 1006, 1002, '2019-02-01 14:00:00', '2019-02-04 13:10:00');

-- rental테이블의 구조를 조회합니다. 수정하실 필요는 없습니다.
DESC rental;

-- 누가 몇권의 책을 빌려갔는지 조회해 봅시다.
SELECT user_id, COUNT(book_id) AS book_count FROM rental GROUP BY user_id;
SELECT user_id, count(*) from rental group by user_id;