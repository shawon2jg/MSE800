CREATE TABLE student (
    student_id 		VARCHAR(4) 		PRIMARY KEY,
    first_name 		VARCHAR(50) 	NOT NULL,
    last_name 		VARCHAR(50) 	NOT NULL,
    email 			VARCHAR(100) 	UNIQUE NOT NULL,
    dob 			DATE,
    address 		VARCHAR(100),
    contact_no 		VARCHAR(15),
    enrollment_date DATE 			NOT NULL,
    major 			VARCHAR(50)
);

CREATE TABLE course (
    course_code 	VARCHAR(6) 		PRIMARY KEY,
    title 			VARCHAR(100) 	NOT NULL,
    description 	VARCHAR(100),
    credit_hours 	INT 			NOT NULL,
    department 		VARCHAR(50) 	NOT NULL,
    prerequisite 	VARCHAR(10),
    --FOREIGN KEY (prerequisite) REFERENCES course(course_code)
);

CREATE TABLE lecturer (
    lecturer_id 	VARCHAR(10) 	PRIMARY KEY,
    first_name 		VARCHAR(50) 	NOT NULL,
    last_name 		VARCHAR(50) 	NOT NULL,
    email 			VARCHAR(100) 	UNIQUE NOT NULL,
    department 		VARCHAR(50) 	NOT NULL,
    office_location VARCHAR(20),
    contact_no		VARCHAR(15),
    join_date 		DATE 			NOT NULL
);

CREATE TABLE class (
    class_id 			VARCHAR(15) PRIMARY KEY,
    course_code 		VARCHAR(10) NOT NULL,
    lecturer_id 		VARCHAR(10) NOT NULL,
    semester 			VARCHAR(10) NOT NULL,  -- e.g., 'Fall', 'Spring', 'Summer'
	section 			VARCHAR(1) 	NOT NULL,  
    year 				INT 		NOT NULL,
    room_number 		VARCHAR(10),    
    max_capacity 		INT,
    current_enrollment 	INT 		DEFAULT 0,
    FOREIGN KEY (course_code) REFERENCES course(course_code),
    FOREIGN KEY (lecturer_id) REFERENCES lecturer(lecturer_id),
    CHECK (current_enrollment <= max_capacity)
);

CREATE TABLE enrollment (
    student_id 		VARCHAR(10) NOT NULL,
    class_id 		VARCHAR(15) NOT NULL,
    enrollment_date DATE 		NOT NULL,
    grade 			VARCHAR(2),
    status 			VARCHAR(20) DEFAULT 'Enrolled',  -- e.g., 'Enrolled', 'Withdrawn', 'Completed'
    PRIMARY KEY (student_id, class_id),
    FOREIGN KEY (student_id) REFERENCES student(student_id),
    FOREIGN KEY (class_id) REFERENCES class(class_id)
);