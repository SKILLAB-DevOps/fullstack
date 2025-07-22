CREATE TABLE users (id INT PRIMARY KEY, name VARCHAR(100));

INSERT INTO public.users (id, name)
VALUES (1, 'Alice'),
       (2, 'Bob'),
       (3, 'Charlie'),
       (4, 'Diana'),
       (5, 'Eve');