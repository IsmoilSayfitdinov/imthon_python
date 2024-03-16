from classes import Customer, Mentor, Statuses, Languages, Courses, Specality, Spectality_cpourses, Card_type, Payments, Moduls, Lessons
from db.db_connect import Dbconnect

def customers_table():
    selects = input("""
        1. Insert
        2. Update
        3. Delete
        4. Select
        0. Back
    """)



    if selects == '1':
        firs_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        email = input("Enter Email: ")
        bio = input("Enter Bio: ")
        headline = input("Enter Headline: ")
        phone = input("Enter Phone: ")

        customers = Customer(firs_name, last_name, username, password, email, bio, headline,phone)
        customers.insert()
        return customers_table()
    elif selects == '2':
        column_name = input("Enter Column Name: ")
        new_data = input("Enter New Data: ")
        old_data = input("Enter Old Data: ")

        print(Customer.update("cutomers", column_name, new_data, old_data))
    elif selects == '3':
        column_name = input("Enter Column Name: ")
        data = input("Enter Data: ")
        print(Customer.delete("cutomers", column_name, data))
        return customers_table()
    elif selects == '4':
        data = Customer.select("cutomers")
        for i in data:
            print(f"""
                ID: {i[0]}
                Name: {i[1]} {i[2]}
                Username: {i[3]}
                Password: {i[4]}
                Email: {i[5]}
                Bio: {i[6]}
                Headline: {i[7]}
                Phone: {i[8]}
            """)
        return customers_table()

    elif selects == '0':
        return main()
    else:
        print("Invalid")
        return customers_table()
def mentor():
    selects = input("""
            1. Insert
            2. Update
            3. Delete
            4. Select
            0. Back
        """)

    if selects == '1':
        firs_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        email = input("Enter Email: ")
        bio = input("Enter Bio: ")
        headline = input("Enter Headline: ")
        phone = input("Enter Phone: ")

        metors = Mentor(firs_name, last_name, username, password, email, bio, headline, phone)
        metors.insert()
        return mentor()
    elif selects == '2':
        column_name = input("Enter Column Name: ")
        new_data = input("Enter New Data: ")
        old_data = input("Enter Old Data: ")

        print(Mentor.update("mentor", column_name, new_data, old_data))
    elif selects == '3':
        column_name = input("Enter Column Name: ")
        data = input("Enter Data: ")
        print(Mentor.delete("mentor", column_name, data))
        return customers_table()
    elif selects == '4':
        data = Mentor.select("mentor")
        for i in data:
            print(f"""
                    ID: {i[0]}
                    Name: {i[1]} {i[2]}
                    Username: {i[3]}
                    Password: {i[4]}
                    Email: {i[5]}
                    Bio: {i[6]}
                    Headline: {i[7]}
                    Phone: {i[8]}
                """)
        return mentor()

    elif selects == '0':
        return main()
    else:
        print("Invalid")
        return mentor()
def statuse():
    selects = input("""
                1. Insert
                2. Update
                3. Delete
                4. Select
                0. Back
            """)

    if selects == '1':
        name = input("Enter Name: ")
        status = Statuses(name)
        status.insert()
        return statuse()
    elif selects == '2':
        column_name = input("Enter Column Name: ")
        new_data = input("Enter New Data: ")
        old_data = input("Enter old date: ")
        print(Statuses.update("status", column_name, new_data, old_data))
    elif selects == '3':
        column_name = input("Enter Column Name: ")
        data = input("Enter Data: ")
        print(Statuses.delete("status", column_name, data))
    elif selects == '4':
        data = Statuses.select("status")
        for i in data:
            print(f"""
                ID: {i[0]}
                Name: {i[1]}
            """)
        return statuse()
def language():
    selects = input("""
        1. Insert
        2. Update
        3. Delete
        4. Select
        0. Back
                """)

    if selects == '1':
        name = input("Enter Name: ")
        language_insert = Languages(name)
        language_insert.insert()
        return language()
    elif selects == '2':
        column_name = input("Enter Column Name: ")
        new_data = input("Enter New Data: ")
        old_data = input("Enter old date: ")
        print(Statuses.update("languages", column_name, new_data, old_data))
        return language()
    elif selects == '3':
        column_name = input("Enter Column Name: ")
        data = input("Enter Data: ")
        print(Statuses.delete("languages", column_name, data))
        return language()
    elif selects == '4':
        data = Languages.select("languages")
        for i in data:
            print(f"""
                ID: {i[0]}
                Name: {i[1]}
            """)
