-- Prepares the SQL server for development

CREATE DATABASE IF NOT EXISTS pantrybuddy_db;

-- Create user if not exists
CREATE USER IF NOT EXISTS 'pantrybuddy_dev'@'localhost' IDENTIFIED BY 'password';

-- Grant appropriate privileges
GRANT SELECT ON performance_schema.* TO 'pantrybuddy_dev'@'localhost';
GRANT ALL PRIVILEGES ON pantrybuddy_db.* TO 'pantrybuddy_dev'@'localhost';
FLUSH PRIVILEGES;
