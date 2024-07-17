CREATE USER grocery_user WITH PASSWORD '123' CREATEDB;
\c postgres grocery_user
CREATE DATABASE groceryshop;
\c groceryshop