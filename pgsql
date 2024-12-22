CREATE TABLE teachers (
   id SERIAL PRIMARY KEY,
   name VARCHAR(100) NOT NULL,
   teacher_type VARCHAR(50) NOT NULL,
   schedule VARCHAR(255) NOT NULL,
   research_field VARCHAR(255)
);
