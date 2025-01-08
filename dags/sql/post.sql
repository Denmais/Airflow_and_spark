BEGIN;

CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(15),
    registration_date DATE DEFAULT CURRENT_DATE,
    loyalty_status VARCHAR(20) CHECK (loyalty_status IN ('Gold', 'Silver'))
);

CREATE TABLE IF NOT EXISTS productCategories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    parent_category_id INT REFERENCES ProductCategories(category_id)
);

CREATE TABLE IF NOT EXISTS products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(60) NOT NULL,
    description TEXT,
    category_id INT REFERENCES ProductCategories(category_id),
    price NUMERIC NOT NULL,
    stock_quantity INT DEFAULT 0,
    creation_date DATE DEFAULT CURRENT_DATE
);

CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    order_date DATE DEFAULT CURRENT_DATE,
    total_amount NUMERIC,
    status VARCHAR(20) CHECK (status IN ('Done', 'Created', 'Completed', 'Deleted')),
    delivery_date DATE
);

CREATE TABLE if not exists orderDetails (
    order_detail_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(order_id),
    product_id INT REFERENCES products(product_id),
    quantity INT NOT NULL,
    price_per_unit NUMERIC NOT NULL,
    total_price NUMERIC DEFAULT 100
);

-- Генератор гпт
INSERT INTO users (first_name, last_name, email, phone, loyalty_status) VALUES
('John', 'Doe', 'john.doe@example.com', '+1234567890', 'Gold'),
('Jane', 'Smith', 'jane.smith@example.com', '+0987654321', 'Silver'),
('Alice', 'Johnson', 'michael.johnson@example.com', '+1122334455', 'Gold'),
('Emily', 'Davis', 'emily.davis@example.com', '+2233445566', 'Gold'),
('William', 'Brown', 'william.brown@example.com', '+3344556677', 'Silver');


INSERT INTO productCategories (name, parent_category_id) VALUES
('Electronics', NULL),
('Mobile Phones', 1),
('Laptops', 1),
('Accessories', NULL),
('Chargers', 4);


INSERT INTO products (name, description, category_id, price, stock_quantity) VALUES
('Smartphone XYZ', 'Latest model smartphone with high-end features.', 2, 699.99, 50),
('Smartphone ABC', 'Affordable smartphone with great battery life.', 2, 299.99, 100),
('Gaming Laptop', 'Powerful laptop for gaming and professional use.', 3, 1299.99, 30),
('Business Laptop', 'Lightweight laptop suitable for business professionals.', 3, 899.99, 20),
('Wireless Charger', 'Fast wireless charger compatible with most devices.', 5, 49.99, 150),
('USB-C Charger', 'Universal USB-C charger for multiple devices.', 5, 19.99, 200);


INSERT INTO orders (user_id, total_amount, status, delivery_date) VALUES
(1, 2999.99, 'Completed', '2023-12-21'),
(2, 9199.99, 'Done', NULL),
(3, 2499.99, 'Created', NULL),
(4, 3799.99, 'Deleted', NULL),
(5, 2919.99, 'Completed', '2023-12-1');


INSERT INTO orderDetails (order_id, product_id, quantity, price_per_unit) VALUES
(1, 1, 1, 999.99),
(1, 2, 1, 6999.99),
(2, 1, 1, 999.99),
(3, 3, 1, 599.99),
(4, 4, 1, 4592.99),
(4, 6, 2, 1391.99),
(5, 5, 1, 3333.99);

COMMIT;