def courses():
    selects = input("""
            1. Insert
            2. Update
            3. Delete
            4. Select
            0. Back
                    """)
    if selects == '1':
        name = input("Enter name: ")
        description = input("Enter description: ")
        raiting = float(input("Enter raiting: "))
        student_bokking = int(input("Enter student bokking: "))
        price = int(input("Enter price: "))
        statuse_courses = int(input("Enter statuse courses: "))
        language_courses = int(input("Enter language courses: "))
        mentors_courses = int(input("Enter mentors courses: "))

        course = Courses(name, description, raiting, student_bokking, price, statuse_courses, language_courses, mentors_courses)
        course.insert()
        return courses()
    elif selects == '2':
        column_name = input("Enter column name: ")
        new_data = input("Enter new data: ")
        old_data = input("Enter old data: ")
        print(Courses.update("courses", column_name, new_data, old_data))
        return courses()
    elif selects == '3':
        column_name = input("Enter column name: ")
        data = input("Enter new data: ")
        print(Courses.delete("courses", column_name, data))
        return courses()
    elif selects == '4':
        data = Courses.select_inner_join()
        for i in data:
            print(f"""
                Name: {i[0]}
                Description: {i[1]}
                Raiting: {i[2]}
                Student Bokking: {i[3]}
                Price: {i[4]}
                Status: {i[5]}
                Language: {i[6]}
                Mentor: {i[7]}
            """)
        return courses()
def specality():
    selects = input("""
       1. Insert
       2. Update
       3. Delete
       4. Select
       0. Back
               """)

    if selects == '1':
        name = input("Enter name: ")
        specality_insert = Specality(name)
        specality_insert.insert()
        return specality()
    elif selects == '2':
        column_name = input("Enter column name: ")
        new_data = input("Enter new data: ")
        old_data = input("Enter old data: ")
        print(Specality.update("specality", column_name, new_data, old_data))
        return specality()
    elif selects == '3':
        column_name = input("Enter column name: ")
        data = input("Enter new data: ")
        print(Specality.delete("specality", column_name, data))
        return specality()
    elif selects == '4':
        data = Specality.select("specality")
        for i in data:
            print(f"""
                ID: {i[0]}
                Name: {i[1]}
            """)
    elif selects == '0':
        return main()
def specality_coruses():
    selects = input("""
           1. Insert
           2. Update
           3. Delete
           4. Select
           0. Back
                   """)

    if selects == '1':
        specality = input("Enter specality id: ")
        courses = input("Enter courses id: ")
        specality_coruses_insert = Spectality_cpourses(specality, courses)
        specality_coruses_insert.insert()
        return specality_coruses()
    elif selects == '2':
        column_name = input("Enter new column name: ")
        new_data = input("Enter new data: ")
        old_data = input("Enter old data: ")
        print(Spectality_cpourses.update("spectality_cpourses", column_name, new_data, old_data))
        return specality_coruses()
    elif selects == '3':
        column_name = input("Enter new column name: ")
        data = input("Enter new data: ")
        print(Spectality_cpourses.delete("spectality_cpourses", column_name, data))
        return specality_coruses()
    elif selects == '4':
        data = Spectality_cpourses.select_inner_join()
        for i in data:
            print(f"""
                Specality: {i[0]}
                Courses: {i[1]}
            """)
    elif selects == '0':
        return main()
    else:
        print("Invalid")
        return specality_coruses()
def card_type():
    selects = input("""
       1. Insert
       2. Update
       3. Delete
       4. Select
       0. Back
           """)

    if selects == '1':
        name = input("Enter new name: ")
        card_t = Card_type(name)
        card_t.insert()
        return card_type()
    elif selects == '2':
        column_name = input("Enter new column name: ")
        new_data = input("Enter new data: ")
        old_data = input("Enter old data: ")
        print(Card_type.update("card_type", column_name, new_data, old_data))
        return card_type()
    elif selects == '3':
        column_name = input("Enter new column name: ")
        data = input("Enter new data: ")
        print(Card_type.delete("card_type", column_name, data))
        return card_type()
    elif selects == '4':
        data = Card_type.select("card_type")
        for i in data:
            print(f"""
                ID: {i[0]}
                Name: {i[1]}
            """)
        return card_type()
    elif selects == '0':
        return main()
