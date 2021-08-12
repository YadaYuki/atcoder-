CREATE DATABASE IF NOT EXISTS recipe_app;
USE recipe_app;
CREATE TABLE IF NOT EXISTS users (
  uuid VARBINARY(16) NOT NULL PRIMARY KEY,
  name VARCHAR(100) NOT NULL
);
CREATE TABLE IF NOT EXISTS recipes (
  uuid VARBINARY(16) NOT NULL PRIMARY KEY,
  title VARCHAR(100) NOT NULL,
  user_id VARBINARY(16) NOT NULL
);
CREATE TABLE IF NOT EXISTS photo_reports (
  uuid VARBINARY(16) NOT NULL PRIMARY KEY,
  title VARCHAR(100) NOT NULL,
  recipe_id VARBINARY(16) references recipes(uuid),
  user_id VARBINARY(16) references users(uuid),
  UNIQUE (recipe_id, user_id)
);

INSERT INTO recipes(uuid,title,user_id)
VALUES ("6ccd780c-baba-1026-9564-0040f4311e29","テスト勉強","6ccd780c-baba-1026-9564-0040f4311e29");
-- CREATE TABLE IF NOT EXISTS user_recipe_repoted (
--   id integer primary key AUTO_INCREMENT,
--   recipe_id VARBINARY(16) references recipes(uuid),
--   user_id VARBINARY(16) references users(uuid)
-- );
-- CREATE DATABASE IF NOT EXISTS todo_app;
-- USE todo_app;
-- CREATE TABLE IF NOT EXISTS todos (
--   id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
--   title VARCHAR(256) NOT NULL,
--   created_at datetime default current_timestamp
-- ) ENGINE = InnoDB DEFAULT CHARSET = utf8;
-- INSERT INTO todos(title)
-- VALUES ("テスト勉強");
-- INSERT INTO todos(title)
-- VALUES ("テスト勉強");
-- INSERT INTO todos(title)
-- VALUES ("テスト勉強");