CREATE TABLE "meteorites" (
	id serial PRIMARY KEY,
    "name" varchar(50)   NOT NULL,
    "class" varchar(40)   NOT NULL,
    "mass" numeric  NOT NULL,
    "fall" varchar(10)   NOT NULL,
    "year" integer  NOT NULL,
    "latitude" double precision   NOT NULL,
    "longitude" double precision   NOT NULL,
    "hemisphere" varchar(15)
);
drop table "meteorites";

select * from meteorites;