from db.db_connect import Dbconnect

class Base:
    @staticmethod
    def select(table):
        query = f"SELECT * FROM {table}"
        return Dbconnect.connect(query, "select")

    @staticmethod
    def update(table, column_name, new_data, old_data):
        query = f"UPDATE {table} SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"
        return Dbconnect.connect(query, "update")

    @staticmethod
    def delete(table, column_name, data):
        query = f"DELETE FROM {table} WHERE {column_name} = {data}"
        return Dbconnect.connect(query, "delete")

class Customer(Base):
    def __init__(self, first_name, last_name, username, password, email, bio, headline, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.email = email
        self.bio = bio
        self.headline = headline
        self.phone = phone

    def insert(self):
        query = f"""
            INSERT INTO cutomers(first_name, last_name, username, password, email, bio, headline, phone)
                VALUES ('{self.first_name}', '{self.last_name}', '{self.username}', '{self.password}', '{self.email}', '{self.bio}', '{self.headline}', '{self.phone}')
        """
        return Dbconnect.connect(query, "insert")


class Mentor(Customer):
    def __init__(self, first_name, last_name, username, password, email, bio, headline, phone):
        super().__init__(first_name, last_name, username, password, email, bio, headline, phone)

    def insert(self):
        query = f"""
            INSERT INTO mentor(first_name, last_name, username, password, email, bio, headline, phone)
                VALUES ('{self.first_name}', '{self.last_name}', '{self.username}', '{self.password}', '{self.email}', '{self.bio}', '{self.headline}', '{self.phone}')
        """
        return Dbconnect.connect(query, "insert")


class Statuses(Base):
    def __init__(self, name):
        self.name = name

    def insert(self):
        query = f"""
            INSERT INTO status(name) VALUES ('{self.name}')
        """
        return Dbconnect.connect(query, "insert")

class Languages(Statuses):
    def __init__(self, name):
        super().__init__(name)

    def insert(self):
        query = f"""
            INSERT INTO languages(name) VALUES ('{self.name}')
        """
        return Dbconnect.connect(query, "insert")


class Courses(Base):
    def __init__(self, name, description, raiting, students_bokking_courses, price, status_courses, language_courses, metors_courses):
        self.name = name
        self.description = description
        self.raiting = raiting
        self.students_bokking_courses = students_bokking_courses
        self.price = price
        self.status_courses = status_courses
        self.language_courses = language_courses
        self.metors_courses = metors_courses

    def insert(self):
        query = f"""
            INSERT INTO courses(name, description, raiting, student_bokking_courses, price, status_courses, language_courses, mentors_courses)
                VALUES ('{self.name}', '{self.description}', '{self.raiting}', '{self.students_bokking_courses}' , '{self.price}', '{self.status_courses}', '{self.language_courses}', '{self.metors_courses}')
        """
        return Dbconnect.connect(query, "insert")

    @staticmethod
    def select_inner_join():
        query = """
            SELECT courses.name, courses.description, courses.raiting, courses.student_bokking_courses, courses.price, status.name, languages.name, mentor.first_name FROM courses
                INNER JOIN status ON courses.status_courses = status.status_id
                INNER JOIN languages ON languages.language_id =  courses.language_courses
                INNER JOIN mentor ON mentor.mentor_id = courses.mentors_courses
        """

        return Dbconnect.connect(query, "select")

class Specality(Base):
    def __init__(self, name):
        self.name = name

    def insert(self):
        query = f"""
            INSERT INTO specality(name) VALUES ('{self.name}')
        """
        return Dbconnect.connect(query, "insert")

class Spectality_cpourses(Base):
    def __init__(self, specality, courses):
        self.specality = specality
        self.courses = courses

    def insert(self):
        query = f"""
            INSERT INTO spectality_cpourses(specality, courses) VALUES ('{self.specality}', '{self.courses}')
        """
        return Dbconnect.connect(query, "insert")

    @staticmethod
    def select_inner_join():
        query = f"""
            SELECT specality.name, courses.name FROM spectality_cpourses
                INNER JOIN specality ON spectality_cpourses.spectality_courses_id = specality.specality_id
                INNER JOIN courses ON spectality_cpourses.courses = courses.course_id
        """

        return Dbconnect.connect(query, "select")


class Card_type(Base):
    def __init__(self, name):
        self.name = name

    def insert(self):
        query = f"""
            INSERT INTO card_type(name) VALUES ('{self.name}')
        """
        return Dbconnect.connect(query, "insert")

class Payments(Base):
    def __init__(self, amound, card, customer):
        self.amound = amound
        self.card = card
        self.customer = customer

    def insert(self):
        query = f"""
            INSERT INTO payments(amount, card, customer) VALUES ('{self.amound}', {self.card}, '{self.customer}')
        """
        return Dbconnect.connect(query, "insert")

    @staticmethod
    def select_inner_join():
        query = f"""
            SELECT payment.amount, payment.card, cutomers.first_name, cutomers.last_name FROM payment
                INNER JOIN cutomers ON payment.customer = cutomers.cutomer_id
        """
        return Dbconnect.connect(query,"select")

class Moduls(Base):
    def __init__(self, name, courses, lesson_count):
        self.name = name
        self.courses = courses
        self.lesson_count = lesson_count

    def insert(self):
        query = f"""
            INSERT INTO moduls(name, courses, lesson_count) VALUES ('{self.name}', '{self.courses}', '{self}')
        """
        return Dbconnect.connect(query, "insert")

    @staticmethod
    def select_inner_join():
        query = f"""
            SELECT moduls.name, moduls.courses, moduls.lessons_count FROM moduls 
                INNER JOIN courses ON moduls.courses = courses.course_id
        """
        return Dbconnect.connect(query, "select")

class Lessons(Base):
    def __init__(self, name, moduls):
        self.name = name
        self.moduls = moduls

    def insert(self):
        query = f"""
            INSERT INTO lessons(name, moduls) VALUES ('{self.name}', '{self.moduls}')
        """
        return Dbconnect.connect(query, "insert")

    @staticmethod
    def select_inner_join():
        query = """
            SELECT lessons.name, moduls.name FROM lessons
                    INNER JOIN moduls ON lessons.moduls =  moduls.modul_id
            """

        return Dbconnect.connect(query, "select")


