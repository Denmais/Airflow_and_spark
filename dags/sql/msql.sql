CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(15),
    registration_date DATE,
    loyalty_status VARCHAR(20)
);

CREATE TABLE productCategories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    parent_category_id INT
);

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    category_id INT,
    price NUMERIC NOT NULL,
    stock_quantity INT DEFAULT 0,
    creation_date DATE
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    order_date DATE,
    total_amount NUMERIC,
    status VARCHAR(20),
    delivery_date DATE
);

CREATE TABLE orderDetails (
    order_detail_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT NOT NULL,
    price_per_unit NUMERIC NOT NULL,
    total_price NUMERIC
);