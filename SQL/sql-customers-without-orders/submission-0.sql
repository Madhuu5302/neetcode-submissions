-- Write your query below
select customers.name from customers LEFT JOIN orders
on customers.id = orders.customer_id 
where orders.customer_id IS NULL;