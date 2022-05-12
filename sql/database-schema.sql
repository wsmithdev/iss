-- Link to the database schema
-- https://app.quickdatabasediagrams.com/#/d/RE8SZO


-- User table -- 
CREATE TABLE "user" (
    "id" int   NOT NULL,
    "first_name" string   NOT NULL,
    "last_name" string   NOT NULL,
    "email" string   NOT NULL,
    "password" string   NOT NULL,
    "location_id" int   NOT NULL,
    "notification_method_id" int   NOT NULL,
    CONSTRAINT "pk_user" PRIMARY KEY (
        "id"
     )
);

-- Location table --
CREATE TABLE "location" (
    "id" int   NOT NULL,
    "lat" float   NOT NULL,
    "long" float   NOT NULL,
    CONSTRAINT "pk_location" PRIMARY KEY (
        "id"
     )
);

-- Notification method table --
CREATE TABLE "notification_method" (
    "id" int   NOT NULL,
    "method" string   NOT NULL,
    CONSTRAINT "pk_notification_method" PRIMARY KEY (
        "id"
     )
);

ALTER TABLE "user" ADD CONSTRAINT "fk_user_location_id" FOREIGN KEY("location_id")
REFERENCES "location" ("id");

ALTER TABLE "user" ADD CONSTRAINT "fk_user_notification_method_id" FOREIGN KEY("notification_method_id")
REFERENCES "notification_method" ("id");