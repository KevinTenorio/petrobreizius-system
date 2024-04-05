create table employees
(
    id        uuid    not null
        primary key,
    name      varchar not null,
    email     varchar,
    birthdate date,
    phone     varchar,
    avatar    varchar
);

alter table employees
    owner to postgres;

create table rooms
(
    id   uuid    not null
        constraint rooms_pk
            primary key,
    name varchar not null
);

alter table rooms
    owner to postgres;

create table events
(
    id     uuid    not null
        constraint events_pk
            primary key,
    name   varchar not null,
    roomid uuid
        constraint events_rooms_id_fk
            references rooms,
    start  varchar not null,
    finish varchar not null
);

alter table events
    owner to postgres;

create table employees_events
(
    employeeid uuid not null
        constraint employee
            references employees,
    eventid    uuid not null
        constraint event
            references events,
    constraint employees_events_pk
        primary key (employeeid, eventid)
);

alter table employees_events
    owner to postgres;

