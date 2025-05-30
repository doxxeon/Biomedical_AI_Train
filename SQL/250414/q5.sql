CREATE TABLE MEMBER(
  	mentee_id		INT NOT NULL	PRIMARY KEY,
  	mento_id		INT
);


INSERT INTO MEMBER VALUES
(1000, NULL),
(1001, NULL),
(1002, 1000),
(1003, 1001),
(1004, 1000),
(1005, 1002),
(1006, 1003),
(1007, 1004),
(1008, 1002),
(1009, 1005),
(1010, 1006),
(1011, 1010);

-- WITH RECURSIVE 를 이용하여 계층형 질의를 작성해보세요.
WITH RECURSIVE CTE(mentee_id, mento_id, lvl)
AS (
    SELECT mentee_id, mento_id, 0 AS lvl
    FROM MEMBER
    WHERE mento_id IS NULL
    UNION ALL
    SELECT m.mentee_id, m.mento_id, cte.lvl + 1
    FROM MEMBER m
    JOIN CTE cte 
    ON m.mento_id = cte.mentee_id
)
SELECT mentee_id, mento_id, lvl
FROM CTE
ORDER BY mentee_id, lvl;