-- use this query if the table 'meteorites' already exists
drop table "meteorites";

-- this query is used for creating the table 
CREATE TABLE "meteorites" (
	id serial PRIMARY KEY,
    "name" varchar(50)   NOT NULL,
    "class" varchar(40)   NOT NULL,
    "mass" numeric  NOT NULL,
    "fall" varchar(10)   NOT NULL,
    "year" integer  NOT NULL,
    "latitude" double precision   NOT NULL,
    "longitude" double precision   NOT NULL
);

-- use this query to check that the data was imported correctly after importing the 'clean_meteorite_data.csv' file 
select * from meteorites