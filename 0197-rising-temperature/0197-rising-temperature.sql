select w1.id
from weather w1
join weather w2
on Date_Sub(w1.recordDate, INTERVAL 1 DAY) = w2.recordDate
where w1.temperature > w2.temperature;
