-- select customer_number
-- from orders
-- group by customer_number
-- order by count(order_number) desc
-- limit 0, 1;

select customer_number
from (
    select customer_number, count(*) as cnt
    from orders
    group by customer_number
) t
where cnt = (
    select max(cnt)
    from (
        select count(*) as cnt
        from orders
        group by customer_number
    ) c
);
