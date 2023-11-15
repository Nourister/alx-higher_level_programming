-- a script that creates the database hbtn_0d_2 and the user_0d_2
-- creates database
CREATE DATABSE IF NOT EXISTS hbtn_0d_2;
--Creates the user
CREATE USER IF NOT EXISTS user_0d_2@localhost
IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2. * TO user_0d_2@localhost;