def payments():
    selects = input("""
           1. Insert
           2. Update
           3. Delete
           4. Select
           0. Back
               """)
    if selects == '1':
        amound = int(input("Enter amound: "))
        card_numbers = int(input("Enter card numbers: "))
        cutomers = int(input("Enter cutomers: "))
        payment = Payments(amound, card_numbers, cutomers)
        payment.insert()
        return payment

    elif selects == '2':
        colum_name = input("Enter new column name: ")
        new_date = input("Enter new date: ")
        old_date = input("Enter old date: ")
        print(Payments.update("payment",colum_name, new_date, old_date))
        return payments()
    elif selects == '3':
        column_name = input("Enter new column name: ")
        data = input("Enter new data: ")
        print(Payments.delete("payment", column_name, data))
        return payments()
    elif selects == '4':
        data = Payments.select_inner_join()
        for i in data:
            print(f"""
                Amount: {i[0]}
                Card: {i[1]}
                Customer: {i[2]}
            """)
        return payments()
    elif selects == '0':
        return main()
def moduls():
    selects = input("""
       1. Insert
       2. Update
       3. Delete
       4. Select
       0. Back
           """)

    if selects == '1':
        name = input("Enter new name: ")
        courses = int(input("Enter new courses id: "))
        lesson_count = int(input("Enter new lesson count: "))

        modul = Moduls(name, courses, lesson_count)
        modul.insert()
        return moduls()
    elif selects == '2':
        column_name = input("Enter new column name: ")
        new_date = input("Enter new date: ")
        old_date = input("Enter old date: ")
        print(Moduls.update("moduls", column_name, new_date, old_date))
        return moduls()
    elif selects == '3':
        column_name = input("Enter new column name: ")
        data = input("Enter new data: ")
        print(Moduls.delete("moduls", column_name,data))
        return moduls()
    elif selects == '4':
        data = Moduls.select_inner_join()
        for i in data:
            print(f"""
                Name: {i[0]}
                Courses: {i[1]}
                Lesson_count: {i[2]}
            """)
        return moduls()

def lesson():
    selects = input("""
       1. Insert
       2. Update
       3. Delete
       4. Select
       0. Back
               """)

    if selects == '1':
        name = input("Enter new name: ")
        moduls = int(input("Enter moduls id: "))
        lessons = Lessons(name, moduls)
        lessons.insert()
        return lesson()
    elif selects == '2':
        column_name = input("Enter new column name: ")
        new_date = input("Enter new date: ")
        old_date = input("Enter old date: ")
        print(Lessons.update("lessons", column_name, new_date, old_date))
        return lesson()
    elif selects == '3':
        column_name = input("Enter new column name: ")
        data = input("Enter new data: ")
        print(Lessons.delete("lessons", column_name, data))
        return lesson()
    elif selects == '4':
        data = Lessons.select_inner_join()
        for i in data:
            print(f"""
                Name: {i[0]}
                Moduls: {i[1]}
            """)
        return lesson()
    elif selects == '0':
        return main()
def main():
    select = input("""
        1. Cutomers
        2. Mentor
        3. Statuses
        4. Language
        5. Courses
        6. Specality
        7. Spectality_cpourses
        8. Card_type
        9. payments
        10. Moduls
        11. Lessons
    """)

    if select == '1':
        return customers_table()
    elif select == '2':
        return mentor()
    elif select == '3':
        return statuse()
    elif select == '4':
        return language()
    elif select =='5':
        return courses()
    elif select =='6':
        return specality()
    elif select =='7':
        return specality_coruses()
    elif select =='8':
        return card_type()
    elif select =='9':
        return payments()
    elif select =='10':
        return moduls()
    elif select =='11':
        return lesson()




if __name__ == '__main__':
        main()