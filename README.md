# viz-for-social-good

#### Initialize a fresh Postgres 13 database

Create a fresh database and initialize the superuser
```postgresql
create database merrowa;
create role merrowa login password --redacted;
alter role merrowa with superuser;
```

```properties
flyway.url=jdbc:postgresql://localhost:5435/merrowa?tcpKeepAlive=true
flyway.user=merrowa
flyway.schemas=public
```