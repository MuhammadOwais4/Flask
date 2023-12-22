CREATE TABLE customer (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    dob DATE,
    phone VARCHAR(15) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    email VARCHAR(255),
    address VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(50),
    postal_code VARCHAR(10)
);
/* "service" table: */
CREATE TABLE service (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    description TEXT
);

/* Order */
CREATE TABLE order (
    id INT PRIMARY KEY,
    created_at TIMESTAMP NOT NULL,
    customer_id INT NOT NULL,
    service_id INT NOT NULL,
    quantity INT,
    total_amount DECIMAL(10, 2),
    status VARCHAR(20)
);
