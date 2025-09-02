**Authors**
    Breckin and Steven

**Overview**
    This repository contains the first version of our College Database design using MySQL Workbench (EER Diagram + Forward Engineering).
    It models a simplified college environment with students, faculty, admins, courses, semesters, rooms, enrollment, and grades.

**The database includes the following core entities:**
    People – stores all individuals (students, admins, faculty) with roles.
    Departments – academic departments offering courses.
    Semesters – academic terms (e.g., Fall 2025).
    Courses – connected to a semester, section, and assigned faculty.
    Rooms – classrooms with seating capacity constraints.
    Enrollment – mapping of students to courses.
    Letter Grades – assigned to students through enrollment records.
    Each table includes primary keys, foreign keys, unique constraints, and not-null requirements to maintain integrity.
