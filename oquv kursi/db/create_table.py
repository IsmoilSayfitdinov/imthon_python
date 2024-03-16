
from db_connect import Dbconnect

def create_table():

    customers = """
        CREATE TABLE cutomers(
            cutomer_id SERIAL PRIMARY KEY,
            first_name VARCHAR(20),
            last_name VARCHAR(20),
            username VARCHAR(20),
            password VARCHAR(20),
            email VARCHAR(90),
            bio VARCHAR(60),
            headline VARCHAR(60),
            phone VARCHAR(40),
            created_at TIMESTAMP DEFAULT now())
    """

    mentor = """
        CREATE TABLE mentor(
            mentor_id SERIAL PRIMARY KEY,
            first_name VARCHAR(20),
            last_name VARCHAR(20),
            username VARCHAR(20),
            password VARCHAR(20),
            email VARCHAR(90),
            bio VARCHAR(100),
            headline VARCHAR(100),
            phone VARCHAR(40),
            created_at TIMESTAMP DEFAULT now()
        )
    """

    statuses = """
        CREATE TABLE status(
            status_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            created_at TIMESTAMP DEFAULT now()
        )
    """

    languages = """
        CREATE TABLE languages(
            language_id SERIAL PRIMARY KEy,
            name VARCHAR(30),
            created_at TIMESTAMP DEFAULT now()
        )
    """

    courses = """
        CREATE TABLE courses(
            course_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            description TEXT,
            raiting FLOAT,
            student_bokking_courses INT,
            price NUMERIC,
            status_courses INT REFERENCES status(status_id),
            language_courses INT REFERENCES languages(language_id),
            mentors_courses INT REFERENCES mentor(mentor_id),
            created_at TIMESTAMP DEFAULT now()
        )
    """

    specality = """
        CREATE TABLE specality(
            specality_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
             created_at TIMESTAMP DEFAULT now()
        )
    """

    spectality_cpourses = """
        CREATE TABLE spectality_cpourses(
            spectality_courses_id SERIAL PRIMARY KEY,
            specality INT REFERENCES specality(specality_id),
            courses INT REFERENCES courses(course_id),
            created_at TIMESTAMP DEFAULT now()
        )
    """

    card_type = """
            CREATE TABLE card_type(
                card_type_id SERIAL PRIMARY KEY,
                name VARCHAR(20),
                created_at TIMESTAMP DEFAULT now()
            )
        """

    payments = """
        CREATE TABLE payment(
            payment_id SERIAL PRIMARY KEY,
            amount INT,
            card INT REFERENCES card_type(card_type_id),
            customer INT REFERENCES cutomers(cutomer_id),
            created_at TIMESTAMP DEFAULT now()
        )
    """



    moduls = """
        CREATE TABLE moduls(
            modul_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            courses INT REFERENCES courses(course_id),
            lessons_count INT,
            created_at TIMESTAMP DEFAULT now()
        )
    """

    lessons = """
        CREATE TABLE lessons(
            lesson_id SERIAL PRIMARY KEY,
            name VARCHAR(20),
            moduls INT REFERENCES moduls(modul_id),
            created_at TIMESTAMP DEFAULT now()
        )
    """


    data ={
        "customers": customers,
        "mentor": mentor,
        "statuses": statuses,
        "languages": languages,
        "courses": courses,
        "specality": specality,
        "spectality_cpourses": spectality_cpourses,
        "card_type": card_type,
        "payments": payments,
        "moduls": moduls,
        "lessons": lessons
    }

    for i in data:
        print(f"{i}: {Dbconnect.connect(data[i], "create")}")



if __name__ == "__main__":
    create_table()