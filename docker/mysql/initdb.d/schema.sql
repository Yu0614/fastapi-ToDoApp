# users table
CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL,
    age INT,
    PRIMARY KEY (id)
);

# todos table
CREATE TABLE todos (
    id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    place VARCHAR(255),
    url VARCHAR(255),
    memo VARCHAR(255),
    start_date DATETIME,
    end_date DATETIME,
    PRIMARY KEY (id)
);