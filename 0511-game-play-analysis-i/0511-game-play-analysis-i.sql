-- select player_id, event_date as first_login
-- from (
--     select player_id, event_date,
--         rank() over (partition by player_id order by event_date) as rnk
--     from activity
-- ) a
-- where rnk = 1;

select player_id, min(event_date) as first_login
from activity
group by player_id;
