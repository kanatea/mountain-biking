-- For the purposes of this project, we will create a database named madeira_trails

-- DROP DATABASE IF EXISTS madeira_trails;

CREATE DATABASE madeira_trails
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United Kingdom.1252' --replace with what is registered on your machine
    LC_CTYPE = 'English_United Kingdom.1252'   --replace with what is registered on your machine
    LOCALE_PROVIDER = 'libc'                   --replace with what is registered on your machine
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

