CREATE TABLE Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    course TEXT NOT NULL
);

CREATE TABLE Tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    status TEXT NOT NULL
);

INSERT INTO Users (name, email) VALUES ('John', 'john@email.com');
INSERT INTO Students (name, course) VALUES ('Alice', 'Python');
INSERT INTO Tasks (title, status) VALUES ('Complete Internship Task', 'Pending');