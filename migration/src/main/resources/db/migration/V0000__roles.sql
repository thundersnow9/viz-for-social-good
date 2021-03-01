-- create role readonly login;
-- create role readwrite login;

alter default privileges for role merrowa
    grant select on tables to readonly;

alter default privileges for role merrowa
    grant select, insert, update, delete on tables to readwrite;

alter default privileges for role merrowa
    grant usage on schemas to readonly;
