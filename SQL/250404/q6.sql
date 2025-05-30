-- 판매기록을 product 테이블과 연결해 출력해 봅시다.
-- 이때 product테이블이 중심이 되도록 해 봅시다.
create table if not exists product(
    id int not null,
    name varchar(32) not null,
    stock int,
    expiration_date date,
    list_price int,
    selling_price int,
    discount_rate float,
    primary key(id)
);

create table if not exists sale(
    id int not null,
    product_id int not null,
    amount int,
    money int,
    foreign key (product_id) references product(id)
);

insert into product values(1, 'carrot', 100, '2019-04-10', 1000, 900, 0.9);
insert into product values(2, 'tea', 1000, '2020-02-10', 1000, 900, 0.9);
insert into product values(3, 'clock', 100, null, 200000, 180000, 0.9);
insert into product values(4, 'trump card', 100, null, 10000, 10000, 1);
insert into product values(5, 'onion', 100, '2019-04-11', 2000, 1800, 0.9);

insert into sale values(1, 1, 10, 9000);
insert into sale values(2, 1, 5, 4500);
insert into sale values(3, 4, 1, 10000);
insert into sale values(4, 3, 1, 180000);
insert into sale values(5, 2, 100, 90000);
insert into sale values(6, 5, 20, 36000);
insert into sale values(7, 2, 10, 9000);
insert into sale values(8, 1, 1, 900);
insert into sale values(9, 5, 10, 18000);
insert into sale values(10, 3, 1, 180000);

SELECT * FROM sale RIGHT JOIN product ON sale.product_id = product.id;