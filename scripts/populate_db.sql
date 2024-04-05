INSERT INTO employees (id, name, email, birthdate, phone, avatar)
VALUES
    ("57415264-8752-474d-b02f-0d141ef3e205", 'Alice Smith', 'alice@example.com', '1990-05-15', '123-456-7890', 'avatar1.jpg'),
    ("086e0fc2-edfb-40b5-9124-d112b24cba6b", 'Bob Johnson', 'bob@example.com', '1985-09-20', '987-654-3210', 'avatar2.jpg'),
    ("0a256ec9-93d4-4b0e-be07-74be08113410", 'Charlie Brown', 'charlie@example.com', '1993-02-10', '555-555-5555', 'avatar3.jpg');

INSERT INTO rooms (id, name)
VALUES
    ("fc6abd92-bca6-498e-a25b-663d268bca94", 'Conference Room 1'),
    ("51aec34a-e23b-4062-bb75-e252a53ce7e3", 'Conference Room 2'),
    ("0e1c39ba-1ba1-4efa-ad01-ddd97e50c38e", 'Board Room');

INSERT INTO events (id, name, roomid, start, finish)
VALUES
    ("7db3c6e4-6e9a-466d-832a-9f2793af09f3", 'Meeting 1', "fc6abd92-bca6-498e-a25b-663d268bca94", '2024-04-05 09:00', '2024-04-05 10:00'),
    ("9553c5d0-1e99-425e-be49-b903dbfdc5c6", 'Meeting 2', "51aec34a-e23b-4062-bb75-e252a53ce7e3", '2024-04-05 11:00', '2024-04-05 12:00'),
    ("ae1aeca5-5a47-4608-b994-c2d8eee84f2a", 'Conference', "0e1c39ba-1ba1-4efa-ad01-ddd97e50c38e", '2024-04-06 10:00', '2024-04-06 17:00');

INSERT INTO employees_events (employeeid, eventid)
VALUES
    ((SELECT id FROM employees WHERE name = 'Alice Smith'), (SELECT id FROM events WHERE name = 'Meeting 1')),
    ((SELECT id FROM employees WHERE name = 'Bob Johnson'), (SELECT id FROM events WHERE name = 'Meeting 1')),
    ((SELECT id FROM employees WHERE name = 'Bob Johnson'), (SELECT id FROM events WHERE name = 'Meeting 2')),
    ((SELECT id FROM employees WHERE name = 'Charlie Brown'), (SELECT id FROM events WHERE name = 'Conference'));