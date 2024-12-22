CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    userName VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL
);

CREATE TABLE Employees (
    id SERIAL PRIMARY KEY,
    firstName VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL,
    salary NUMERIC(10, 2) NOT NULL,
    department VARCHAR(255) NOT NULL
);

CREATE TABLE Teachers (
    id SERIAL PRIMARY KEY,
    firstName VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL,
    department VARCHAR(255) NOT NULL
);

CREATE TABLE Managers (
    id SERIAL PRIMARY KEY,
    firstName VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL,
    department VARCHAR(255) NOT NULL
);

CREATE TABLE Students (
    id SERIAL PRIMARY KEY,
    firstName VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    major VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    gpa DECIMAL(3, 2) NOT NULL
);

CREATE TABLE Admins (
    id SERIAL PRIMARY KEY,
    firstName VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL
);

CREATE TABLE Courses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    credits INT NOT NULL,
    type VARCHAR(50) NOT NULL,
    availableSlots INT NOT NULL DEFAULT 30
);

CREATE TABLE Marks (
    id SERIAL PRIMARY KEY,
    student_id INT REFERENCES Students(id),
    course_id INT REFERENCES Courses(id),
    mark INT NOT NULL
);

CREATE TABLE Lessons (
    id SERIAL PRIMARY KEY,
    topic VARCHAR(255) NOT NULL,
    lessonDate DATE NOT NULL,
    room VARCHAR(50) NOT NULL,
    course_id INT REFERENCES Courses(id)
);

CREATE TABLE Librarians (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE Books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    code VARCHAR(50) UNIQUE NOT NULL,
    isAvailable BOOLEAN DEFAULT TRUE
);

CREATE TABLE BorrowedBooks (
    id SERIAL PRIMARY KEY,
    book_id INT REFERENCES Books(id) ON DELETE CASCADE,
    student_id INT REFERENCES Students(id) ON DELETE CASCADE,
    borrow_date DATE NOT NULL,
    due_date DATE NOT NULL,
    return_date DATE
);

CREATE TABLE Researchers (
    id SERIAL PRIMARY KEY,
    firstName VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL,
    department VARCHAR(255) NOT NULL
);

CREATE TABLE ResearchProjects (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    lead_researcher_id INT REFERENCES Researchers(id)
);

CREATE TABLE ResearchPapers (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    journal VARCHAR(255),
    citations INT DEFAULT 0,
    pages VARCHAR(50),
    doi VARCHAR(255),
    publicationDate DATE,
    author_id INT REFERENCES Researchers(id)
);

CREATE TABLE Complaints (
    id SERIAL PRIMARY KEY,
    student_id INT REFERENCES Students(id) ON DELETE CASCADE,
    teacher_id INT REFERENCES Teachers(id) ON DELETE CASCADE,
    urgency_level VARCHAR(50) NOT NULL,
    complaint TEXT NOT NULL
);

CREATE TABLE News (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    publication_date DATE NOT NULL
);

CREATE TABLE Messages (
    id SERIAL PRIMARY KEY,
    sender_id INT REFERENCES Users(id),
    receiver_id INT REFERENCES Users(id),
    content TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO Users (userName, email, password, role) VALUES
('admin', 'admin@example.com', 'adminpass', 'ADMIN'),
('user1', 'user1@example.com', 'user1pass', 'USER');

INSERT INTO Employees (firstName, lastName, salary, department) VALUES
('John', 'Smith', 60000, 'HR'),
('Jane', 'Doe', 65000, 'IT');

INSERT INTO Teachers (firstName, lastName, department) VALUES
('Alice', 'Brown', 'Computer Science'),
('Bob', 'White', 'Mathematics');

INSERT INTO Managers (firstName, lastName, department) VALUES
('Charlie', 'Black', 'Finance'),
('David', 'Green', 'Operations');

INSERT INTO Students (firstName, lastName, email, major, year, gpa) VALUES
('Alice', 'Wonderland', 'alice@example.com', 'Computer Science', 2, 3.9),
('Bob', 'Builder', 'bob@example.com', 'Engineering', 3, 3.7);

INSERT INTO Admins (firstName, lastName) VALUES
('Admin', 'One'),
('Admin', 'Two');

INSERT INTO Courses (name, credits, type, availableSlots) VALUES
('Data Structures', 4, 'MAJOR', 25),
('Ethics in Computing', 3, 'MINOR', 20);

INSERT INTO Marks (student_id, course_id, mark) VALUES
(1, 1, 85),
(2, 2, 90);

INSERT INTO Lessons (topic, lessonDate, room, course_id) VALUES
('Introduction to Programming', '2024-01-10', 'Room 101', 1),
('Software Development Life Cycle', '2024-01-15', 'Room 102', 2);

INSERT INTO Librarians (name) VALUES
('Librarian One'),
('Librarian Two');

INSERT INTO Books (title, author, code, isAvailable) VALUES
('Introduction to Algorithms', 'Thomas H. Cormen', 'B001', TRUE),
('Clean Code', 'Robert C. Martin', 'B002', TRUE);

INSERT INTO Researchers (firstName, lastName, department) VALUES
('Eve', 'Davis', 'Physics'),
('Frank', 'Miller', 'Chemistry');

INSERT INTO ResearchProjects (title, description, lead_researcher_id) VALUES
('AI in Healthcare', 'Research project on AI applications in healthcare', 1),
('Renewable Energy', 'Research project on renewable energy sources', 2);

INSERT INTO ResearchPapers (title, journal, citations, pages, doi, publicationDate, author_id) VALUES
('Quantum Computing', 'Journal of Physics', 50, '1-10', '10.1234/quantum2024', '2024-01-01', 1),
('Organic Chemistry', 'Chemistry Today', 30, '11-20', '10.5678/chem2024', '2024-01-05', 2);

INSERT INTO News (title, content, publication_date) VALUES
('New Library Opens', 'The new library building has been inaugurated.', '2024-01-01'),
('Research Grant Awarded', 'The university has been awarded a research grant.', '2024-01-05');

INSERT INTO Messages (sender_id, receiver_id, content) VALUES
(1, 2, 'Hello, can you help me with my assignment?'),
(2, 1, 'Sure, I will help you.');
