DROP TABLE IF EXISTS data_mart;


CREATE TABLE data_mart AS
SELECT
    o.order_id,
    o.total_amount AS order_total,
    o.status,
    o.order_date,
    CONCAT(u.first_name, " ", u.last_name) as full_name,
    u.email,
    u.phone,
    u.loyalty_status,
    p.name as product_name,
    pc.name as category_name
FROM
    orders o
JOIN
    users u ON o.user_id = u.user_id
LEFT JOIN
    orderDetails od ON o.order_id = od.order_id
LEFT JOIN
    products p ON od.product_id = p.product_id
LEFT JOIN
    productCategories pc ON p.category_id = pc.category_id;