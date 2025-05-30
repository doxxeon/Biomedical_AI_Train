create table if not exists sale(
    id int not null,
    name varchar(16) not null,
    amount int,
    revenue int,
    primary key(id)
);

insert into sale values(1, 'tea', 10, 9000);
insert into sale values(2, 'tea', 5, 4500);
insert into sale values(3, 'card', 1, 10000);
insert into sale values(4, 'clock', 1, 180000);
insert into sale values(5, 'carrot', 100, 90000);
insert into sale values(6, 'onion', 20, 36000);
insert into sale values(7, 'carrot', 10, 9000);
insert into sale values(8, 'tea', 1, 900);
insert into sale values(9, 'onion', 10, 18000);
insert into sale values(10, 'clock', 1, 180000);
insert into sale values(11, 'umbrella', 5, 50000);


SELECT name, SUM(amount) FROM sale GROUP BY name HAVING SUM(revenue) >= 50000;