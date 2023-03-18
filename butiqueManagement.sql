create database boutique;
use boutique;
create table customer(cust_id int primary key,cust_name varchar(20),last_name varchar(20),cust_contact varchar(20),cust_adrs varchar(50),booked_prod varchar(20));
desc customer;
create table employee(emp_id varchar(5) primary key,emp_name varchar(20),emp_Lname varchar(20),emp_contact varchar(20),emp_adrs varchar(50));
desc employee;
create table product(prod_no varchar(10),prod_id varchar(20) primary key,prod_price int,prod_stock int);
desc product;
