-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2022-11-20 01:07:33.953

-- tables
-- Table: buildings
CREATE TABLE buildings (
    name varchar(50)  NOT NULL,
    CONSTRAINT buildings_pk PRIMARY KEY (name)
);

-- Table: copy_keys
CREATE TABLE copy_keys (
    id serial  NOT NULL,
    issued_date date  NOT NULL,
    issued_time time  NOT NULL,
    hooks_id int  NOT NULL,
    is_loss boolean  NOT NULL,
    CONSTRAINT copy_keys_pk PRIMARY KEY (id,is_loss)
);

-- Table: door_type
CREATE TABLE door_type (
    name varchar(50)  NOT NULL,
    CONSTRAINT door_type_pk PRIMARY KEY (name)
);

-- Table: doors
CREATE TABLE doors (
    door_type_name varchar(50)  NOT NULL,
    rooms_num int  NOT NULL,
    rooms_buildings_name varchar(50)  NOT NULL,
    CONSTRAINT doors_pk PRIMARY KEY (door_type_name,rooms_num,rooms_buildings_name)
);

-- Table: employees
CREATE TABLE employees (
    name varchar(100)  NOT NULL,
    id serial  NOT NULL,
    CONSTRAINT employees_uk_1 UNIQUE (name) NOT DEFERRABLE  INITIALLY IMMEDIATE,
    CONSTRAINT employees_pk PRIMARY KEY (id)
);

-- Table: hook_lines
CREATE TABLE hook_lines (
    doors_door_type_name varchar(50)  NOT NULL,
    doors_rooms_num int  NOT NULL,
    doors_rooms_buildings_name varchar(50)  NOT NULL,
    hooks_id int  NOT NULL,
    CONSTRAINT hook_lines_pk PRIMARY KEY (doors_door_type_name,doors_rooms_num,doors_rooms_buildings_name,hooks_id)
);

-- Table: hooks
CREATE TABLE hooks (
    id serial  NOT NULL,
    CONSTRAINT hooks_pk PRIMARY KEY (id)
);

-- Table: key_requests
CREATE TABLE key_requests (
    request_id int  NOT NULL,
    rooms_num int  NOT NULL,
    rooms_buildings_name varchar(50)  NOT NULL,
    employees_id int  NOT NULL,
    request_date date  NOT NULL,
    copy_keys_id int  NOT NULL,
    copy_keys_is_loss boolean  NOT NULL,
    CONSTRAINT key_requests_pk PRIMARY KEY (request_id)
);

-- Table: loss
CREATE TABLE loss (
    loss_date date  NOT NULL,
    key_requests_request_id int  NOT NULL,
    loaned_date int  NOT NULL,
    CONSTRAINT loss_pk PRIMARY KEY (key_requests_request_id)
);

-- Table: returns
CREATE TABLE returns (
    return_date date  NOT NULL,
    key_requests_request_id int  NOT NULL,
    loaned_date int  NOT NULL,
    CONSTRAINT returns_pk PRIMARY KEY (key_requests_request_id)
);

-- Table: rooms
CREATE TABLE rooms (
    num int  NOT NULL,
    buildings_name varchar(50)  NOT NULL,
    CONSTRAINT rooms_uk_01 UNIQUE (num) NOT DEFERRABLE  INITIALLY IMMEDIATE,
    CONSTRAINT rooms_pk PRIMARY KEY (num,buildings_name)
);

-- foreign keys
-- Reference: copy_keys_hooks_fk_01 (table: copy_keys)
ALTER TABLE copy_keys ADD CONSTRAINT copy_keys_hooks_fk_01
    FOREIGN KEY (hooks_id)
    REFERENCES hooks (id)
    ON DELETE  RESTRICT 
    ON UPDATE  RESTRICT 
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: doors_door_type_fk_01 (table: doors)
ALTER TABLE doors ADD CONSTRAINT doors_door_type_fk_01
    FOREIGN KEY (door_type_name)
    REFERENCES door_type (name)
    ON DELETE  RESTRICT 
    ON UPDATE  RESTRICT 
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: doors_rooms_fk_01 (table: doors)
ALTER TABLE doors ADD CONSTRAINT doors_rooms_fk_01
    FOREIGN KEY (rooms_num, rooms_buildings_name)
    REFERENCES rooms (num, buildings_name)
    ON DELETE  RESTRICT 
    ON UPDATE  RESTRICT 
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: hok_lines_doors_fk_01 (table: hook_lines)
ALTER TABLE hook_lines ADD CONSTRAINT hok_lines_doors_fk_01
    FOREIGN KEY (doors_door_type_name, doors_rooms_num, doors_rooms_buildings_name)
    REFERENCES doors (door_type_name, rooms_num, rooms_buildings_name)
    ON DELETE  RESTRICT 
    ON UPDATE  RESTRICT 
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: hook_lines_hooks_fk_01 (table: hook_lines)
ALTER TABLE hook_lines ADD CONSTRAINT hook_lines_hooks_fk_01
    FOREIGN KEY (hooks_id)
    REFERENCES hooks (id)
    ON DELETE  RESTRICT 
    ON UPDATE  RESTRICT 
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: key_requests_copy_keys_fk_01 (table: key_requests)
ALTER TABLE key_requests ADD CONSTRAINT key_requests_copy_keys_fk_01
    FOREIGN KEY (copy_keys_id, copy_keys_is_loss)
    REFERENCES copy_keys (id, is_loss)
    ON DELETE  RESTRICT 
    ON UPDATE  RESTRICT 
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: key_requests_employees_fk_01 (table: key_requests)
ALTER TABLE key_requests ADD CONSTRAINT key_requests_employees_fk_01
    FOREIGN KEY (employees_id)
    REFERENCES employees (id)
    ON DELETE  RESTRICT 
    ON UPDATE  RESTRICT 
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: key_requests_rooms_fk_01 (table: key_requests)
ALTER TABLE key_requests ADD CONSTRAINT key_requests_rooms_fk_01
    FOREIGN KEY (rooms_num, rooms_buildings_name)
    REFERENCES rooms (num, buildings_name)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: loss_key_requests (table: loss)
ALTER TABLE loss ADD CONSTRAINT loss_key_requests
    FOREIGN KEY (key_requests_request_id)
    REFERENCES key_requests (request_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: returns_key_requests (table: returns)
ALTER TABLE returns ADD CONSTRAINT returns_key_requests
    FOREIGN KEY (key_requests_request_id)
    REFERENCES key_requests (request_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: rooms_buildings_fk_01 (table: rooms)
ALTER TABLE rooms ADD CONSTRAINT rooms_buildings_fk_01
    FOREIGN KEY (buildings_name)
    REFERENCES buildings (name)
    ON DELETE  RESTRICT 
    ON UPDATE  RESTRICT 
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

