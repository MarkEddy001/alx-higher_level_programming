-- Creates the table force_name.
-- force_name description: id INT, name VARCHAR(256) can’t be null
-- database name will be passed as an argument of the mysql command
CREATE TABLE IF NOT EXISTS `force_name` (
    `id`   INT,
    `name` VARCHAR(256) NOT NULL
);
