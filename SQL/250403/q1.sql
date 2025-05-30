create table if not exists book(
    id int not null,
    title varchar(64) not null,
    author varchar(16),
    publisher varchar(32),
    date_received date,
    primary key (id)
);


insert into book values(1000, 'Romeo and Juliet', 'William Shakespeare', null, '2012-04-01');
insert into book values(1001, 'Don Quixote', 'Miguel de Cervantes Saavedra', null, '2015-03-31');
insert into book values(1002, 'The Little Prince', 'Antoine de Saint-Exupery', null, '2018-12-21');
insert into book values(1003, 'Harry Potter and the Philosophers Stone', 'Joanne Kathleen Rowling', 'Bloomsbury Publishing', '2017-06-26');
insert into book values(1004, 'The Lord of the Rings', 'John Ronald Reuel Tolkien', 'Allen & Unwin', '2014-07-29');


SELECT title, author FROM book;